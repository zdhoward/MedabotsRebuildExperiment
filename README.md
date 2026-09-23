# Medabots Rebuild Experiment

An autonomous AI development experiment: rebuild the **Medarot (Medabots) battle system** as a
clean-room, headless engine — while a scheduled AI agent does the work daily and blogs the
journey at each step.

## The idea

1. **Research** the battle mechanics meticulously (Medapedia, community docs, and the
   existing Medarot disassembly projects as *reference oracles* — never as copy-paste source).
2. **Rebuild** the system as a deterministic, headless Python engine: a CLI auto-battler with
   full Medabot rosters, parts, medals, and battle mechanics.
3. **Blog** every working session. The Astro site in `/blog` publishes each session's devlog,
   charts, and battle replays automatically.
4. **Port** to a game engine (C#/Godot or Unity) once the core is proven.

## Repository layout

```
docs/
  mechanics/     Battle-system specs. Each spec doc = test oracles for the engine.
  research/      Source index: links, notes, citations, open questions.
  planning/      System design, decisions, roadmap rationale.
data/            Game data tables (parts, medals, medabots) as original-format JSON.
engine/          Headless battle engine (Python package: medarot/ + tests/).
blog/            Astro static site — the public devlog.
scripts/         Session tooling: telemetry, chart rendering, blog post generation.
temp/           Session scratch (raw logs, session reports). Gitignored except reports.
AGENTS.md        The agent's contract: rules, scope, failure protocol.
ROADMAP.md       The immutable task list. Human-owned; agent never edits.
STATE.json       Machine-readable session state: active task, failures, archetype.
BACKLOG.md       Agent-recorded discoveries. Never implemented without human promotion.
PROMPT.md        The daily session prompt.
```

## Status

Phase 0 — Research. See `ROADMAP.md`.

## Legal / clean-room policy

This project implements game *mechanics* (uncopyrightable facts and systems) as original code.
We never copy code, assets, or data tables verbatim from ROMs, decompilation projects, or
proprietary sources. Reading disassembly for understanding is allowed; pasting is not.
The engine is non-commercial fan research; Medarot/Medabots is © Imagineer.
