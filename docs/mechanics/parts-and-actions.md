# Spec: Parts & Actions

Status: DRAFT
Task: T0.3

Scope: Medarot 2 CORE (GBA; English releases "Medabots: Metabee" / "Medabots: Rokusho").
This spec covers part types, their statistics, success/aim mechanics, and the complete
action taxonomy. Damage formulas and success-rate calculations are T0.4 scope.

## Summary

A Medabot is assembled from four parts: Head, Right Arm, Left Arm, and Legs [S-1].
Each part type has distinct statistics and roles in battle. Heads have finite Uses for
their action; arms have infinite uses but finite Charge/ Radiations (CRG/RAD) cycles;
legs provide movement, defense, and terrain interaction [S-1][S-2][S-3].

Actions are categorized by Skill (Strike, Berserk, Shoot, Aim Shot, Defend, Heal,
Support, Interrupt) and by Attribute (e.g., Grapple, Optic, Bomb) [S-2][S-3].
The Medal's Target/Aim statistic biases which opponent part is selected for actions
that accept a target, but the exact weighting algorithm remains undocumented [S-1][S-2].

## Sources

- [x] [S-1] Medapedia, "Parts" — https://medarot.meowcorp.us/wiki/Parts —
  link-verified 2026-09-23 (session T0.1): four-part composition, parts destroyed
  in battle stay down for that battle, armor restoration after battle.
- [x] [S-2] Medapedia, "Stats" — https://medarot.meowcorp.us/wiki/Stats —
  link-verified 2026-09-23 (session T0.1): part statistics for heads/arms/legs,
  the 11 series skills list, skill vs attribute distinction.
- [x] [S-3] Medapedia, "Leg type" — https://medarot.meowcorp.us/wiki/Leg_type —
  link-verified 2026-09-23 (session T0.1): seven leg types, terrain bonus/penalty system.
- [x] [S-4] Kenshin_Xtreme, "Medabots RPG Walkthrough" v3.50 (2004) —
  https://gamefaqs.gamespot.com/gba/915188-medabots-metabee/faqs/24031 —
  verified live 2026-09-23 (session T0.1): attack types, Aim attribute, skill leveling.
- [x] [S-5] Imaku, "Guide and Walkthrough" (Medabots: Metabee) —
  https://gamefaqs.gamespot.com/gba/915188-medabots-metabee/faqs/32327 —
  verified live 2026-09-23 (session T0.1): part categories in English terms.
- [ ] [S-6] Medapedia, "User:Kimbles/Medarot 1 Hacking Notes" —
  https://medarot.meowcorp.us/wiki/User:Kimbles/Medarot_1_Hacking_Notes —
  per-part byte layout (attribute, action, armor, skill, success, power, pierce,
  uses/charge, cooldown). UNVERIFIED for Medarot 2 CORE; applicable as cross-check
  only if Medarot 1 mechanics match 2 CORE (see battle-flow.md).
- [ ] [S-7] tiomasta, GameFAQs thread "Explanation of game stats/mechanics here" —
  https://gamefaqs.gamespot.com/boards/915188-medabots-metabee/79284943 —
  HYPOTHESIS-grade claims about success/evasion interactions; methodology not stated.

## Rules (pseudocode)

### Part composition

1. A Medabot requires exactly four parts: Head + Right Arm + Left Arm + Legs.
   [DOCUMENTED — S-1]
2. Parts destroyed during a Robattle remain unusable for the rest of that
   Robattle. [DOCUMENTED — S-1]
3. At the end of a Robattle, all part Armor and Head Uses are restored for the
   next battle. [DOCUMENTED — S-1]

### Head parts

4. Head parts have these statistics: Armor, Rate of Success (ROS), Power,
   Uses, Skill, Action, Attribute. [DOCUMENTED — S-2][S-4]
5. Head parts do NOT display Charge or Radiation values in-game; they may or
   may not have internal CRG/RAD values. [DOCUMENTED that they do not display — S-2;
   internal CRG/RAD existence UNKNOWN]
6. Head.Armor = HP of the head part. When Head.Armor reaches 0, the part is
   destroyed. [DOCUMENTED — S-2]
7. Head.Uses = maximum number of times the Head's Action can be invoked during
   a single Robattle. [DOCUMENTED — S-2][S-4]
