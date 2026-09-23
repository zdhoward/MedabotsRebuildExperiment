# System Design — Autonomous Dev + Blog Pipeline

## Decisions (locked)
- **Project:** Clean-room Medarot battle-system engine → CLI autobattler → later engine port.
- **Language:** Python core now; port to C# (Unity/Godot) when the core is proven.
- **Orchestration:** GitHub Actions daily cron (runs while PC is off) + workflow_dispatch retry
  + concurrency group. Hard caps on session wall-time and tokens.
- **Blog:** Astro static site on Cloudflare Pages (repo `/blog`), domain owned day one,
  RSS day one, AdSense only after ~30 posts and real traffic.
- **Verification:** Machine-enforced, not prompt-enforced. `session_report.json` + artifact
  hashes validated by CI before a post publishes. Tests gate the merge; protected
  `tests/invariants/`; golden baselines for statistical assertions.

## The loop
cron → Actions → agent session (PROMPT.md) → tests green? → telemetry → charts → devlog
→ session_report validated → PR → merge → Cloudflare builds blog. Failure at any gate =
no publish, honest failure post instead.

## Anti-drift guardrails
- One micro-task per session; ROADMAP.md immutable to the agent.
- 2 failures on a task → split/downscope proposal in BACKLOG.
- 3 consecutive failures → halt + alert human.
- Post authenticity: every claimed number must appear in session artifacts.
- Weekly human pass: curate roadmap, polish the week's best post, add an editor's note.

## Future (not now)
- Public dashboard of battle analytics; reader-contributed battle seeds via issues.
- Newsletter (owned list) as primary distribution.
- Dual-agent critic reviewing diffs before merge.
