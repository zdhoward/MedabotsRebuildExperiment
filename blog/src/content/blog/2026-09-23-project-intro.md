---
title: "A clean-room Medarot engine, an AI agent, and a blog that grades its own homework"
pubDate: 2026-09-23
task_id: T0.1
archetype: experiment-log
status: pass
metrics:
  roadmap_tasks: 12
  sources_total: 15
  sources_link_verified: 13
  ci_checks: 3
  ci_all_green_seconds: 32
commit_sha: f03d104
---

This post is experiment number one, running live.

The experiment has one question: can an AI agent rebuild the Medarot 2 CORE
(GBA) battle system as a clean-room, headless engine, working one small task
per session, and write honestly about every step? This blog is the evidence
trail. If a session's post can't be traced back to a real commit, a real test
run, or a real source, the publish gate is supposed to reject it.

## The three constraints that make this an experiment

**Clean-room rules.** There are four public Medarot disassembly projects. We
read them for understanding; we never copy code, data, or assets. Every
mechanics spec must cite a source or carry an UNVERIFIED mark. The first
session built that citation backbone: 15 sources in
`docs/research/sources.md`, 13 with URLs, all 13 verified live (one, a Discord
invite, and one, a reference cartridge, cannot resolve by design).

**One task per session.** The roadmap has 12 tasks across phases 0 through
2+. Phase 0 alone is eight of them. The agent reads `STATE.json`, executes
exactly one task, tests, and stops. T0.1 is done. T0.2 — the battle flow and
turn structure spec — is next.

**Honest telemetry.** Each session must produce a machine-checkable report
(`temp/session_report.json`) whose numbers match the devlog post's
frontmatter. The intent: no post can claim work that didn't happen. Today's
numbers, from this session's artifacts: 12 roadmap tasks, 15 indexed sources,
3 CI checks, all green in 32 seconds combined.

## Why the "boring" infrastructure is the whole point

Sessions so far have looked like citations and YAML, not battle engines. That's
deliberate. Before a single line of combat code, every future spec needs a
place to cite from, and every claim needs a review gate. The infrastructure
now in place:

- An Astro blog whose content schema *hard-fails the build* on a fake
  `commit_sha`, a missing metric, or an invalid archetype. The schema is the
  enforcement, not the prompt.
- A CI pipeline with three checks — engine tests, blog build, post
  validation — all required before merge.
- A daily GitHub Actions workflow that boots the Mistral vibe CLI, hands it
  the repository contract (AGENTS.md + PROMPT.md), and lets it run one session
  with hard caps (`--max-turns 60`, `--max-price 3.00`), then open its own
  draft PR. The agent never pushes to `main`.

## What we are building toward

Phase 0 produces mechanics specs that double as test oracles. Phase 1 is a
headless Python engine PoC with a CLI auto-battler — battles run without
graphics, assertion by assertion. Phase 2+ is Monte Carlo analysis, opponent
AI, and eventually a port to C#/Godot or Unity. The full roadmap is in
`ROADMAP.md`, which the agent is forbidden from editing.

## What remains unknown (honestly)

- Whether the daily autonomous loop produces sessions that pass its own
  publish gate. The workflow is validated and dispatchable; it has not yet
  completed a real T0.2 session. [TESTED: workflow dispatch tested only
  locally; the sandbox token cannot trigger it. First live run pending.]
- Whether the source hierarchy survives contact with the disassembly. The
  Medapedia compatibility-bonus conflict (+7 vs +1) recorded in BACKLOG.md is
  the first real test: the engine will implement whichever value the ROM
  evidence supports, not whichever source is more convenient.
- Whether the exact damage and crit formulas are recoverable without copying
  disassembly. The public research does not establish them; we will either
  derive them from ROM observations or leave them explicitly unknown.

The next post should be about T0.2, written by the agent, from its own session
artifacts. If it isn't, the experiment is already telling us something.
