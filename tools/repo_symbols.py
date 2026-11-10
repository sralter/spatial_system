"""Extract declared callable names and one-based source lines without executing code.

Python uses its standard AST. Rust, Swift, and SQL use pinned Tree-sitter
grammars. These are syntactic locations, not compiler-resolved references.
"""

import ast
from functools import cache
import importlib

from tree_sitter import Language, Parser


GRAMMARS = {".rs": "tree_sitter_rust", ".swift": "tree_sitter_swift", ".sql": "tree_sitter_sql"}
CALLABLES = {
    ".rs": {"function_item", "function_signature_item"},
    ".swift": {
        "function_declaration", "protocol_function_declaration", "init_declaration",
        "deinit_declaration", "subscript_declaration",
    },
    ".sql": {"create_function", "create_procedure"},
}
CONTAINERS = {
    ".rs": {"mod_item", "trait_item", "impl_item"},
    ".swift": {"class_declaration", "protocol_declaration"},
    ".sql": set(),
}


@cache
def _parser(suffix: str) -> Parser:
    module = importlib.import_module(GRAMMARS[suffix])
    return Parser(Language(module.language()))


def _python_symbols(content: bytes) -> tuple[list[tuple[str, int]], str | None]:
    try:
        root = ast.parse(content)
    except (SyntaxError, ValueError, RecursionError) as error:
        return [], f"Python parsing failed ({type(error).__name__}); symbols unavailable"
    symbols = []
    pending = [(root, ())]
    while pending:
        node, scope = pending.pop()
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            scope = (*scope, node.name)
            if not isinstance(node, ast.ClassDef):
                symbols.append((".".join(scope), node.lineno))
        pending.extend((child, scope) for child in reversed(list(ast.iter_child_nodes(node))))
    return symbols, None


def extract_symbols(suffix: str, content: bytes) -> tuple[list[tuple[str, int]], str | None]:
    """Return callable locations plus an explicit warning for incomplete parsing.

    Names include lexical scopes; overloads remain separate entries. Macro
    expansions, dynamically created callables, and embedded SQL bodies are not
    resolved. SQL grammar support does not establish engine-dialect validity.
    """
    if suffix == ".py":
        return _python_symbols(content)
    if suffix not in GRAMMARS:
        return [], None
    tree = _parser(suffix).parse(content)
    symbols = []
    pending = [(tree.root_node, ())]
    while pending:
        node, scope = pending.pop()
        field = node.child_by_field_name("name")
        name = field.text.decode("utf-8", errors="replace") if field else None
        if suffix == ".rs" and node.type == "impl_item":
            target = node.child_by_field_name("type")
            trait = node.child_by_field_name("trait")
            name = target.text.decode("utf-8", errors="replace") if target else None
            if name and trait:
                name += " as " + trait.text.decode("utf-8", errors="replace")
        if node.type in CONTAINERS[suffix] and name:
            scope = (*scope, name)
        if node.type in CALLABLES[suffix]:
            if suffix == ".sql":
                reference = next(
                    (child for child in node.named_children if child.type == "object_reference"),
                    None,
                )
                name = reference.text.decode("utf-8", errors="replace") if reference else None
            if not name and suffix == ".swift":
                name = {
                    "init_declaration": "init", "deinit_declaration": "deinit",
                    "subscript_declaration": "subscript",
                }.get(node.type)
            if name:
                symbols.append((".".join((*scope, name)), node.start_point.row + 1))
                scope = (*scope, name)
        pending.extend((child, scope) for child in reversed(node.named_children))
    warning = (
        "Parser reported errors; symbols may be incomplete"
        if tree.root_node.has_error else None
    )
    return symbols, warning