8. Head.ROS contributes to success/accuracy/critical calculations. [DOCUMENTED — S-2]
9. Head.Power determines the base strength of the Head's Action. [DOCUMENTED — S-2]
10. Head.Skill is one of the eight skill categories (see Action taxonomy).
    [DOCUMENTED — S-2]
11. Head.Action is the specific action the Head performs (e.g., Laser, Repair).
    [DOCUMENTED — S-2]
12. Head.Attribute is the compatibility category (e.g., Grapple, Optic).
    [DOCUMENTED — S-2]
13. When the Leader's Head.Armor reaches 0, the Robattle ends immediately.
    [DOCUMENTED — S-1]

### Arm parts (Right and Left)

14. Arm parts have these statistics: Armor, Rate of Success (ROS), Power,
    Charge (CRG), Radiation (RAD), Skill, Action, Attribute.
    [DOCUMENTED — S-2][S-4]
15. Arm.Armor = HP of the arm part. When Arm.Armor reaches 0, the part is
    destroyed and unusable for the rest of the battle. [DOCUMENTED — S-1][S-2]
16. Arm.ROS contributes to success/accuracy/critical calculations.
    [DOCUMENTED — S-2]
17. Arm.Power determines the base strength of the arm's Action.
    [DOCUMENTED — S-2]
18. Arm.CRG = time it takes the Medabot to move from command line to active line
    to execute the arm's Action. Lower CRG = faster. [DOCUMENTED — S-2][S-4]
19. Arm.RAD = time it takes to recover after the action (return to command line).
    Lower RAD = faster. [DOCUMENTED — S-2][S-4]
20. Arm.Skill is one of the eight skill categories. [DOCUMENTED — S-2]
21. Arm.Action is the specific action the arm performs (e.g., Sword, Missile).
    [DOCUMENTED — S-2]
22. Arm.Attribute is the compatibility category. [DOCUMENTED — S-2]
23. Arms have infinite Uses: an arm's Action can be invoked any number of times
    in a Robattle (subject to CRG/RAD timing). [DOCUMENTED — S-2][S-4]
24. The Right Arm is USUALLY faster/less powerful and the Left Arm USUALLY
    slower/more powerful, but this is a design tendency, not a mechanical
    rule. Individual parts determine their actual CRG/RAD/Power values.
    [DOCUMENTED — S-2]

### Leg parts

25. Leg parts have these statistics: Armor, Propulsion, Evasion, Defense,
    Proximity, Remoteness, Leg type / terrain compatibility.
    [DOCUMENTED — S-2][S-3]
26. Leg.Armor = HP of the leg part. When Leg.Armor reaches 0, the Medabot
    loses its mobility and terrain bonuses, and the part is unusable.
    [DOCUMENTED — S-1][S-2]
27. Leg.Propulsion affects movement speed during CRG and RAD phases.
    [DOCUMENTED — S-2][S-4]
28. Leg.Evasion affects whether attacks can be dodged. Community testing
    reports Evasion also participates in damage reduction calculations, not
    merely the binary dodge check. [DOCUMENTED that Evasion affects dodge — S-2;
    damage reduction participation HYPOTHESIS — S-7]
29. Leg.Defense affects damage reduction and whether normal Part Defense can
    activate. [DOCUMENTED — S-2]
30. Leg.Proximity is used by close-range/melee actions and several supportive
    actions. [DOCUMENTED — S-2]
31. Leg.Remoteness is used by ranged actions and several remote/support/
    disruption actions. [DOCUMENTED — S-2]
32. Leg.Propulsion also affects Berserk damage: effective Berserk Power =
    Part Power + (Propulsion / 2). [DOCUMENTED — S-4]
33. Exact numerical contributions of Proximity, Remoteness, Evasion, Defense
    to damage/success formulas: T0.4 scope, UNVERIFIED here.
    [UNVERIFIED]

### Leg types

34. The seven leg types are: Bipedal, Multi-leg, Wheeled, Tank, Hover/Float,
    Flying, Aquatic. [DOCUMENTED — S-3]
35. Each leg type has terrain compatibility bonuses/penalties that affect
    effective speed and defense on specific terrain types. [DOCUMENTED — S-3]
