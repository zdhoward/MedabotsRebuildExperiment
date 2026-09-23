# Spec: Battle Flow & Turn Structure

Status: DRAFT
Task: T0.2

Scope: Medarot 2 CORE (GBA; English releases "Medabots: Metabee" / "Medabots:
Rokusho"). This spec covers the battle loop structure only — command phases,
charge/cool movement, battle start/end conditions, and the leader rule. Hit/crit/
damage internals are T0.4; parts/actions are T0.3.

## Summary

A Robattle is not a turn-based RPG: up to three Medabots per side run the same
loop concurrently and asynchronously [S-A]. Each Medabot cycles between a command
line (where it receives orders) and an active line (where it acts); travel time
to the active line is governed by the selected part's Charge (CRG) value and
travel back by its cooldown/Radiation (RAD) value, both modified by leg speed,
leg type, and terrain [S-A][S-B]. The battle ends immediately when either
leader's Head armor reaches 0, or when the battle timer expires [S-A][S-B].

## Sources

- [x] [S-A] Medapedia, "Battle system" —
  https://medarot.meowcorp.us/wiki/Battle_system — re-verified live 2026-09-23
  (session T0.2): leader rule, 1–3 Medarots per side, 6-lane layout, command
  line → active line movement, shooting-vs-melee targeting split, "battles are
  not turn-based".
- [x] [S-B] Autocon, "Medabots: Rokusho — Guide and Walkthrough" v1.3 (2015) —
  https://gamefaqs.gamespot.com/gba/915189-medabots-rokusho/faqs/35357 —
  verified live 2026-09-23 (session T0.2): timer lengths (40/30/20 s), timer
  counting rules (movement only), leader/partner selection, CRG/RAD
  definitions, timer-expiry tie-breaks, Rotation/Auto behavior, command menu.
  Tier 3 (experienced community guide) — strong for observable behavior, not
  ROM proof.
- [x] [S-C] Medapedia, "Parts" — https://medarot.meowcorp.us/wiki/Parts —
  link-verified 2026-09-23 (session T0.1): parts destroyed in battle stay down
  for that battle.
- [ ] [S-D] tiomasta, GameFAQs thread "Explanation of game stats/mechanics
  here" — https://gamefaqs.gamespot.com/boards/915188-medabots-metabee/79284943 —
  verified live (session T0.1). HYPOTHESIS-grade: recovery-turn attack
  weaknesses cited below only where marked.
- [ ] [S-E] Owner-supplied compiled report,
  `docs/research/reports/2026-09-23-medarot2-core-battle-systems-report.md` —
  used as a scaffold only (its §89–96). AI-compiled; per repo policy not
  citable as evidence. Every rule below was re-verified against S-A/S-B before
  being labeled DOCUMENTED.
- [ ] [S-F] Medarot 1 disassembly (github.com/Medabots/medarot1) — read-only
  oracle, not yet consulted for this spec; see Verification plan.

## Rules (pseudocode)

Numbered rules implement the full turn loop. Labels follow
`docs/planning/content-rules.md` §8. "Functioning" below means: Head armor > 0.

### Battle setup

1. Each side fields 1–3 Medabots. [DOCUMENTED — S-A]
2. `leader = first Medarot selected`; remaining are Partners. [DOCUMENTED — S-A, S-B]
3. Player Medabots start at the command line, left side; enemy at the command
   line, right side; one of 6 lanes per Medabot (3 per side). [DOCUMENTED — S-A]
4. Battle timer is configured to 20, 30, or 40 seconds before the battle
   starts. [DOCUMENTED — S-B]
5. `battle.over = false`; timer starts. [DOCUMENTED — S-B; start-frame behavior UNKNOWN]

### Command phase (per Medabot, at the command line)

6. The Medabot's fighter may issue a command: use Head, use Right Arm, use
   Left Arm, use Medaforce 1–3, or charge the Medaforce gauge. [DOCUMENTED — S-B]
7. IF Auto is enabled THEN the command is taken from the Medal's Rotation
   sequence, which advances one entry per executed action. Manual commands
   also advance the rotation pointer; Auto resumes from the corresponding
   point, it does not restart. [DOCUMENTED — S-B]
8. IF the action is ranged (shooting/support/heal) THEN its target Medabot
   (and part) is selected and highlighted BEFORE the command is issued.
   [DOCUMENTED — S-A]
9. IF the action is melee (physical) THEN no target is pre-selected; the
   target is chosen at the active line. [DOCUMENTED — S-A]
10. Target selection is weighted by the acting Medal's Target/Aim (skill-type
    preference). Exact weighting algorithm: UNVERIFIED (no source publishes it;
    see Known unknowns). [DOCUMENTED that Aim influences targeting — S-A
    ("nature"), S-B (Aim menu); weighting algorithm UNKNOWN]

### CRG phase (command line → active line)

