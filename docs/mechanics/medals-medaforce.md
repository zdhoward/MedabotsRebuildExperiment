# Spec: Medals, Skill Levels & Medaforce

Status: DRAFT
Task: T0.5

Scope: Medarot 2 CORE (GBA; English releases "Medabots: Metabee" / "Medabots:
Rokusho"). This spec covers Medal properties (level, attribute, compatibility,
Target/Aim), Skill level progression, and the Medaforce system (gauge, unlocks,
charge, costs).

## Summary

A Medal is the "soul" of a Medabot that supplies evolving combat proficiency
and behavior [S-M][S-S]. It carries: an overall Medal Level that unlocks new
Medaforces and transformations, eight independent Skill levels (one per action
type) that improve combat effectiveness, an Attribute that determines part
compatibility, a compatibility bonus that boosts calculations, and a Target/Aim
that biases target selection [S-M][S-S][S-K].

Medaforce is a chargeable resource (max 80) consumed by special Medal abilities
that unlock at Medal levels 10, 30, and 60; it charges via a dedicated action
(+40) or by taking damage (+20) [S-K][S-R]. Medaforce attacks bypass ordinary
Dodge/Part Defense/Guard, making them hard counters to defensive builds [S-R].

## Sources

- [x] [S-M] Medapedia, "Medals" —
  https://medarot.meowcorp.us/wiki/Medals — link-verified 2026-09-23 (session
  T0.1). Primary source: Medal attribute, compatibility bonus, nature/target,
  XP leveling, skill levels, evolution ranks (levels 0/10/30/60/100 in GB-era
  games), Medaforce/Charge gauge.
- [x] [S-S] Medapedia, "Stats" —
  https://medarot.meowcorp.us/wiki/Stats — link-verified 2026-09-23 (session
  T0.1). Primary source: medal stats list (level, skill levels, attribute/
  compatibility, nature/target, Medaforce).
- [x] [S-K] Kenshin_Xtreme, "Medabots RPG Walkthrough" v3.50 (2004) —
  https://gamefaqs.gamespot.com/gba/915188-medabots-metabee/faqs/24031 —
  link-verified 2026-09-23 (session T0.1). Secondary source: skill levels cap
  at 100 with ~8 uses per skill level increase; Medal evolution at 10/30/60
  levels; +100 evolution for Kabuto/Kuwagata at level 100; Medaforce costs and
  gauge behavior; full Medal FAQ with attributes, aims, compatibility bonuses.
  NOTE: compatibility values conflict with the compiled report's Medal table
  (see BACKLOG.md entry 2026-09-23).
- [x] [S-R] Compiled report, "2026-09-23-medarot2-core-battle-systems-report.md" —
  used as a scaffold only (sections 41-45, 1660-1760). AI-compiled; per repo
  policy not citable as evidence. Rules below were cross-checked against S-M,
  S-S, S-K before labeling.
- [ ] [S-G] Guide: Medarot 2 / 2 CORE / Medabots guide —
  https://medarot.meowcorp.us/wiki/Guide:Medarot_2_/_2_CORE_/_Medabots_guide —
  link-verified 2026-09-23 (session T0.1). Secondary/corroborating source for
  Medal proficiencies and Medaforce.

## Rules (pseudocode)

### Medal core properties

1. Every Medal has: Medal Level, Attribute, Compatibility Bonus, Target/Aim,
   eight Skill levels, learned Medaforces, Medal form/evolution state.
   [DOCUMENTED — S-M, S-S]
2. Medal Level starts at 1 and increases through Robattle experience.
   [DOCUMENTED — S-M, S-R]
3. Medal Level affects: base combat capability, speed, Evasion/Defense
   contributions, Medaforce unlocks, Medal transformations. [DOCUMENTED — S-R]

### Skill level progression

4. There are eight Skill types: Strike, Berserk, Shoot, Snipe/Aim Shot, Defend,
   Heal, Support, Disrupt/Interrupt. [DOCUMENTED — S-S]
5. Each Skill has its own proficiency level, independent of the others.
   [DOCUMENTED — S-R]
6. Skill levels range from 0 to 100 (maximum). [DOCUMENTED — S-K]
7. Using a part with an action of a given Skill type increases that Skill's
   progress counter by 1. [DOCUMENTED — S-R]
8. When a Skill's progress counter reaches 8, that Skill level increases by 1
   and the progress counter resets to 0. [DOCUMENTED — S-K]
9. Higher Skill proficiency improves the corresponding actions' combat
   effectiveness. [DOCUMENTED — S-R]

### Medal Attribute & Compatibility

10. A Medal's Attribute determines which Medapart attributes it is naturally
    compatible with. [DOCUMENTED — S-R]
11. Each Medal has a compatibility bonus value. [DOCUMENTED — S-M]
12. WHEN a part's attribute matches the Medal's Attribute THEN the
    compatibility bonus is added to the Medabot's combat calculations.
    [DOCUMENTED — S-R]
13. Compatibility bonus contributes to: ROS, Evasion/Defense, effectiveness
    of many support/heal/Medaforce effects. [DOCUMENTED — S-R]
14. The compatibility contribution is TEAM-WIDE with respect to that Medabot's
    part set (i.e., all compatible parts on a Medabot contribute their
    combined bonus to the Medabot as a whole, not restricted to individual
    parts). [DOCUMENTED — S-R]
15. Changing one part to an incompatible part reduces the total compatibility
    contribution, but the remaining contribution still applies to the
    Medabot. [DOCUMENTED — S-R]

### Target/Aim system

16. Every Medal has a Target/Aim property specifying a preferred Skill type
    for target selection. [DOCUMENTED — S-S ("nature/target"), S-R]