36. Flying leg types have high Propulsion/Evasion/Defense but are vulnerable
    to Anti-Air actions. [DOCUMENTED — S-3]
37. Aquatic leg types have high mobility on water terrain but are vulnerable
    to Anti-Sea actions. [DOCUMENTED — S-3]
38. The complete leg-type x terrain interaction matrix: T0.6 scope, UNKNOWN here.
    [UNKNOWN]

### Success / Aim mechanics

39. Every Medal has a Target/Aim statistic that represents a skill-type
    preference for targeting. [DOCUMENTED — S-2][S-4]
40. For actions that accept target selection (ranged actions pre-select a
    target before CRG; melee actions select at the active line), the Medal's
    Target/Aim biases which opponent part is chosen. [DOCUMENTED — S-1][S-2]
41. Exact Target/Aim weighting algorithm (scoring function, distance weighting,
    random tie-breaking): no citable source publishes it. [UNKNOWN]
42. Part Rate of Success (ROS) contributes to success/accuracy/critical
    calculations. The exact formula: T0.4 scope, UNVERIFIED here.
    [UNVERIFIED]
43. Community testing (tiomasta) claims crits are deterministic (ROS vs
    Evasion+Defense) with a small random factor. Methodology not stated;
    treat as HYPOTHESIS. [HYPOTHESIS — S-7]

### Actions vs Skills vs Attributes

44. Action = the specific thing the part does (e.g., Sword, Missile, Defense).
    [DOCUMENTED — S-2]
45. Skill = the proficiency category that powers the action. There are eight
    active skill categories: Strike, Berserk, Shoot, Aim Shot, Defend, Heal,
    Support, Interrupt. [DOCUMENTED — S-2][S-4]
46. Attribute = the compatibility category of the part (e.g., Grapple, Optic,
    Bomb). Attribute determines Medal compatibility bonuses. [DOCUMENTED — S-2]
47. Skill and Attribute are DIFFERENT concepts and must not be conflated.
    [DOCUMENTED — S-2]

### Action taxonomy

48. Actions are grouped by their primary Skill. The following taxonomy table
    lists all known base action types organized by Skill category.
    [DOCUMENTED — S-2][S-4]

## Action Taxonomy Table

| Skill | Canonical Name | Aliases | Description | Typical Use Case |
|-------|----------------|---------|-------------|------------------|
| Strike | Strike | — | Quick close-range attack | Melee damage |
| Berserk | Berserk | Reckless | Powerful close-range attack; user cannot evade normally during recovery | High melee damage with vulnerability |
| Shoot | Shoot | — | Normal ranged attack | Ranged damage |
| Aim Shot | Aim Shot | Snipe | Precision ranged attack; higher crit characteristics | High-accuracy ranged damage |
| Defend | Defend | Protect | Defensive action; reduces incoming damage | Damage mitigation |
| Heal | Heal | — | Restorative action; restores armor/HP | Recovery |
| Support | Support | — | Buff/acceleration/utility; enhances allies or battlefield | Team utility |
| Interrupt | Interrupt | Disrupt | Disruption/counterplay; disrupts opponent actions | Debuff/CC |

### Strike skill actions

| Action | Description | Source |
|--------|-------------|--------|
| Sword | Standard melee sword strike | [DOCUMENTED — S-2][S-4] |
| Destroy | Status-inflicting physical attack | [DOCUMENTED — S-2][S-4] |

### Berserk skill actions

| Action | Description | Source |
|--------|-------------|--------|
| Hammer | Powerful melee hammer strike | [DOCUMENTED — S-2][S-4] |
| Chain Reaction | Penetrating destructive attack | [DOCUMENTED — S-4] |

**Berserk formula note:** Effective Berserk Power = Part Power + (Propulsion / 2)
[DOCUMENTED — S-4]

### Shoot skill actions