11. On command, the Medabot moves toward the active line. Travel time is a
    function of the selected part's Charge (CRG) value, leg
    speed/propulsion, leg type, and terrain; lower CRG = faster. [DOCUMENTED —
    S-A, S-B; exact formula UNVERIFIED]
12. The battle timer advances ONLY while any Medabot is moving toward or away
    from the active line. It does not advance during command selection or
    action execution. [DOCUMENTED — S-B]

### Action resolution (at the active line)

13. On arrival, the Medabot executes its commanded action: hit/miss, critical,
    damage or effect, status, chain, part destruction. [DOCUMENTED that these
    occur — S-A, S-B; resolution ORDER and formulas are T0.4 scope, UNVERIFIED
    here]
14. IF the action was ranged AND its pre-selected target is already destroyed
    or shut down at execution time THEN the action fails (GB-era behavior;
    later games retarget instead). [DOCUMENTED — S-A]
15. IF the action was melee THEN the target is the enemy closest to the active
    line at execution time. [DOCUMENTED — S-A]

### RAD phase (active line → command line)

16. After acting, the Medabot returns to the command line. Travel time is a
    function of the used part's Radiation/cooldown (RAD) value (and the same
    movement modifiers); lower RAD = faster. [DOCUMENTED — S-A, S-B; exact
    formula UNVERIFIED]
17. Recovery-turn vulnerability states (attack-type weaknesses while
    returning) are claimed by community testing but not established by a
    citable methodology. [HYPOTHESIS — S-D; T0.4 scope]
18. On reaching the command line the Medabot is READY for the next command;
    goto 6. [DOCUMENTED — S-A, S-B]

### Concurrency

19. Rules 6–18 run independently and asynchronously for every fielded
    Medabot. There are no global, alternating turns. [DOCUMENTED — S-A
    ("battles are not turn-based"), S-B]

### Part destruction and battle end

20. When any part's armor reaches 0, that part is destroyed and unusable for
    the rest of the battle. [DOCUMENTED — S-C, S-B]
21. WHEN a Partner's Head is destroyed THEN that Partner stops functioning;
    the battle continues. [DOCUMENTED — S-A, S-B]
22. WHEN either Leader's Head armor reaches 0 THEN the battle ends
    immediately (victory for the other side). [DOCUMENTED — S-A, S-B]
23. WHEN the timer expires THEN:
    a. the side with more functioning Medabots wins;
    b. ELSE the side with more functioning (undestroyed) Medaparts wins;
    c. any further tie: UNKNOWN — the guide author explicitly leaves this
    unresolved, and no other source establishes it. [DOCUMENTED for a/b — S-B;
    UNKNOWN for c]
24. After the battle, destroyed parts are restored automatically. [DOCUMENTED — S-B, S-C]

## Known unknowns / Open questions

- Timer internals: what a "second" of battle timer is in frames, whether the
  timer ticks per-Medabot-movement or globally, and pause/edge behavior —
  no source establishes these. [UNKNOWN — needs ROM-level research; see S-F]
- Target/Aim weighting: both S-A and S-B confirm Aim biases targeting toward
  a skill type, but neither publishes the algorithm (score? random among
  candidates? distance-weighted?). [UNKNOWN]
- CPU opponent command/target choice: no citable source documents the CPU's
  decision routine. [UNKNOWN — must not be invented]
- CRG/RAD exact formulas and whether CRG/RAD are shared stats per part or
  derived per action. [UNKNOWN — T0.3/T0.4]
- Melee "closest to the active line": tie-breaking when two enemies are
  equidistant. [UNKNOWN]
- Whether rules 12 and 22 interact (timer frozen during the final action that
  kills a leader). [UNKNOWN]

## Verification plan

1. Cross-check rules 6–23 against the Medarot 1 disassembly (S-F) battle loop
   routines — justified by S-A's claim that the system is "mostly unchanged
   since Medarot 1", but every mismatch must be recorded as a 2 CORE vs
   Medarot 1 difference, never silently harmonized.
2. In-game observation against Medabots: Metabee/Rokusho (GBA): seeded
   headless replays once Phase 1 lands; until then, manual observation of
   timer counting (rule 12) and ranged-target failure (rule 14).
3. Engine tests derived below become invariants when Phase 1 implements the
   loop.

## Derived test oracles

- Battle-end condition: a test battle where the enemy leader's head armor
  reaches 0 ends immediately, even with partners alive (rule 22).
- Timer expiry: with fixed "movement-time" inputs, a battle that exhausts the
  configured timer resolves by 23a, then 23b (23c is asserted UNIMPLEMENTED
  until evidence arrives).
- Ranged-target failure: a ranged action whose pre-selected target is
  destroyed mid-CRG fails (rule 14); the same action against a living target
  does not.
- Melee targeting: with enemy positions at distinct distances, a melee action
  hits the closest (rule 15).
- Rotation pointer: manual interleaving advances the rotation pointer; Auto
  resumes from the advanced position (rule 7).
- Concurrency: two Medabots with different CRG values issue their actions in
  CRG order, not in slot order (rules 11, 19).
