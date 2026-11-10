"""Exercise callable declarations and qualification across all supported languages."""

import unittest

from repo_symbols import extract_symbols


class SymbolTests(unittest.TestCase):
    def test_python_async_methods_nested_functions_and_strings(self):
        source = b'''# def fake(): pass
text = "def also_fake(): pass"
class Reader:
    async def read(self):
        def decode():
            pass
'''
        symbols, warning = extract_symbols(".py", source)
        self.assertEqual(symbols, [("Reader.read", 4), ("Reader.read.decode", 5)])
        self.assertIsNone(warning)

    def test_rust_modules_trait_requirements_and_impls(self):
        source = b'''// fn fake() {}
const TEXT: &str = "fn also_fake() {}";
mod query {
    pub trait Reader { fn read(&self); }
    struct Copc;
    impl Reader for Copc { fn read(&self) {} }
    impl Copc { pub fn open() {} }
}
'''
        symbols, warning = extract_symbols(".rs", source)
        self.assertEqual(symbols, [
            ("query.Reader.read", 4), ("query.Copc as Reader.read", 6),
            ("query.Copc.open", 7),
        ])
        self.assertIsNone(warning)

    def test_swift_methods_overloads_initializers_protocols_and_extensions(self):
        source = b'''// func fake() {}
struct Point {
    init() {}
    func distance() {}
    func distance(to other: Point) {}
}
protocol Reader {
    func read()
}
extension Point {
    func extra() {}
}
'''
        symbols, warning = extract_symbols(".swift", source)
        self.assertEqual(symbols, [
            ("Point.init", 3), ("Point.distance", 4), ("Point.distance", 5),
            ("Reader.read", 8), ("Point.extra", 11),
        ])
        self.assertIsNone(warning)

    def test_sql_declared_functions_and_procedures_not_calls_or_tables(self):
        source = b'''-- CREATE FUNCTION fake() RETURNS int;
CREATE TABLE points (z integer);
CREATE FUNCTION public.total(x integer) RETURNS integer
LANGUAGE SQL AS $$ SELECT x; $$;
CREATE PROCEDURE public.refresh() LANGUAGE SQL AS $$ SELECT 1; $$;
SELECT public.total(1);
'''
        symbols, warning = extract_symbols(".sql", source)
        self.assertEqual(symbols, [("public.total", 3), ("public.refresh", 5)])
        self.assertIsNone(warning)

    def test_parse_failures_are_explicit(self):
        symbols, warning = extract_symbols(".py", b"def unfinished(")
        self.assertEqual(symbols, [])
        self.assertIn("symbols unavailable", warning)
        _, warning = extract_symbols(".rs", b"fn unfinished(")
        self.assertIn("incomplete", warning)


if __name__ == "__main__":
    unittest.main()