| Action | Description | Source |
|--------|-------------|--------|
| Rifle | Standard ranged rifle shot | [DOCUMENTED — S-2][S-4] |
| Gatling / Chain Gun | Rapid-fire ranged attack | [DOCUMENTED — S-2][S-4] |
| Laser | Energy-based ranged attack | [DOCUMENTED — S-2][S-4] |
| Beam | Energy beam ranged attack | [DOCUMENTED — S-2][S-4] |
| Missile | Projectile ranged attack | [DOCUMENTED — S-2][S-4] |
| Napalm | Fire-based area attack | [DOCUMENTED — S-2][S-4] |
| Anti-Air | Ranged attack effective against Flying legs | [DOCUMENTED — S-3][S-4] |
| Anti-Sea | Ranged attack effective against Aquatic legs | [DOCUMENTED — S-3][S-4] |
| Sacrifice | Self-damage or team-benefit ranged action | [DOCUMENTED — S-4] |

### Aim Shot skill actions

| Action | Description | Source |
|--------|-------------|--------|
| Snipe | Precision high-crit ranged attack | [DOCUMENTED — S-2][S-4] |

**Aim Shot note:** The user's Medabot suffers a major evasion disadvantage during
recovery. Critical hits bypass normal defensive redirection.
[DOCUMENTED — S-4]

### Defend skill actions

| Action | Description | Source |
|--------|-------------|--------|
| Defense | Standard damage reduction | [DOCUMENTED — S-2][S-4] |
| Half Block | Partial damage reduction | [DOCUMENTED — S-4] |
| Full Block | Complete damage negation | [DOCUMENTED — S-4] |
| Counter | Retaliatory action on being hit | [DOCUMENTED — S-4] |
| Cross Attack setup | Prepares coordinated attack | [DOCUMENTED — S-4] |

**Defend note:** Defense actions can protect teammates and/or reduce incoming damage.
After using a melee action, the Medabot cannot normally activate Part Defense during
the recovery period until it performs an appropriate non-melee action.
[DOCUMENTED — S-4]

### Heal skill actions

| Action | Description | Source |
|--------|-------------|--------|
| Recovery | Restores armor/HP to target | [DOCUMENTED — S-2][S-4] |
| Repair | Fixes damaged parts | [DOCUMENTED — S-2][S-4] |
| Reactivate | Revives destroyed parts (temporary) | [DOCUMENTED — S-4] |
| AutoRecover | Passive/automatic recovery effect | [DOCUMENTED — S-4] |
| Status Clear | Removes status effects | [DOCUMENTED — S-4] |
| Trap Clear | Removes traps from the field | [DOCUMENTED — S-4] |

### Support skill actions

| Action | Description | Source |
|--------|-------------|--------|
| Scout | Reveals enemy information | [DOCUMENTED — S-2][S-4] |
| Conceal | Hides own Medabot from targeting | [DOCUMENTED — S-2][S-4] |
| Boost Charge | Reduces CRG time | [DOCUMENTED — S-4] |
| Rapid Charge | Greatly reduces CRG time | [DOCUMENTED — S-4] |

### Interrupt skill actions

| Action | Description | Source |
|--------|-------------|--------|
| Disable | Disables enemy part | [DOCUMENTED — S-2][S-4] |
| Confusion | Causes enemy to target randomly | [DOCUMENTED — S-2][S-4] |
| No Escape | Prevents enemy from retreating | [DOCUMENTED — S-4] |
| No Defense | Prevents enemy from using Defend | [DOCUMENTED — S-4] |
| Charge Drain | Reduces enemy Medaforce/Charge gauge | [DOCUMENTED — S-4] |
| Ammo Drain | Reduces enemy head Uses | [DOCUMENTED — S-4] |
| Force Drain | Reduces enemy action effectiveness | [DOCUMENTED — S-4] |
| Force Bind | Restricts enemy movement | [DOCUMENTED — S-4] |
| Pushover | Forces enemy position change | [DOCUMENTED — S-4] |
| Transform | Changes own or enemy form | [DOCUMENTED — S-4] |

### Attribute taxonomy (compatibility categories)

