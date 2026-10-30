# Rust course workbook workflow

These instructions apply to this course directory and its descendants.

## Course authority and resume point

- Follow `../syllabi/0-rust-for-geospatial-systems-syllabus-v0.2.md` for the curriculum. Use Python, SQL, PostGIS, and GIS bridges and the syllabus's CS Lens.
- Read this directory's `README.md`, the active workbook, and its associated code before teaching or reviewing. Follow their links to historical progress when needed.
- Historical starting evidence: Unit 1 is complete in `../progress/COURSE_PROGRESS_Rust_for_Geospatial_Systems_Unit_01.md`; Unit 2 is in progress in `../progress/checkpoint/_CHECKPOINT_rust-for-geospatial-systems-unit-02-checkpoint-v3.md`.
- The original stopping point is the six geometry prediction questions in that Unit 2 checkpoint. Do not treat them as answered or reviewed without student evidence.
- Record observed progress, not assumed mastery. Earlier exposure to ownership and borrowing does not replace Unit 3.

## Files and lesson scope

- Keep a course index in `README.md` with lesson links, status, the current resume point, and any unresolved questions.
- Use one numbered folder per lesson, containing one `workbook.md` and any associated `.rs`, `.py`, or data files. Prefer Markdown for prose.
- Keep lesson code in its lesson folder. Move or promote code into `rust/spatial-core` only after explicitly agreeing with the student that it is ready to become a reusable portfolio component. Do not move existing historical code as part of routine lesson setup.
- Keep runnable exercises simple. A standalone Rust file may use `rustc`; introduce a lesson-local Cargo package when dependencies or project structure justify it. State the working directory for commands and keep generated binaries out of source folders.
- Each lesson should fit approximately 30 minutes: a small concept or review, familiar-language bridge, prediction, student attempt, and explanation of systems/geospatial implications.
- The initial lesson is one approximately 30-minute refresher of previously covered concepts, ending at the outstanding geometry exercise. New material follows review of that attempt.

## Teaching and solutions

- Generate one lesson at a time. Generate the next lesson only after reviewing the student's current attempt and resolving material gaps, unless the student explicitly requests otherwise.
- Ask the student to predict before compiling or running. Keep predictions separate from observations and revisions.
- Withhold exercise solutions, answer keys, completed implementations, and answer-revealing expected output until the student submits an attempt. Do not conceal premature solutions in collapsed sections or separate files.
- Provide explanatory examples without solving the assigned exercises. Leave substantive exercise code for the student to write; infrastructure and unsolved starter files are appropriate.
- Do not introduce advanced syntax as if already mastered. Teach one new concept at a time and explain unfamiliar scaffolding.
- Distinguish compiler correctness, algorithmic correctness, and geospatial correctness. State relevant CRS, units, and data-model limitations. Measure performance claims when performance becomes relevant.

## Review and durable progress

- Review submitted Markdown answers and code in context. Preserve the student's original responses, predictions, and code attempts; do not silently rewrite them into correct answers.
- Add dated instructor feedback in a clearly labeled section, referencing question IDs and code locations. Explain what is correct, what needs revision, and why; distinguish correctness from idiom and systems/domain reasoning.
- Put student revisions in separate labeled spaces. Before replacing attempted code during review, preserve the original in a clearly named attempt file or another durable record.
- Run checks appropriate to submitted code and report what was actually run. Treat deliberate compiler-error exercises as such, rather than fixing them automatically. Avoid formatting away or changing the student's submission without preserving it.
- Use explicit states: `Not started`, `In progress`, `Awaiting review`, `Revision needed`, and `Complete`. Creation is not completion; instructor feedback is not evidence that the student has made the requested revision.
- Update the workbook and index after review with remaining gaps and the exact next action. At unit completion, create a concise completion record following syllabus section 19 and link it from the index. Preserve historical checkpoints.
- The workbook is the durable lesson and feedback record. Chat may coordinate work, but substantive instruction and reviews belong in the files.
