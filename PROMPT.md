# Daily Session Prompt

Execute the agent contract in `AGENTS.md`. Sequence:

## 1. Context
- Read `STATE.json` → `active_task_id`.
- Read ONLY that task's section in `ROADMAP.md`.
- Read `tests/invariants/README.md`.

## 2. Implement & test
- Minimal changes to satisfy the task's acceptance criteria.
- `cd engine && pytest -q` must pass before anything else happens.
- Fail → one fix attempt → still failing → failure protocol (AGENTS.md #4).

## 3. Telemetry & assets
- `python scripts/run_telemetry.py --seed 42 --output temp/sim_log.json` (skip gracefully if
  the task is not simulation-related).
- Render charts: `python scripts/render_charts.py --input temp/sim_log.json`.
- Write `temp/session_report.json`:
  `{task_id, tests_passed, files_changed, metrics, failure_reason, seed}`.
  Include artifact hashes (state dumps, charts) for authenticity validation.

## 4. Devlog (`blog/src/content/blog/YYYY-MM-DD-<slug>.md`)
- First person, candid, technical. No filler intros ("In today's deep dive..."). Start with
  the problem, a number, or a code snippet.
- Cite ≥3 concrete numbers from the session artifacts.
- Rotate archetypes via `STATE.json.last_post_archetype`; never repeat:
  1. **Autopsy** (a bug/failure/dissection) 2. **Specimen Spotlight** (one mechanic traced deep)
  3. **Research Notes** (what the sources say + what we verified)
  4. **Experiment Log** (hypothesis → data → verdict, e.g. Monte Carlo battle analysis)
- Frontmatter: title, pubDate, task_id, archetype, status (pass|fail), featured_image,
  metrics {…}, commit_sha.
- Link every claim to its artifact (chart file, test name, spec doc).

## 5. State
- Update `STATE.json`: last_run_status, last_post_archetype, consecutive_failures,
  completed_tasks, active_task_id (advance only on success).
- Append discoveries to `BACKLOG.md`.
- Commit on the session branch; the CI publish gate validates the post + session report.
