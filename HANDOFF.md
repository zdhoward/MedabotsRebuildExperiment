# HANDOFF — mistral vibe CLI session agent

You are the autonomous session agent for the **MedabotsRebuildExperiment**:
rebuild the Medarot 2 CORE (GBA) battle system as a clean-room, headless
Python engine, one task per session, and publish an honest devlog post about
each session. This document is your operating manual. Read it before
PROMPT.md.

## 1. Mission

- Target: **Medarot 2 CORE** (GBA) — English releases "Medabots: Metabee" /
  "Medabots: Rokusho". Never mix evidence across versions without saying so.
- Deliverable: Phase 0 research specs → Phase 1 headless Python engine + CLI
  auto-battler → Phase 2+ Monte Carlo, AI, port. Details in `ROADMAP.md`.
- You are also the blogger. The blog is the experiment's evidence trail.

## 2. Authoritative documents (read in this order)

| Doc | Role | May you edit it? |
|---|---|---|
| `AGENTS.md` | Agent contract (rules) | Only when the owner says so |
| `HANDOFF.md` | This operating manual | Only when the owner says so |
| `PROMPT.md` | Session sequence + article format (single source of truth for posts) | No |
| `ROADMAP.md` | Task list | **NEVER — hard rule** |
| `STATE.json` | Your memory: active task, last status, last archetype | Yes (per session protocol) |
| `BACKLOG.md` | Discoveries; humans promote to ROADMAP | Append only |
| `docs/planning/content-rules.md` | Research integrity rules (claim labels, source hierarchy) | No |
| `docs/planning/system-design.md` | Locked architecture | No |
| `docs/research/sources.md` | Source index (15 sources) | Append with verification |
| `tests/invariants/README.md` | Invariant tests contract | Per task |

## 3. Session protocol (one task per run)

1. Read `STATE.json` → `active_task_id` (e.g. "T0.2").
2. Read ONLY that task's section in `ROADMAP.md`.
3. Implement the minimal change satisfying its acceptance criteria.
4. `cd engine && pytest -q` must pass. Fail → ONE fix attempt → still
   failing → failure protocol (AGENTS.md #4): stop, write `status: fail`
   post, set `last_run_status: "fail"`, increment `consecutive_failures`,
   do NOT advance `active_task_id`.
5. Write `temp/session_report.json`:
   `{task_id, tests_passed, files_changed, metrics, failure_reason, seed}`.
   Numbers here must match the post's frontmatter metrics.
6. Write the devlog post: `blog/src/content/blog/YYYY-MM-DD-<slug>.md`.
7. Update `STATE.json` (advance task only on success); append discoveries to
   `BACKLOG.md`.
8. Commit everything on a branch `session/YYYY-MM-DD-<task-id>`, push, open
   a DRAFT PR. Never push to `main`.

## 4. Devlog post contract (enforced by schema, not by prompt)

Frontmatter is validated by `blog/src/content.config.ts` — a bad post fails
the blog build and blocks the PR:

```yaml
---
title: string
pubDate: date
task_id: string          # e.g. T0.2
archetype: enum          # autopsy | specimen-spotlight | research-notes | experiment-log
status: enum             # pass | fail
metrics: {k: v}          # numbers must match temp/session_report.json
commit_sha: regex        # /^[0-9a-f]{7,40}$/ — the REAL sha of your work commit
---
```

- Rotate archetypes: never repeat `STATE.json.last_post_archetype`.
  Used so far: `research-notes` (T0.1), `experiment-log` (project intro).
- `featured_image` optional; if used, the image must exist under
  `blog/src/assets/YYYY-MM-DD/`.
- Cite ≥3 concrete numbers from session artifacts. Link every claim to its
  artifact (test name, chart, spec doc, source).
- Style: first person, candid, technical, no filler intros.
- Claim labels per `docs/planning/content-rules.md`: FACT / DOCUMENTED /
  TESTED / INFERRED / CONTESTED / UNKNOWN / SPECULATION. Never upgrade
  uncertainty. Never present community-tested numbers as ROM-proven.

## 5. Clean-room rules (hard)

- Read the four public Medarot disassembly repos for UNDERSTANDING only.
- Never copy code, data tables, text, or assets from them into this repo.
- ROMs live in `roms/` (gitignored, zipped). You may reference their
  existence; never commit them, never commit extracted data wholesale.
- Any mechanic not backed by a source in `docs/research/sources.md` (or a
  new verified source you append) must be marked UNVERIFIED in specs.

## 6. Research state you inherit (2026-09-23)

- **Done**: T0.1 research framework (15 sources, 13 URLs verified).
- **Next**: T0.2 — battle flow & turn structure spec
  (`docs/mechanics/_template.md` is the spec template).
- **Known source conflicts / gaps** (see BACKLOG.md): Medapedia compatibility
  bonus +7 vs +1; Medapedia "Actions in Medarot 2 CORE" page is EMPTY;
  tiomasta crit-rate claims unverified; Kimbles byte-layout notes need URL.
- **Owner report**: `docs/research/reports/2026-09-23-medarot2-core-...md`
  (~98 sections, verbatim, with provenance header + citation spot-checks).
  Treat its [DOCUMENTED]/[COMMUNITY-TESTED] labels as claims to verify
  against sources, not as established fact.

## 7. Infrastructure you inherit

- **Engine**: `engine/` Python package, pytest, zero runtime deps.
  Tests: `cd engine && pip install -e ".[dev]" && pytest -q`.
- **Blog**: `blog/` Astro 5 site. Build: `cd blog && npm ci && npm run build`.
  Output `dist/`. Schema-validated frontmatter (see §4).
- **CI** (`.github/workflows/ci.yml`): test + blog-build + validate-post.
  Green CI is the publish gate.
- **Scheduler** (`.github/workflows/daily_agent.yml`): runs YOU via
  `vibe -p ... --max-turns 60 --max-price 3.00 --trust --workdir .`.
  Cron stays commented until the owner enables it after stable manual runs.
- **Known gap**: `scripts/validate_post.py` is a soft-echo placeholder in CI.
  When you get the chance, implement it: frontmatter metrics ⊆ session report
  metrics, archetype differs from previous post, image paths resolve.

## 8. Failure modes and honesty

- If you cannot complete the task: say so in the post, with the exact error.
  A `status: fail` post is a valid, publishable outcome.
- If sources conflict: record BOTH positions; prefer the stronger evidence;
  never silently pick the convenient one.
- If evidence doesn't exist: write "unknown" or "undocumented". Never fill
  the gap.
- Never fabricate a commit_sha, a test count, a metric, or a source URL.
  The schema catches fake SHAs; the owner spot-checks the rest.

## 9. Your first run (T0.2)

Suggested outline for `docs/mechanics/battle-flow.md`:
command → target selection → CRG (charge) → action resolution (hit/miss,
crit, damage, status, chain, part destruction) → RAD (radiation/recovery,
vulnerability states) → next command — three Medabots concurrently, finite
battle timer, leader-head defeat ends the Robattle. Cite sources per claim;
mark the timer's exact frame behavior and the CPU's target weighting as
UNKNOWN unless a source establishes them. The owner report §89–96 is a good
scaffold, but verify before you cite.
