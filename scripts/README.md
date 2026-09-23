# Session tooling

- `run_telemetry.py` — run seeded battles, emit `temp/sim_log.json` (battle stats, RNG seed).
- `render_charts.py` — deterministic chart PNGs from telemetry for blog posts.
- `validate_post.py` — blog post authenticity gate: every metric claimed in frontmatter must
  appear in `temp/session_report.json`; images must exist; archetype must differ from the
  previous post. Non-zero exit = CI blocks publish.

These are built incrementally by roadmap tasks; placeholders are replaced as Phases progress.
