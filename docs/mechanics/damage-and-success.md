# Spec: Damage & Success Formulas

Status: DRAFT
Task: T0.4

Scope: Medarot 2 CORE (GBA; English releases "Medabots: Metabee" / "Medabots:
Rokusho"). This spec covers damage calculation, success rate (ROS) mechanics,
critical hit determination, and the interaction of part stats with Medal
skill levels during action resolution. Terrain/leg interactions are T0.6
scope. Battle flow context is in T0.2; parts/actions in T0.3.

## Summary

Damage in Medarot 2 CORE is computed from the attacking part's **Power**, the
defending part's **Armor**, and modifiers from **Success** (ROS), **Evasion**,
**Defense**, and **Medal skill levels** [S-A][S-B HYPOTHESIS]. Community testing
suggests a deterministic crit system based on ROS vs (Evasion + Defense), with
stat-based scaling factors applied to damage [S-B]. Each stat's contribution
has a proposed formula with testable predictions, but only disassembly or
controlled in-game measurement can confirm them for 2 CORE.

The **Rate of Success** (ROS/Success) stat on parts appears to serve dual roles:
accuracy (hit/miss) and critical hit chance, while **Evasion** and **Defense**
stats on legs provide damage reduction [S-B HYPOTHESIS]. Medal skill levels
scale the effective Power or Success of matching actions [S-A].

## Sources

- [x] [S-A] Medapedia, "Stats" — https://medarot.meowcorp.us/wiki/Stats —
  verified live 2026-09-24: master stat reference; defines part stats including
  Success (ROS), Power, Armor, Evasion, Defense; lists Medal stats including
  skill levels (0-100). Confirms stat existence, not formulas.
- [ ] [S-B] tiomasta, GameFAQs thread "Explanation of game stats/mechanics here" —
  https://gamefaqs.gamespot.com/boards/915188-medabots-metabee/79284943 —
  HYPOTHESIS-grade: empirical claims about deterministic crits (ROS vs
  Evasion+Defense), Evasion/Defense subtract 25% of their value from damage,
  ROS adds 25% of itself as bonus damage, recovery-turn attack-type weaknesses.
  Methodology not stated; needs cross-check against disassembly or in-game
  verification. Primary source for formulas in this spec.
- [ ] [S-C] Medarot 1 disassembly (github.com/Medabots/medarot1) — read-only
  oracle; battle system "mostly unchanged since Medarot 1" per S-A, so Medarot 1
  damage routines are valid cross-checks for 2 CORE. Not yet consulted for
  this spec — marked as future verification target.
- [ ] [S-D] Kenshin_Xtreme, "Medabots RPG Walkthrough (v3.50, 2004)" —
  https://gamefaqs.gamespot.com/gba/915188-medabots-metabee/faqs/24031 —
  secondary source; may corroborate or conflict with S-B claims; link blocked
  by 403 for automated fetch, verified manually in T0.1.
- [ ] [S-E] Autocon, "Medabots: Rokusho Guide and Walkthrough (v1.3, 2015)" —
  https://gamefaqs.gamespot.com/gba/915189-medabots-rokusho/faqs/35357 —
  verified live 2026-09-23 (T0.2): documents battle mechanics but does not
  specify damage formulas; useful for behavioral context.

**Note on source reliability:** S-B (tiomasta) is the only source publishing
actual damage/success formulas for the GBA games. Because methodology is not
stated, all formulas from S-B are marked **HYPOTHESIS**. S-A (Medapedia) is
authoritative for stat definitions but not formulas. Disassembly cross-check
(S-C) is the only path to **VERIFIED** status.

## Stat Definitions (relevant subset)

| Stat | Type | Range | Role in damage/success |
|------|------|-------|----------------------|
| Power | Head/Arm | 0-255 | Base damage output [DOCUMENTED — S-A] |
| Armor | All parts | 0-255 | HP; damage absorbs Armor, part destroyed at 0 [DOCUMENTED — S-A, S-B (battle-flow)] |
| Success | Head/Arm | 0-99 | Rate of Success; accuracy and crit chance [DOCUMENTED — S-A] |
| Evasion | Legs | 0-255 | Reduces incoming damage or hit chance [DOCUMENTED — S-A (stat exists); effect HYPOTHESIS — S-B] |
| Defense | Legs | 0-255 | Reduces incoming damage [DOCUMENTED — S-A (stat exists); effect HYPOTHESIS — S-B] |
| Skill | Head/Arm | 0-15 | Maps to Medal skill type; determines which Medal skill level applies [DOCUMENTED — S-A, parts-and-actions T0.3] |
| Skill Level | Medal | 0-100 | Modifies effective Power or Success for matching actions [DOCUMENTED — S-A] |

**Medal stat interaction:** When a part action is used, its **Skill** byte
selects which Medal **Skill Level** is applied to the action's calculation.
For example, a Shoot action (Skill=05 hex) on a part uses the Medal's Shoot
skill level [DOCUMENTED — S-A, parts-and-actions T0.3 rule 22].

## Formulas

### F1: Base Damage Formula

**Claim:** Raw damage from an attacking part before any reduction.

```
BaseDamage = Power + (Power * (SkillLevel / 100)) + (Success * 0.25)  [HYPOTHESIS — S-B]
```

**Provenance:** tiomasta states "ROS adds 25% of itself as bonus damage". 
The Skill Level scaling is implied by S-A's description that higher skill
levels provide "more power", but the exact multiplicative factor is from
community interpretation, not a cited source.

**Interpretation:** The Success stat contributes 25% of its value directly to
damage output. Medal Skill Level scales Power by its percentage (e.g., skill
level 50 = +50% Power).

**Test to verify:**
- Equip a head with Power=100, Success=0, Skill=Shoot, on a Medal with Shoot
  skill level 0. Measure damage against a 0-Armor target. Expected: 100.
- Same head, Medal Shoot skill level 100. Expected: 200.
- Same head with Success=40. Expected: 100 + 10 = 110 (with skill 0) or 200 +
  10 = 210 (with skill 100).
- Use seeded engine replay (Phase 1) to confirm deterministic output.

**Status:** HYPOTHESIS — needs disassembly (S-C) or in-game verification.

---

### F2: Damage Reduction Formula (Evasion and Defense)

**Claim:** Each point of Evasion and Defense reduces incoming damage by 25%
of their value.

```
DamageReduction = (Evasion * 0.25) + (Defense * 0.25)  [HYPOTHESIS — S-B]
FinalDamage = max(1, BaseDamage - DamageReduction)  [HYPOTHESIS — S-B]
```

**Provenance:** tiomasta explicitly states "Evasion and Defense each subtract 25%
of their value from damage."

**Interpretation:** Evasion=100 and Defense=100 together reduce damage by
(100*0.25 + 100*0.25) = 50. A BaseDamage of 100 becomes 50.

**Test to verify:**
- Attack with BaseDamage=100 against a target with legs Evasion=100,
  Defense=0. Expected FinalDamage = 100 - 25 = 75.
- Same attack against Evasion=0, Defense=100. Expected: 75.
- Same attack against Evasion=100, Defense=100. Expected: 50.
- Same attack against Evasion=400, Defense=0. Expected: 100 - 100 = 0,
  clamped to 1 (minimum damage).

**Status:** HYPOTHESIS — needs disassembly (S-C) or in-game verification.

---

### F3: Hit/Miss Determination

**Claim:** Actions have a hit/miss check based on Success vs Evasion.

```
IF Success >= Evasion THEN hit  [HYPOTHESIS — S-B, derived from crit claim]
ELSE miss
```

**Alternative interpretation (accuracy formula):**
```
HitRate = Success / (Success + Evasion)  [HYPOTHESIS — common RPG pattern, not cited]
Roll random(0-99) < HitRate*100 THEN hit ELSE miss
```

**Provenance:** tiomasta focuses on crits (F4), not hit/miss. S-A confirms
Success affects "accuracy" but does not specify the formula. The deterministic
interpretation (Success >= Evasion) is an inference from the deterministic
crit claim.

**Interpretation:** If Success >= Evasion, the action always hits (ignoring
Defense). If Success < Evasion, the action always misses.

**Test to verify:**
- Attack with Success=50 vs target Evasion=40. Expected: always hit.
- Attack with Success=40 vs target Evasion=50. Expected: always miss.
- Attack with Success=50 vs target Evasion=50. Expected: always hit (>=).

**Status:** HYPOTHESIS — needs disassembly (S-C) or in-game verification.

---

### F4: Critical Hit Determination

**Claim:** Critical hits are deterministic based on ROS vs (Evasion + Defense),
with a possible small random factor.

```
CritThreshold = Evasion + Defense
IF Success >= CritThreshold THEN critical hit  [HYPOTHESIS — S-B]
ELSE normal hit/miss
```

**Provenance:** tiomasta: "crits are deterministic (ROS vs evasion+defense)
with a small random factor".

**Interpretation:** If Success >= Evasion + Defense, the hit is critical.
The "small random factor" suggests there may be a ±N range or a secondary
check, but this is unspecified. For now, we model the base deterministic
case.

**Critical hit effect:** tiomasta does not explicitly state the crit damage
multiplier. Common community assumption is 2x damage, but this is **UNVERIFIED**.

```
IF critical THEN
    FinalDamage = FinalDamage * 2  [UNVERIFIED — community assumption]
```

**Test to verify:**
- Attack with Success=100 vs target Evasion=40, Defense=50.
  CritThreshold = 90. Success >= 90, so critical hit.
- Attack with Success=100 vs target Evasion=40, Defense=61.
  CritThreshold = 101. Success < 101, so normal hit (if Success >= Evasion)
  or miss (if Success < Evasion).
- Observe if damage is doubled on crit (requires visible damage numbers or
  controlled HP tracking).

**Status:** HYPOTHESIS (formula) + UNVERIFIED (crit multiplier).

---

### F5: Armor Absorption

**Claim:** Damage is subtracted from the target part's Armor. When Armor reaches
0, the part is destroyed.

```
TargetArmor = TargetArmor - FinalDamage  [DOCUMENTED — S-A, battle-flow T0.2 rule 20]
IF TargetArmor <= 0 THEN
    TargetArmor = 0
    Part is destroyed and unusable for rest of battle  [DOCUMENTED — S-A, S-B]
```

**Provenance:** Medapedia Parts page and battle-flow spec both document
that parts are destroyed when Armor reaches 0.

**Test to verify:**
- Attack a part with Armor=100 with FinalDamage=50. Expected: Armor=50, part
  still functional.
- Attack same part again with FinalDamage=50. Expected: Armor=0, part
  destroyed.

**Status:** DOCUMENTED.

---

### F6: Part Destruction Damage Passthrough

**Claim:** When a part is destroyed (Armor = 0), excess damage passes through
to another part of the same Medarot.

```
IF FinalDamage > TargetArmor THEN
    ExcessDamage = FinalDamage - TargetArmor
    ; Select next part to absorb excess
    ; Priority: UNKNOWN — likely highest remaining Armor, or head last
    NextPart.Armor = NextPart.Armor - ExcessDamage  [HYPOTHESIS — community, not cited]
```

**Provenance:** tiomasta claims "part defense passes damage to highest-HP
parts" but this specific passthrough behavior for excess damage on destruction
is not explicitly documented in S-A or S-B. The Medapedia Parts page only
states that destroyed parts stay down for the battle.

**Test to verify:**
- Attack a part with Armor=50 with FinalDamage=100.
- Observe if another part on the same Medarot loses 50 Armor.

**Status:** HYPOTHESIS — needs citation or in-game verification.

---

### F7: Recovery-Turn Weakness (Radiation Phase)

**Claim:** During the Radiation/cooldown phase (returning to command line),
Medabots have attack-type weaknesses.

```
IF Target is in RAD phase THEN
    IF Attack is of type X THEN
        FinalDamage = FinalDamage * 2  ; or similar bonus  [HYPOTHESIS — S-B]
```

**Provenance:** tiomasta: "attack-type weaknesses during recovery turns".
No details on which attack types are strong against which recovery states,
nor the multiplier.

**Test to verify:**
- Execute a melee attack against a Medarot in RAD phase with melee legs.
  Observe damage vs same attack when target is ready.
- Execute a ranged attack against a Medarot in RAD phase with ranged legs.

**Status:** HYPOTHESIS — needs details from S-B or in-game verification.

---

### F8: Medal Compatibility Bonus

**Claim:** Medal compatibility with part Attribute provides a stat bonus.

```
IF Medal.Attribute matches Part.Attribute THEN
    AllPartStats *= (1 + CompatibilityBonus)  [UNVERIFIED — conflicting sources]
```

**Provenance:** Medapedia Medal page documents compatibility. Kenshin_Xtreme
 guide states +1 for Tortoise/Jellyfish/Bear medals. Owner-supplied report
 claims +7 for the same medals (CONFLICT — see BACKLOG.md 2026-09-23).

**Conflict resolution:** Until disassembly or in-game measurement resolves
this, compatibility bonus magnitude is **UNVERIFIED**. Do not implement in
engine without evidence.

**Status:** UNVERIFIED (magnitude). DOCUMENTED (that compatibility exists).

---

### F9: Anti-Type Bonus (Leg Type Interactions)

**Claim:** Anti-Air actions/parts deal bonus damage to Flying legs; Anti-Sea
to Aquatic legs.

```
IF Attack has Anti-Air flag AND Target.LegType == Flying THEN
    FinalDamage = FinalDamage * 2  [HYPOTHESIS — community, based on S-C]
IF Attack has Anti-Sea flag AND Target.LegType == Aquatic THEN
    FinalDamage = FinalDamage * 2  [HYPOTHESIS — community, based on S-C]
```

**Provenance:** Medapedia Leg type page states Flying/Aquatic have high stats
but are vulnerable to Anti-Air/Anti-Sea [S-A]. Kimbles' Medarot 1 notes show
non-zero anti-type flags at offsets 0x0D/0x0E for Flying/Aquatic legs [S-C
(from parts-and-actions T0.3)]. The exact multiplier is **UNVERIFIED**.

**Test to verify:**
- Attack a Flying-leg Medarot with an Anti-Air part/action.
  Expected: damage is higher than same attack without Anti-Air.
- Quantify the multiplier.

**Status:** HYPOTHESIS (multiplier). DOCUMENTED (that Anti-Air/Anti-Sea exist).

---

## Rules (pseudocode)

Numbered rules for action resolution. Labels per `docs/planning/content-rules.md`.

### Damage calculation

1. BaseDamage = Power + (Power * SkillLevel / 100) + (Success * 0.25) [HYPOTHESIS — S-B, F1]
2. DamageReduction = (Evasion * 0.25) + (Defense * 0.25) [HYPOTHESIS — S-B, F2]
3. FinalDamage = max(1, BaseDamage - DamageReduction) [HYPOTHESIS — S-B, F2]

### Hit/miss and crit

4. IF Success >= Evasion THEN hit = true ELSE hit = false [HYPOTHESIS — S-B, F3]
5. IF hit = false THEN FinalDamage = 0 [HYPOTHESIS — derived from F3]
6. CritThreshold = Evasion + Defense [HYPOTHESIS — S-B, F4]
7. IF hit = true AND Success >= CritThreshold THEN crit = true [HYPOTHESIS — S-B, F4]
8. IF crit = true THEN FinalDamage = FinalDamage * 2 [UNVERIFIED — community assumption]

### Armor and part destruction

9. TargetArmor = TargetArmor - FinalDamage [DOCUMENTED — S-A, F5]
10. IF TargetArmor <= 0 THEN TargetArmor = 0 AND mark part as destroyed [DOCUMENTED — S-A, F5]
11. IF part is destroyed THEN part is unusable for rest of battle [DOCUMENTED — S-A, F5]

### Passthrough (excess damage on destruction)

12. IF FinalDamage > original TargetArmor THEN ExcessDamage = FinalDamage - original TargetArmor [HYPOTHESIS — F6]
13. IF part destroyed THEN select next part by UNKNOWN priority AND apply ExcessDamage [HYPOTHESIS — F6]

### Special conditions

14. IF Target is in RAD phase THEN apply type-specific bonus (details UNKNOWN) [HYPOTHESIS — S-B, F7]
15. IF Attack has Anti-Air AND Target legs are Flying THEN FinalDamage *= 2 [HYPOTHESIS — F9]
16. IF Attack has Anti-Sea AND Target legs are Aquatic THEN FinalDamage *= 2 [HYPOTHESIS — F9]

### Leader rule interaction

17. IF Target is Leader Head AND TargetArmor <= 0 THEN battle ends immediately [DOCUMENTED — battle-flow T0.2 rule 22]
18. IF Target is Partner Head AND TargetArmor <= 0 THEN Partner stops functioning [DOCUMENTED — battle-flow T0.2 rule 21]

## Known unknowns / Open questions

- **Crit multiplier:** Is it 2x, 1.5x, or variable? No source confirms. [UNVERIFIED — F4]
- **Hit/miss formula:** Is it deterministic (Success >= Evasion) or probabilistic? tiomasta implies deterministic but doesn't specify hit/miss, only crits. [HYPOTHESIS — F3]
- **Small random factor in crits:** tiomasta mentions this but doesn't quantify. Could be ±5, ±10, or a die roll. [UNKNOWN — F4]
- **Passthrough priority:** When excess damage destroys a part, which part absorbs the overflow? Highest Armor? Head last? Random? [UNKNOWN — F6]
- **Recovery-turn weakness details:** Which attack types are strong against which RAD states? What multipliers? [UNKNOWN — F7]
- **Anti-type multiplier:** Is it exactly 2x? Or is it additive (+50%)? [HYPOTHESIS — F9]
- **Compatibility bonus magnitude:** +1 (Kenshin_Xtreme) vs +7 (owner report). [CONFLICT — see BACKLOG.md]
- **Skill level scaling:** Is it Power * (SkillLevel / 100) or a flat bonus? [HYPOTHESIS — F1]
- **Minimum damage:** Is it clamped at 1 or can it be 0 (complete miss)? [HYPOTHESIS — F2]
- **Success contribution to damage:** Is it Success * 0.25 added to BaseDamage, or does it scale Power multiplicatively? [HYPOTHESIS — F1]
- **Melee vs Ranged difference:** Do melee actions use different formulas than ranged? No source distinguishes them in damage calc. [UNKNOWN]
- **Pierce effect:** Byte G = 0B in Medarot 1 marks piercing attacks. Does this ignore Defense? Reduce Armor directly? Chain to adjacent parts? [UNVERIFIED — parts-and-actions T0.3 known unknown]

## Verification plan

### Phase 0 (current): Spec documentation
1. Document all community claims with explicit provenance (S-B) and HYPOTHESIS/UNVERIFIED labels.
2. Cross-check against Medarot 1 disassembly (S-C) for formula implementations.
3. Identify in-game test cases for each formula (see Test to verify sections above).

### Phase 1: Disassembly cross-check (manual research)
1. Read medarot1 disassembly battle routines for:
   - Damage calculation entry point
   - Hit/miss check implementation
   - Crit check implementation
   - Armor subtraction and part destruction
   - Passthrough logic
2. Map Medarot 1 findings to 2 CORE via S-A's continuity claim.
3. Record any Medarot 1 vs 2 CORE differences explicitly.

### Phase 2: In-game measurement (when Phase 1 engine enables seeded replays)
1. Set up controlled battles with known part stats.
2. Measure damage outcomes against formula predictions.
3. For probabilistic elements, run ≥100 trials to establish distributions.
4. Test edge cases: Success = Evasion, Success = Evasion + Defense, etc.

### Phase 3: Engine invariant tests
Once Phase 1 engine is implemented, add these pytest invariants:
- `test_damage_base_formula`: Verify F1 with known inputs and outputs
- `test_damage_reduction`: Verify F2 with various Evasion/Defense values
- `test_crit_deterministic`: Verify F4 with Success vs Evasion+Defense
- `test_armor_passthrough`: Verify F6 with excess damage scenarios
- `test_anti_type_bonus`: Verify F9 with Flying/Aquatic targets

## Derived test oracles

From the rules above, the following testable invariants can be derived for
future engine tests:

- **Deterministic damage:** Given the same part stats, Medal skill levels, and
  target stats, damage output is deterministic (assuming no random crit factor
  or probabilistic hit/miss). If S-B's "small random factor" is real, this
  becomes: damage is deterministic ±N where N is known.
- **Crit threshold:** A part with Success=100 always crits against targets with
  Evasion+Defense ≤ 100. [HYPOTHESIS — F4]
- **Evasion/Defense parity:** Evasion=100 and Defense=0 reduces damage by 25,
  same as Evasion=0 and Defense=100. [HYPOTHESIS — F2]
- **Minimum damage:** No attack deals 0 damage; minimum is 1. [HYPOTHESIS — F2]
- **Passthrough:** When FinalDamage > TargetArmor, exactly one other part on
  the Medarot loses Armor equal to ExcessDamage. [HYPOTHESIS — F6]
- **Anti-type:** Anti-Air vs Flying always deals ≥2x base damage. [HYPOTHESIS — F9]

## Action Items for Next Tasks

- **T0.7 (Data schema):** Include Damage, Success, Evasion, Defense fields in
  the Part schema with documented ranges (0-255 for most, 0-99 for Success).
- **T1.3 (Turn loop):** Implement damage resolution using HYPOTHESIS formulas
  with pluggable overrides for when VERIFIED formulas become available.
- **Future:** Add a `formula_version` field to the engine config to support
  switching between HYPOTHESIS and VERIFIED implementations.