17. WHEN a Medabot with that Medal selects a targetable enemy THEN the
    Medal's Target/Aim biases targeting toward parts using the preferred Skill
    type. [DOCUMENTED — S-R]
18. Target/Aim is a targeting priority modifier, not a full AI brain;
    it is layered on top of the action chosen for the Medabot.
    [DOCUMENTED — S-R]

### Medal evolution & forms

19. Medals evolve/transform at specific Medal levels: Level 10 (first
    Medaforce), Level 30 (second Medaforce), Level 60 (third Medaforce).
    [DOCUMENTED — S-K, S-R]
20. Kabuto and Kuwagata starter Medals have a fourth transformation at
    Level 100 without a fourth Medaforce. [DOCUMENTED — S-K, S-R]
21. The third Medaforce unlocks at Level 60; sources that label it as Level 50
    are incorrect based on cross-checked English guides. [DOCUMENTED — S-K,
    S-R]

### Medaforce gauge

22. Every Medal has a Medaforce gauge with maximum capacity of 80 MF.
    [DOCUMENTED — S-R]
23. The Medaforce gauge is a shared resource per Medal, not per Medabot.
    [DOCUMENTED — S-R]
24. Using the "charge Medaforce" command adds 40 MF to the gauge.
    [DOCUMENTED — S-K, S-R]
25. Taking damage adds 20 MF to the gauge. [DOCUMENTED — S-K, S-R]
26. MF added cannot exceed the maximum of 80; overflow is discarded.
    [DOCUMENTED — S-R]

### Medaforce unlocks and costs

27. A Medaforce can be used IF: (a) the Medal has learned it, AND (b) the
    Medaforce gauge contains enough MF for its cost. [DOCUMENTED — S-R]
28. Individual Medaforces consume varying amounts: 30, 40, 50, 60, 70, or 80 MF.
    [DOCUMENTED — S-R]
29. An 80-MF Medaforce requires either two charging actions or a combination
    of charging and damage taken to reach full capacity. [DOCUMENTED — S-R]
30. The first Medaforce unlocks at Medal Level 10, second at Level 30, third
    at Level 60. [DOCUMENTED — S-K, S-R]

### Medaforce defensive interaction

31. Normal offensive Medaforce attacks bypass ordinary Dodge, Part Defense,
    and Guard effects. [DOCUMENTED — S-R]
32. Status Medaforces still depend on target status immunity/resistance;
    they can be prevented if the target resists the particular status.
    [DOCUMENTED — S-R]

### Medaforce power formula

33. Medaforce Result = Base Medaforce Power + (Compatibility Bonus / 8) +
    (relevant Medal Skill / 8). [COMMUNITY-TESTED — S-R]
34. The Skill contribution is rounded or truncated per the game's integer
    handling (e.g., 40 Skill -> +5 contribution, 100 Skill -> +12.5 before
    integer handling). [COMMUNITY-TESTED — S-R]
35. This formula applies to many damage and support Medaforces.
    [COMMUNITY-TESTED — S-R]

## Known unknowns / Open questions

- Compatibility bonus values: S-K documents specific values that CONFLICT
  with the compiled report's Medal table (e.g., +7 Tortoise/Jellyfish/Bear in
  the report vs +1 in S-K; Kabuto/Kuwagata at +4 matches both). The exact
  per-Medal compatibility bonus values must be verified against disassembly
  or in-game observation before entering data/. [UNVERIFIED — BACKLOG.md
  2026-09-23 entry, S-K vs report section 49]
- Whether the Medaforce gauge is shared across all Medabots on a team or
  per-Medal/per-Medabot. S-R implies per-Medal; needs in-game confirmation.
  [UNVERIFIED]
- Exact integer handling/rounding for the Medaforce power formula (rule 33-34).
  [UNVERIFIED]
- The complete list of Medaforces per Medal and their exact MF costs. S-R
  documents ranges; individual Medal/Medaforce data needs primary source
  verification. [UNVERIFIED]
- How the Target/Aim weighting algorithm works (score-based? random among
  candidates? distance-weighted?). [UNKNOWN — also noted in battle-flow.md]
- Whether Medaforce charging can be interrupted or has animation time that
  affects battle timer counting. [UNKNOWN]

## Verification plan

1. Cross-check Medal Level breakpoints (10/30/60) and Medaforce gauge
   behavior against Medarot 1 disassembly, justified by Medapedia's claim that
   the battle system is "mostly unchanged since Medarot 1"; record any
   differences as 2 CORE vs Medarot 1.
2. In-game observation against Medabots: Metabee/Rokusho (GBA): verify Skill
   level progression (8 uses per level), Medaforce gauge charging (+40 charge,
   +20 damage), and bypass behavior (rule 31-32).
3. Verify compatibility bonus values by comparing calculated ROS/Evasion/
   Defense values with and without matched attributes in controlled
   in-game setups.
4. Verify Target/Aim bias by observing CPU Medabot targeting patterns with
   different Aim values.

## Derived test oracles

- Skill progression: a Medabot that uses a Strike-type part 8 times gains +1
  Strike Skill level (rule 7-8).
- Medaforce gauge: starting from 0, one charge action brings gauge to 40;
  taking damage once brings it to 60; second charge action caps at 80
  (rule 22, 24-25, 26).
- Medaforce unlock: a Medal at Level 9 cannot use any Medaforce; at Level 10
  it can use its first Medaforce (rule 19, 27, 30).
- Medaforce bypass: an offensive Medaforce with sufficient MF succeeds against
  a target with high Dodge and Part Defense (rule 31).
- Compatibility: a Medabot with all parts matching Medal Attribute has
  higher calculated ROS/Evasion/Defense than the same parts with a
  non-matching Medal (rule 12-13).
