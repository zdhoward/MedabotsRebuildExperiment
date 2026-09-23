# ROADMAP

Immutable task list. The agent NEVER edits this file. Humans add/split tasks via PR.
Format: `### <id>: <title>` with acceptance criteria that are test-checkable.

## Phase 0 — Research (mechanics specs, each doc = future test oracles)

### T0.1: Set up research framework
Create `docs/mechanics/_template.md` (sections: Summary, Sources, Rules as pseudocode,
Open Questions, Verification Plan) and fill `docs/research/sources.md` with the known
source list. Acceptance: template exists, sources.md lists ≥6 sources with URLs and notes.

### T0.2: Spec — battle flow & turn structure
Charge/cool time, command phases, battle start/end conditions, leader defeat.
Sources: Medapedia battle system page + Medarot 1/2 observation. Acceptance: doc covers
full turn loop as numbered pseudocode; every rule carries a source or is marked UNVERIFIED.

### T0.3: Spec — parts & actions
Head (finite uses), arms (infinite), legs (terrain/movement/defense), success/aim mechanics,
action types (Shoot, Strike, Snipe, Berserk, Defend, etc.). Acceptance: action taxonomy table
with all base action types documented.

### T0.4: Spec — damage & success formulas
Pull together what is known/believed about damage calculation, success rates, crits.
Mark every formula VERIFIED (source) vs HYPOTHESIS (needs testing). Acceptance: every formula
has provenance and a proposed in-game test to verify it.

### T0.5: Spec — medals, skill levels & Medaforce
Medal skill leveling, medal-part affinity, Medaforce charge mechanics. Acceptance: doc
explains skill level progression rules with sources.

### T0.6: Spec — terrain & legs interaction
Leg types (two-leg, multi-leg, wheel, flight, etc.) × terrain (grass, forest, desert, etc.)
speed/defense effects. Acceptance: interaction matrix drafted, unknown cells marked.

### T0.7: Data schema v1
Define JSON schemas (`data/schemas/`) for Medabots, Parts, Medals. Acceptance: schema files
validate against sample entries for 3 real Medabots researched from community data.

### T0.8: Seed dataset — starter roster
Research and enter (in our own format) the data for ~10 Medabots, all their parts, and
~5 medals. Acceptance: dataset validates against schemas; every entry cites its source.

## Phase 1 — Headless engine PoC

### T1.1: Engine skeleton + first failing test
Python package `medarot`, pytest configured, a test that asserts a Battle can be constructed.
Acceptance: `pytest` runs green with one trivial passing test and CI workflow executes it.

### T1.2: Data loading
Load `data/*.json` into typed model objects with validation errors surfaced clearly.

### T1.3: Turn loop skeleton
Charge/cool time progression, command selection stubs, deterministic seeded RNG. Acceptance:
a seeded 1v1 battle runs to completion with a reproducible log given the same seed.

### T1.4–T1.10: (humans to define after T0 specs stabilize — actions, damage,
targeting, success rolls, head-ammo, defeat conditions, 3v3, CLI autobattler)

## Phase 2+ — Fidelity, Monte Carlo analysis, opponent AI, engine port
(to be planned when Phase 1 completes)