| Attribute | Description | Example Part | Source |
|-----------|-------------|--------------|--------|
| Grapple | Close-combat | Pipo Hammer | [DOCUMENTED — S-2][S-4] |
| Shoot | Ranged | — | [DOCUMENTED — S-2] |
| Optic | Vision/laser-based | — | [DOCUMENTED — S-2] |
| Bomb/Explosive | Explosive damage | — | [DOCUMENTED — S-2] |
| Gravity | Gravity manipulation | — | [DOCUMENTED — S-2] |
| Formation/Set-up | Positioning | — | [DOCUMENTED — S-2] |
| Movement/Flux | Mobility | — | [DOCUMENTED — S-2] |
| Stop | Stun/freeze | — | [DOCUMENTED — S-2] |
| Bind | Restriction | — | [DOCUMENTED — S-2] |
| Flow/Burn | Status effect | — | [DOCUMENTED — S-2] |
| Cancel/Release | Negation | — | [DOCUMENTED — S-2] |
| Defense | Protective | — | [DOCUMENTED — S-2] |
| Heal/Recovery | Restorative | — | [DOCUMENTED — S-2] |
| Anti-Air | Effective vs Flying | — | [DOCUMENTED — S-3] |
| Anti-Sea | Effective vs Aquatic | — | [DOCUMENTED — S-3] |
| Scan | Reconnaissance | — | [DOCUMENTED — S-2] |
| Conceal | Stealth | — | [DOCUMENTED — S-2] |
| Time | Temporal manipulation | — | [DOCUMENTED — S-2] |
| Interrupt/Disrupt | Disruption | — | [DOCUMENTED — S-2] |
| Destroy | Destruction | — | [DOCUMENTED — S-2] |
| Rebirth/Regenerate | Revival | — | [DOCUMENTED — S-2] |
| Teamwork/Link | Coordination | — | [DOCUMENTED — S-2] |
| Counter | Retaliation | — | [DOCUMENTED — S-2] |
| Transform | Morphing | — | [DOCUMENTED — S-2] |

## Known unknowns / Open questions

- Head part internal CRG/RAD: Do Head parts have internal Charge/Radiation values
  even though they are not displayed in-game? [UNKNOWN — needs ROM-level or
  disassembly verification]
- Success formula: Exact calculation of success rate incorporating ROS, Evasion,
  Defense, and random factors. [UNVERIFIED — T0.4 scope]
- Aim weighting algorithm: Exact formula for how Medal Target/Aim biases target
  selection among candidate parts. [UNKNOWN — needs in-game measurement or
  disassembly]
- Leg stat contributions: Exact numerical formulas for how Propulsion, Evasion,
  Defense, Proximity, Remoteness contribute to CRG/RAD time, damage, and success.
  [UNVERIFIED — T0.4 scope]
- Leg type x terrain matrix: Complete interaction table with bonus/penalty values.
  [UNKNOWN — T0.6 scope]
- Head Uses restoration: Whether Head Uses restore mid-battle (e.g., via Heal actions)
  or only between battles. [UNKNOWN]
- Berserk vulnerability details: Exact evasion/defense penalty values during recovery.
  [HYPOTHESIS — S-7]

## Verification plan

1. Cross-check part statistics against Medarot 1 disassembly (S-6) — justified
   by the claim that the battle system is "mostly unchanged since Medarot 1" (S-1),
   but every mismatch must be recorded as a 2 CORE vs Medarot 1 difference.
2. In-game observation of Head Uses: verify whether head actions are consumed
   and whether they restore mid-battle or only between battles.
3. In-game observation of Aim targeting: record target selection patterns across
   different Medal Target/Aim values to infer the weighting algorithm.
4. Manual timing tests: measure CRG/RAD times for known parts on known terrain
   to verify Propulsion's contribution.
5. Damage measurement: record damage values for Berserk actions with different
   Propulsion values to verify the formula: Effective Power = Power + (Propulsion / 2).

## Derived test oracles

- Part composition: a Medabot cannot be constructed with fewer than 4 parts;
  a Medabot with all 4 parts can enter battle.
- Head Uses: a Head with Uses=3 can invoke its action exactly 3 times in a
  Robattle, then becomes unusable for that battle.
- Arm infinite uses: an arm's action can be invoked any number of times
  (limited only by CRG/RAD timing).
- Berserk formula: a Berserk action with Part Power=100 and Propulsion=50
  deals base damage of 125 (100 + 50/2).
- Aim Shot vulnerability: a Medabot that used Aim Shot takes increased damage
  from the next incoming attack during its RAD phase.
- Defend restriction: after using a melee action, a Medabot cannot use Defend
  until it has used a non-melee action or returned to the command line.
