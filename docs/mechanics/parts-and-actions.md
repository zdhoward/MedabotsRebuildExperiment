# Spec: Parts & Actions

Status: DRAFT
Task: T0.3

Scope: Medarot 2 CORE (GBA; English releases "Medabots: Metabee" / "Medabots:
Rokusho"). This spec covers part categories (head, arms, legs), part statistics,
action taxonomy, and the success/aim (ROS) mechanics. Damage formulas, success
rolls, and crit mechanics are T0.4 scope. Terrain/leg interactions are T0.6.

## Summary

A Medarot is composed of four parts: **Head**, **Right Arm**, **Left Arm**, and **Legs**,
each with distinct statistics and roles [S-A][S-B]. Heads and arms share a common
stat block and perform **actions** (attacks, support, defense) while legs govern
movement, terrain interaction, and defensive posture [S-A][S-C].

There are **11 skill types** that categorize actions and determine which Medal
skill levels they draw from [S-A]. Actions are categorized into families:
melee (Strike, Berserk/Reckless), ranged (Shoot, Snipe/Aim Shot), defense (Protect/Defend),
healing (Heal), support (Support, Scan, Conceal), disruption (Disrupt/Interrupt,
traps, status), and special/other (Special, Transform, Medaforce) [S-A][S-C].

Head parts have **finite Uses** per battle; arm parts have **infinite uses** [S-A][S-C].
Every action has a **Success** stat (also called ROS — Rate of Success) that affects
accuracy and critical hit likelihood [S-A][S-D HYPOTHESIS].

## Sources

- [x] [S-A] Medapedia, "Stats" — https://medarot.meowcorp.us/wiki/Stats —
  verified live 2026-09-24: master reference for Medal stats and part stats including
  the 11 skill list (Strike, Reckless/Berserk, Shoot, Snipe/Aim Shot, Protect/Defend,
  Heal, Support, Disrupt/Interrupt, Set-up, Special, Other) and head/arm/leg stat
  definitions (Action, Skill, Armor, Power, Success, Charge, Cooldown/Uses, etc.).
- [x] [S-B] Medapedia, "Parts" — https://medarot.meowcorp.us/wiki/Parts —
  verified live 2026-09-24: parts overview, 4-part composition, destruction behavior.
- [x] [S-C] Medapedia, "User:Kimbles/Medarot 1 Hacking Notes" —
  https://medarot.meowcorp.us/wiki/User:Kimbles/Medarot_1_Hacking_Notes —
  verified live 2026-09-24: per-part byte layout for head/arm (Attribute, Action,
  Armor, Skill, Success, Power, Pierce, Uses/Charge, Cooldown, flags, animation,
  effect flags) and legs (Attribute, Leg type, Armor, Speed, Mobility, Fighting,
  Shooting, Scan, Conceal, anti-type flags); **60-action list** with hex codes,
  descriptions, and action categories; skill mapping (01-0F) covering Strike,
  Berserk, Shoot, Snipe, Support, Protect, Heal, Disrupt, Set-up, Other.
- [ ] [S-D] tiomasta, GameFAQs thread "Explanation of game stats/mechanics here" —
  https://gamefaqs.gamespot.com/boards/915188-medabots-metabee/79284943 —
  HYPOTHESIS-grade: claims about crit determinism, ROS vs evasion+defense interaction.
  Not directly referenced here except where marked; see T0.4.
- [ ] [S-E] GameFAQs guides (Kenshin_Xtreme, Autocon) — blocked by 403 for automated
  fetch; secondary corroboration for skill lists and action categories cited via
  S-A and S-C where possible.
- [ ] [S-F] Medarot 1 disassembly (github.com/Medabots/medarot1) — read-only
  oracle; the battle system is "mostly unchanged since Medarot 1" per S-A, so Medarot 1
  part data layout and action list are valid cross-checks for 2 CORE. Not yet
  consulted directly for this spec.

**Note on Medarot 1 vs 2 CORE:** Medapedia states the battle system "has remained
mostly unchanged since Medarot 1" [S-A]. We rely on this to use Kimbles' Medarot 1
notes [S-C] and the medarot1 disassembly [S-F] as oracles for part/action mechanics.
Any discovered 2 CORE vs Medarot 1 differences will be recorded explicitly.

## Part Categories and Roles

### Part composition

1. A battle-ready Medarot requires exactly **4 parts**: Head + Right Arm + Left Arm + Legs. [DOCUMENTED — S-B]
2. IF any part's Armor reaches 0 THEN that part is destroyed and unusable for the rest of the battle. [DOCUMENTED — S-B, battle-flow T0.2 rule 20]
3. Destroyed parts are restored automatically after the battle. [DOCUMENTED — S-B]

### Head parts

4. Head parts perform **actions** selected from the command menu. [DOCUMENTED — S-B]
5. Head parts have **finite Uses** per battle (byte H in Kimbles layout). Once exhausted, the head cannot be used again that battle. [DOCUMENTED — S-C]
6. Head parts share the same stat schema as Arm parts (Attribute, Action, Skill, Armor, Power, Success, Charge, Cooldown, Pierce, Uses, effect flags). [DOCUMENTED — S-C]

### Arm parts (Right and Left)

7. Arm parts perform **actions** and have **infinite uses** (Charge byte H is used for charge value, not uses; uses = infinite for arms). [DOCUMENTED — S-C, inferred from S-A]
8. Right Arm and Left Arm are mechanically identical in stat structure; the distinction is positional only. [DOCUMENTED — S-C]

### Leg parts

9. Leg parts determine **movement speed**, **terrain bonuses/penalties**, and **defensive posture**. [DOCUMENTED — S-A]
10. Leg parts have a **Leg type** that interacts with terrain (7 types: Bipedal, Multi-leg, Wheeled, Tank, Hover/Float, Flying, Aquatic). [DOCUMENTED — S-A leg type page reference]
11. Leg parts do NOT perform actions; they provide passive stats only. [DOCUMENTED — S-A, S-B]

## Part Statistics

### Head and Arm part stats

| Stat | Japanese | Description | Scope |
|------|----------|-------------|-------|
| Attribute | 属性 | Category for Medal compatibility | All head/arm parts [DOCUMENTED — S-A, S-C] |
| Action | 行動/わざ | The attack/ability performed | All head/arm parts [DOCUMENTED — S-A, S-C] |
| Skill | スキル | Determines which Medal skill level is used | All head/arm parts [DOCUMENTED — S-A, S-C] |
| Armor | 装甲 | HP; part destroyed at 0 | All parts [DOCUMENTED — S-A, S-B] |
| Power | 威力 | Attack power or effect strength | Attacking head/arm parts [DOCUMENTED — S-A, S-C] |
| Success | 成功 | Rate of Success (ROS); accuracy and/or crit likelihood | All head/arm parts [DOCUMENTED — S-A, S-C] |
| Charge | 充填 | Wait time: command line → active line | All head/arm parts [DOCUMENTED — S-A, S-C] |
| Cooldown | 冷却 | Wait time: active line → command line (Radiation) | Arm parts only; 00 for heads [DOCUMENTED — S-C] |
| Uses | 回数 | Number of uses per battle | Head parts only; 00 for arms means infinite [DOCUMENTED — S-C] |
| Pierce | 貫通 | Whether effect chains to additional parts | Some attacking parts [DOCUMENTED — S-C] |

**Byte layout for head/arm parts (Medarot 1, 16 bytes each):** [DOCUMENTED — S-C]
```
Offset  Stat        Size  Notes
------  ----        ----  -----
0x00    Attribute   1     00-1B (28 values; some special medals only)
0x01    Action      1     00-37 (60 possible values; see Action list)
0x02    Armor       1     00-FF (0-255)
0x03    Skill       1     01-0F (maps to 11 skills; see Skill mapping)
0x04    Success     1     00-63 (0-99)
0x05    Power       1     00-FF (0-255)
0x06    Pierce      1     00 = no, 0B = yes
0x07    Uses/Charge 1     Heads: uses count; Arms: charge value
0x08    Cooldown    1     Heads: always 00; Arms: cooldown value
0x09    Flag A      1     00 or 01 (Attack category?)
0x0A    Flag D      1     00 or 01 (Defense category?)
0x0B    Flag S      1     00 or 01 (Special category?)
0x0C    Animation   1     00-16 (battle animation ID)
0x0D    Effect N    1     Preferred target effect flag
0x0E    Effect O    1     Own effect flag marker
0x0F    Attack Name 1     00-12 (in-battle attack name ID; 00 for non-attacking)
```

### Leg part stats

| Stat | Japanese | Description | Scope |
|------|----------|-------------|-------|
| Attribute | 属性 | Category for Medal compatibility | All leg parts [DOCUMENTED — S-A, S-C] |
| Leg type | - | 7 types affecting terrain interaction | All leg parts [DOCUMENTED — S-A, S-C] |
| Armor | 装甲 | HP; part destroyed at 0 | All leg parts [DOCUMENTED — S-A] |
| Speed | 推進 | Propulsion; movement speed | All leg parts [DOCUMENTED — S-A, S-C] |
| Mobility | 起動 | Evasion; dodge capability | All leg parts [DOCUMENTED — S-A, S-C] |
| Defense | 防御 | Damage reduction | All leg parts [DOCUMENTED — S-A, S-C] |
| Melee | 格闘 | Proximity; close-range attack power | All leg parts [DOCUMENTED — S-A, S-C] |
| Shooting | 射撃 | Remoteness; ranged attack power | All leg parts [DOCUMENTED — S-A, S-C] |
| Scan | さくてき | Scan effectiveness | Some leg parts [DOCUMENTED — S-C] |
| Conceal | いんぺい | Conceal effectiveness | Some leg parts [DOCUMENTED — S-C] |

**Byte layout for leg parts (Medarot 1, 16 bytes each):** [DOCUMENTED — S-C]
```
Offset  Stat        Size  Notes
------  ----        ----  -----
0x00    Attribute   1     Same as head/arm
0x01    Leg type    1     3D = Flying, 43 = Water/Aquatic (7 types total)
0x02    Armor       1     00-FF
0x03    Speed       1     00-FF
0x04    Mobility    1     00-FF
0x05    Fighting    1     00-FF (Melee/Proximity)
0x06    Shooting    1     00-FF (Shooting/Remoteness)
0x07    Scan        1     00-FF
0x08    Conceal     1     00-FF (hidden in Medarot 1 stat screen)
0x09    -           1     Always 00
0x0A    -           1     Always 00
0x0B    -           1     Always 00
0x0C    -           1     Always 00
0x0D    Anti-type N 1     Non-zero for Flying/Aquatic (Anti-Air/Anti-Sea)
0x0E    Anti-type O 1     Non-zero for Flying/Aquatic
0x0F    -           1     Always 00
```

## Skill Types (11 total)

The 11 skills are the categorization system for actions and Medal proficiencies.
Each action belongs to exactly one skill type, which determines which Medal
skill level it uses [DOCUMENTED — S-A].

From Kimbles' Medarot 1 hacking notes, skill byte D maps as follows: [DOCUMENTED — S-C]

| Hex | Skill | Japanese | English (Metabee/Rokusho) | Notes |
|-----|-------|----------|----------------------------|-------|
| 01 | Strike | なぐる | Strike | Melee attack [DOCUMENTED — S-A, S-C] |
| 02 | Berserk | がむしゃら | Reckless | Melee attack, unused in Medarot 1 per S-C [DOCUMENTED — S-C] |
| 03 | Strike | (unused) | Strike | Unused variant [DOCUMENTED — S-C] |
| 04 | Berserk | がむしゃら | Reckless | Melee attack [DOCUMENTED — S-C] |
| 05 | Shoot | うつ | Shoot | Ranged attack [DOCUMENTED — S-A, S-C] |
| 06 | Snipe | ねらいうち | Aim Shot | Ranged attack [DOCUMENTED — S-A, S-C] |
| 07 | Support | ouille | Support | Speed-up effects [DOCUMENTED — S-C] |
| 08 | Protect | まもる/えんご | Defend | Defensive [DOCUMENTED — S-C] |
| 09 | Protect | (traps) | Defend | Trap-related protect [DOCUMENTED — S-C] |
| 0A | Heal | なおす/かいふく | Heal | Recovery/status [DOCUMENTED — S-C] |
| 0B | Heal | (recovery) | Heal | Recovery variant [DOCUMENTED — S-C] |
| 0C | Support | (scan) | Support | Scan support [DOCUMENTED — S-C] |
| 0D | Support | (conceal) | Support | Conceal support [DOCUMENTED — S-C] |
| 0E | Other | とくしゅ | Special | Transform [DOCUMENTED — S-C] |
| 0F | Other | そのほか | Other | Negate [DOCUMENTED — S-C] |

**Canonical English terms for Medarot 2 CORE:** [DOCUMENTED — S-A]
- Berserk = Reckless
- Snipe = Aim Shot
- Protect = Defend
- Disrupt = Interrupt
- Set-up = Set-up

## Action Taxonomy

Actions are categorized by their **Skill** and their **behavioral family**. The
following table presents all documented action types for Medarot 2 CORE, based on
the Medarot 1 action list [S-C] which is justified for use by S-A's claim that the
battle system is mostly unchanged.

**Action types are marked with their relationship to Medarot 2 CORE:**
- **[DOCUMENTED]** — confirmed present in Medarot 1 data and/or referenced by S-A
- **[INFERRED]** — present in Medarot 1, expected in 2 CORE by continuity
- **[UNVERIFIED]** — existence in 2 CORE not confirmed by any source

### Offensive Actions

| Action | Hex | Skill | Family | Description | 2 CORE Status |
|--------|-----|-------|--------|-------------|----------------|
| Sword | 00 | Strike | Melee | Simple melee strike | DOCUMENTED [S-C] |
| Hammer | 00 | Strike | Melee | Heavy melee strike | DOCUMENTED [S-C] |
| Gatling | 01 | Shoot | Ranged | Rapid-fire gun | DOCUMENTED [S-C] |
| Laser | 02 | Shoot | Ranged | High-power beam | DOCUMENTED [S-C] |
| Beam | 03 | Shoot | Ranged | Standard beam | DOCUMENTED [S-C] |
| Missile | 04 | Shoot | Ranged | Explosive projectile | DOCUMENTED [S-C] |
| Napalm | 05 | Shoot | Ranged | Fire-based attack | DOCUMENTED [S-C] |
| Break | 06 | Shoot | Ranged | High damage, defense-piercing | DOCUMENTED [S-C] |
| Press | 07 | Shoot | Ranged | Crushing attack | DOCUMENTED [S-C] |
| Rifle | 00 | Shoot | Ranged | Standard rifle shot | DOCUMENTED [S-C] |
| Ghost | 00 | Other | Special | Spectral attack | DOCUMENTED [S-C] |

### Melee Actions

| Action | Hex | Skill | Family | Description | 2 CORE Status |
|--------|-----|-------|--------|-------------|----------------|
| Strike | - | Strike | Melee | Standard melee | DOCUMENTED [S-A] |
| Berserk/Reckless | - | Berserk | Melee | High-power melee with tradeoff | DOCUMENTED [S-A] |

### Support Actions

| Action | Hex | Skill | Family | Description | 2 CORE Status |
|--------|-----|-------|--------|-------------|----------------|
| Boost Charge | 2D | Support | Support | Increases movement speed | DOCUMENTED [S-C] |
| Instant Charge | 2E | Support | Support | Zero preparation time | DOCUMENTED [S-C] |
| Scan | 28 | Support | Support | Makes attacks more likely to hit | DOCUMENTED [S-C] |
| Conceal | 29 | Support | Support | Makes attacks more likely to dodge | DOCUMENTED [S-C] |
| Scan Clear | 2A | Support | Support | Removes all scan bonuses | DOCUMENTED [S-C] |

### Defensive Actions

| Action | Hex | Skill | Family | Description | 2 CORE Status |
|--------|-----|-------|--------|-------------|----------------|
| Protect/Defend | 1C | Protect | Defense | Protects ally Medarot | DOCUMENTED [S-C] |
| Perfect Defense | 1D | Protect | Defense | Completely blocks attacks | DOCUMENTED [S-C] |
| Lesser Defense | 1E | Protect | Defense | Completely blocks weak attacks | DOCUMENTED [S-C] |

### Healing Actions

| Action | Hex | Skill | Family | Description | 2 CORE Status |
|--------|-----|-------|--------|-------------|----------------|
| Heal | - | Heal | Healing | Restores HP to parts | DOCUMENTED [S-A] |
| Repair | 20 | Heal | Healing | Repairs damaged parts | DOCUMENTED [S-C] |
| Revive | 22 | Heal | Healing | Restores destroyed parts | DOCUMENTED [S-C] |

### Disruption/Status Actions

| Action | Hex | Skill | Family | Description | 2 CORE Status |
|--------|-----|-------|--------|-------------|----------------|
| Fighting Trap | 08 | Protect | Disrupt | Damages Strike/Berserk users | DOCUMENTED [S-C] |
| Shooting Trap | 09 | Protect | Disrupt | Damages Shoot/Snipe users | DOCUMENTED [S-C] |
| Bug | 0A | Disrupt | Disrupt | Lowers action success rate | DOCUMENTED [S-C] |
| Virus | 0B | Disrupt | Disrupt | Status effect | DOCUMENTED [S-C] |
| Thunder | 0C | Disrupt | Disrupt | Stops enemy movement | DOCUMENTED [S-C] |
| Freeze | 0D | Disrupt | Disrupt | Freezes enemy | DOCUMENTED [S-C] |
| Hold | 0E | Disrupt | Disrupt | Slows enemy movement | DOCUMENTED [S-C] |
| Wave | 0F | Disrupt | Disrupt | Wave-based effect | DOCUMENTED [S-C] |
| Fire | 10 | Disrupt | Disrupt | Damage during movement | DOCUMENTED [S-C] |
| Melt | 11 | Disrupt | Disrupt | Melting effect | DOCUMENTED [S-C] |

### Cancel Actions

| Action | Hex | Skill | Family | Description | 2 CORE Status |
|--------|-----|-------|--------|-------------|----------------|
| Trap Cancel | 12 | - | Disrupt | Negates Trap effects | DOCUMENTED [S-C] |
| Flux Cancel | 13 | - | Disrupt | Negates Bug/Virus | DOCUMENTED [S-C] |
| Stop Cancel | 14 | - | Disrupt | Negates Thunder/Freeze | DOCUMENTED [S-C] |
| Bind Cancel | 15 | - | Disrupt | Negates Hold/Wave | DOCUMENTED [S-C] |
| Burn Cancel | 16 | - | Disrupt | Negates Melt/Fire | DOCUMENTED [S-C] |
| Status Cancel | 17 | - | Disrupt | Negates all status | DOCUMENTED [S-C] |

### Negate Actions

| Action | Hex | Skill | Family | Description | 2 CORE Status |
|--------|-----|-------|--------|-------------|----------------|
| Negate Optical | 18 | - | Disrupt | Blocks Laser/Beam | DOCUMENTED [S-C] |
| Negate Gunpowder | 19 | - | Disrupt | Blocks Missile/Napalm | DOCUMENTED [S-C] |
| Negate Gravity | 1A | - | Disrupt | Blocks Break/Press | DOCUMENTED [S-C] |
| Negate All | 1B | - | Disrupt | Blocks all special attacks (unused in Medarot 1) | UNVERIFIED [S-C] |

### Special Actions

| Action | Hex | Skill | Family | Description | 2 CORE Status |
|--------|-----|-------|--------|-------------|----------------|
| Anti-Air | 23 | - | Special | Strong vs Flying legs | DOCUMENTED [S-C] |
| Anti-Sea | 26 | - | Special | Strong vs Aquatic legs | DOCUMENTED [S-C] |
| Transform | 37 | Other | Special | Transforms into another part | DOCUMENTED [S-C] |

### Medaforce Actions

Medaforce actions are special abilities tied to Medals, not parts. They consume
the Medaforce gauge. The specific Medaforces available depend on the Medal.
[DOCUMENTED — S-A]

## Success / Aim (ROS) Mechanics

1. Every head and arm part has a **Success** stat (0-99) representing Rate of Success (ROS). [DOCUMENTED — S-A, S-C]
2. Higher Success values make actions more accurate and/or more likely to land critical hits. [HYPOTHESIS — S-D; exact formula UNVERIFIED]
3. The **Aim** (Target) stat on Medals biases which enemy parts are selected as targets. [DOCUMENTED — S-A]
4. Melee actions (Strike, Berserk/Reckless) do NOT use pre-selected targets; they hit the enemy closest to the active line at execution time. [DOCUMENTED — S-A, battle-flow T0.2 rule 15]
5. Ranged actions (Shoot, Snipe/Aim Shot, and most support/disruption actions) DO use pre-selected targets chosen before the command is issued. [DOCUMENTED — S-A, battle-flow T0.2 rule 8]
6. IF a ranged action's pre-selected target is destroyed or shut down at execution time THEN the action fails (GB-era behavior, per Medapedia). [DOCUMENTED — S-A, battle-flow T0.2 rule 14]

**Target/Aim weighting algorithm:** UNVERIFIED (no source publishes the exact scoring; see Known unknowns). [UNKNOWN]

## Part Categories by Behavior

### Head (Finite Uses)
- Can be used a limited number of times per battle (Uses stat)
- Each use consumes one count; at 0 uses, the head cannot be selected
- After uses are exhausted, the Medabot must use arm parts or Medaforce
- Typical actions: High-power attacks, special abilities

### Arms (Infinite Uses)
- Right Arm and Left Arm can be used indefinitely
- No uses counter; only limited by Charge/Cooldown timing
- Typical actions: Standard attacks (Shoot, Strike), support, defense

### Legs (Passive)
- Do not perform actions
- Provide movement stats (Speed, Mobility)
- Provide terrain interaction via Leg type
- Provide defensive stats (Defense, Melee, Shooting)
- Provide situational bonuses (Scan, Conceal)

## Rules (pseudocode)

### Part composition and destruction
1. A Medarot = Head + Right Arm + Left Arm + Legs. [DOCUMENTED — S-B]
2. IF Head.Armor == 0 AND Medarot is Leader THEN battle ends immediately. [DOCUMENTED — battle-flow T0.2 rule 22]
3. IF Head.Armor == 0 AND Medarot is Partner THEN Medarot stops functioning. [DOCUMENTED — battle-flow T0.2 rule 21]
4. IF any Part.Armor == 0 THEN that part is destroyed for the rest of the battle. [DOCUMENTED — S-B]

### Head usage
5. Head.Uses starts at the part's Uses value at battle start. [DOCUMENTED — S-C]
6. ON Head action executed: Head.Uses -= 1. [DOCUMENTED — S-C]
7. IF Head.Uses == 0 THEN Head cannot be selected from command menu. [DOCUMENTED — S-C]
8. Head.Uses resets after battle. [DOCUMENTED — S-B (parts restored)]

### Arm usage
9. Arm.Uses is infinite (no Uses stat; Charge byte is charge time, not uses). [DOCUMENTED — S-C]
10. Arm parts can be selected any number of times, limited only by Charge/Cooldown. [DOCUMENTED — S-C]

### Action categories
11. Melee actions: Strike, Berserk/Reckless. [DOCUMENTED — S-A, S-C]
12. Ranged actions: Shoot, Snipe/Aim Shot. [DOCUMENTED — S-A, S-C]
13. Defense actions: Protect/Defend, Perfect Defense, Lesser Defense. [DOCUMENTED — S-C]
14. Support actions: Support (speed-up), Boost Charge, Instant Charge, Scan, Conceal, Scan Clear. [DOCUMENTED — S-C]
15. Healing actions: Heal, Repair, Revive. [DOCUMENTED — S-A, S-C]
16. Disruption actions: Fighting Trap, Shooting Trap, Bug, Virus, Thunder, Freeze, Hold, Wave, Fire, Melt. [DOCUMENTED — S-C]
17. Cancel actions: Trap Cancel, Flux Cancel, Stop Cancel, Bind Cancel, Burn Cancel, Status Cancel. [DOCUMENTED — S-C]
18. Negate actions: Negate Optical, Negate Gunpowder, Negate Gravity. [DOCUMENTED — S-C]
19. Special actions: Anti-Air, Anti-Sea, Transform. [DOCUMENTED — S-C]

### Skill system
20. Each action belongs to exactly one Skill type. [DOCUMENTED — S-A, S-C]
21. The Medarot's Medal has skill levels for each Skill type. [DOCUMENTED — S-A]
22. When an action is used, its Success is modified by the Medal's corresponding Skill level. [DOCUMENTED — S-A]
23. Higher Skill level = higher accuracy, faster charge, or more power for actions of that Skill. [DOCUMENTED — S-A]

### Leg stats
24. Leg.Speed affects movement speed toward/away from active line. [DOCUMENTED — S-A, S-C]
25. Leg.Mobility affects evasion capability. [DOCUMENTED — S-A, S-C]
26. Leg.Defense affects damage reduction. [DOCUMENTED — S-A, S-C]
27. Leg.Melee (Proximity) boosts close-range attack power. [DOCUMENTED — S-A, S-C]
28. Leg.Shooting (Remoteness) boosts ranged attack power. [DOCUMENTED — S-A, S-C]
29. Leg.Scan and Leg.Conceal affect Scan/Conceal action effectiveness. [DOCUMENTED — S-C]

### Anti-type interactions
30. Anti-Air actions/parts deal bonus damage or effects to Flying leg types. [DOCUMENTED — S-C]
31. Anti-Sea actions/parts deal bonus damage or effects to Aquatic leg types. [DOCUMENTED — S-C]
32. Flying leg parts have non-zero values at offsets 0x0D and 0x0E (Anti-Air targets). [DOCUMENTED — S-C]
33. Aquatic leg parts have non-zero values at offsets 0x0D and 0x0E (Anti-Sea targets). [DOCUMENTED — S-C]

## Known unknowns / Open questions

- **2 CORE action list:** Medapedia's "Actions in Medarot 2 CORE" page is EMPTY [BACKLOG 2026-09-23]. The action taxonomy above is based on Medarot 1 data [S-C]. We need in-game or disassembly verification that all these actions exist in 2 CORE with the same hex codes. [UNKNOWN]
- **Action count:** The owner report claims a "60-action list" but its cited Medapedia sources are empty. Kimbles documents ~40 distinct actions (hex 00-37 with gaps). The exact number of actions in 2 CORE is UNVERIFIED. [UNKNOWN]
- **Head vs Arm Charge/Cooldown:** Medarot 1 heads use byte H for Uses and byte I is always 00; arms use H for Charge and I for Cooldown. Does 2 CORE use the same layout? UNVERIFIED. [UNKNOWN]
- **Success formula:** How exactly Success (ROS) combines with evasion, defense, and Medal skill levels to determine hit/miss and crit. tiomasta claims deterministic crits based on ROS vs evasion+defense, but methodology not stated. [HYPOTHESIS — S-D; T0.4 scope]
- **Aim/Target weighting:** No source publishes how the Medal's Aim stat scores candidate targets. [UNKNOWN — battle-flow T0.2 rule 10]
- **Skill byte mapping for 2 CORE:** Kimbles' Medarot 1 mapping shows some duplicates (Strike at 01 and 03; Berserk at 02 and 04; Heal at 0A and 0B; Protect at 08 and 09; Support at 07, 0C, 0D). Is this also true for 2 CORE, or is the mapping cleaner? UNVERIFIED. [UNKNOWN]
- **Pierce effect mechanics:** Byte G = 0B means pierce; what does this mean exactly? Does it chain to adjacent parts? Pierces defense? Exact behavior UNVERIFIED. [UNKNOWN]
- **Category flags (J, K, L):** Medarot 1 uses bytes J/K/L as Attack/Defense/Special category flags. Do these affect gameplay in 2 CORE? UNVERIFIED. [UNKNOWN]
- **Effect flags (N, O):** Bytes N and O on head/arm parts mark effect preferences for targeting. How exactly do they interact with Aim? UNVERIFIED. [UNKNOWN]
- **Leg type terrain matrix:** The 7 leg types × terrain types interaction matrix is T0.6 scope, not documented here. [OUT OF SCOPE]

## Verification plan

1. **Cross-check against Medarot 1 disassembly** [S-F]: Verify that part data structures match Kimbles' notes by reading the medarot1 disassembly source. This establishes the byte layout as ground truth for Medarot 1; then rely on S-A's continuity claim for 2 CORE.
2. **Find 2 CORE-specific sources:** Search for "Actions in Medarot 2 CORE" page content (archived?), or equivalent in Japanese sources. The Medarot 2 Core Japanese wiki may have this data.
3. **In-game observation:** Once Phase 1 engine can run seeded battles, test that:
   - Head uses decrement correctly and cannot be used at 0
   - Arm parts have no uses limit
   - Melee actions hit closest enemy
   - Ranged actions fail if pre-selected target is destroyed
   - Each action belongs to the expected Skill type
4. **Disassembly cross-check:** When T0.7 or later touches disassembly, verify the action list and part stats for 2 CORE specifically, recording any differences from Medarot 1.

## Derived test oracles

- Head uses: A head with Uses=3 can be used exactly 3 times in a battle, then becomes unselectable (rule 7).
- Arm infinite uses: An arm can be used any number of times, limited only by timing (rule 10).
- Melee targeting: With enemies at distances 10, 20, 30 from active line, a Strike action hits the enemy at distance 10 (closest) (battle-flow rule 15).
- Ranged targeting: A ranged action against a specific target succeeds if that target is alive at execution time (battle-flow rule 8, 14).
- Action-skill mapping: A Shoot action uses the Medal's Shoot skill level, not Strike or Snipe (rule 22).
- Anti-Air bonus: An Anti-Air action against a Flying-leg Medarot deals bonus damage/effect (rule 30).
- Part destruction: When a part's armor reaches 0, it is destroyed and unusable for the rest of the battle (rule 4).
