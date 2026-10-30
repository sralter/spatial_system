# Rust for Geospatial Systems — Workbooks

This is the durable home for lessons, student responses, code exercises, and instructor reviews. The curriculum follows the [v0.2 syllabus](../syllabi/0-rust-for-geospatial-systems-syllabus-v0.2.md); our working agreement is in [AGENTS.md](AGENTS.md).

## Current position

Unit 1 is complete. Unit 2, **Data Has Shape**, is in progress. The most recent historical checkpoint is October 1, 2026; workbook learning begins October 30, 2026.

**Resume here:** Open [Lesson 001](001-returning-to-rust/workbook.md), read the refresher, and fill in the student response spaces. Record predictions before running code. Finish with the six unanswered geometry questions from the checkpoint. Request review when ready; feedback will be added to the workbook while preserving your responses.

| Lesson | Unit | Focus | Status |
| --- | --- | --- | --- |
| [001 — Returning to Rust](001-returning-to-rust/workbook.md) | 1–2 review | Compiler reasoning, representation, ownership recap, geometry predictions | Not started |

**Pending review:** No workbook answers submitted yet. Review depth will be adjusted from the student's attempt. The original six geometry predictions remain unanswered.

**After review:** Resolve any gaps, then create the next Unit 2 lesson on structured enum payloads and combining structs with enums. Methods/`impl`, `Option`/`match` reinforcement, and `if let` follow gradually; they are not assumed mastered.

## How to work

1. Read a lesson and enter answers beneath each question ID. Write uncertainty down rather than looking for an answer key.
2. Write exercise code in that lesson's folder. Follow the workbook's commands and keep predictions, observations, and revisions separate.
3. Change the workbook status to `Awaiting review` and ask for review. Partial attempts can also be reviewed; identify where you stopped.
4. Read the dated instructor feedback and add revisions without deleting the original attempt. The next lesson is generated after review and resolution of material gaps.

Lesson code stays beside its workbook until we agree to promote a reusable component into `rust/spatial-core`. No migration is needed for the existing Unit 1 and Unit 2 artifacts.

## Historical evidence

- [Unit 1 completion record](../progress/COURSE_PROGRESS_Rust_for_Geospatial_Systems_Unit_01.md)
- [Unit 2 checkpoint and exact stopping exercise](../progress/checkpoint/_CHECKPOINT_rust-for-geospatial-systems-unit-02-checkpoint-v3.md)
- [Existing Unit 2 code notes](../../spatial-core/src/bin/unit2_notes.rs)
- [Unit 1 consolidation code](../../spatial-core/src/bin/unit1_consolidation.rs)

Historical records describe progress before the workbook transition. New workbook attempts and reviews provide the evidence for subsequent progress.
