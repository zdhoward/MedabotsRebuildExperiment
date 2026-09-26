# Spec: Medals, Skill Levels & Medaforce

Status: DRAFT
Task: T0.5

Scope: Medarot 2 CORE (GBA; English releases "Medabots: Metabee" / "Medabots:
Rokusho"). This spec covers Medal statistics, Medal-part compatibility, the
skill leveling system, and Medaforce charge mechanics. Battle flow context is
in T0.2; parts/actions in T0.3; damage/success formulas in T0.4.

## Summary

A **Medal** is the core personality and stat modifier for a Medarot, determining
its attribute, targeting preferences, compatibility bonuses, and the Medaforce
gauge that powers special abilities [S-A][S-B]. Each Medal has **11 skill levels**
(0-100) corresponding to the 11 action skill types; these levels scale the
effective Power and Success of matching actions when used by parts that share
the same skill type [S-A][S-C].

Skill levels increase through **experience** gained by using actions of the
corresponding skill type; the Kenshin_Xtreme guide claims **~8 uses per skill
level**, with a hard cap at 100 [S-B]. Medals have **evolution ranks** at levels
10, 30, and 60, with Kabuto and Kuwagata Medals gaining +100 to all stats at
evolution (other Medal evolution effects are undocumented) [S-B].

**Medaforce** is a special gauge that charges over time and enables Medaforce
actions — powerful special abilities tied to the Medal rather than to parts
[S-A][S-B]. The gauge charges at a rate determined by the Medal's **nature**
and **target** stats, and can be expended to use Medaforce actions from the
command line [S-B].

**Compatibility** between Medal and part Attributes provides stat bonuses, but
the exact magnitude is in conflict between sources: Kenshin_Xtreme guide states
+1 for Tortoise/Jellyfish/Bear medals, while an owner-supplied report claims +7
for the same (see BACKLOG.md) [S-B HYPOTHESIS]. Until disassembly or in-game
measurement resolves this, the compatibility bonus magnitude is **UNVERIFIED**.

## Sources

- [x] [S-A] Medapedia, "Stats" — https://medarot.meowcorp.us/wiki/Stats —
  verified live 2026-09-23 (session T0.1): master reference for Medal stats
  (level, skill levels, attribute/compatibility, nature/target, Medaforce) and
  the 11 skill list. Primary source for Medal stat definitions.
- [x] [S-B] Medapedia, "Medal" — https://medarot.meowcorp.us/wiki/Medals —
  verified live 2026-09-25: Medal attribute, compatibility bonus, nature/target,
  XP leveling, skill levels, evolution ranks, and Medaforce/Charge gauge.
  Primary source for T0.5.
- [x] [S-C] GameFAQs: Kenshin_Xtreme's "Medabots RPG Walkthrough" (v3.50, 2004) —
  https://gamefaqs.gamespot.com/gba/915188-medabots-metabee/faqs/24031 —
  verified live 2026-09-23 (session T0.1): documents skill leveling (8 uses
  per skill level, max 100), medal evolution (10/30/60, +100 for Kabuto/Kuwagata),
  the Aim attribute, and a full Medal FAQ with attributes, aims, compatibility
  bonuses. Secondary source for T0.5.
- [ ] [S-D] Medarot 1 disassembly (github.com/Medabots/medarot1) — read-only
  oracle, not yet consulted for this spec. Medapedia Battle system page claims
  the battle system "has remained mostly unchanged since Medarot 1", so Medarot
  1's Medal and skill level routines are valid cross-checks for 2 CORE [S-A].
  Marked as future verification target.
- [ ] [S-E] Owner-supplied compiled report,
  `docs/research/reports/2026-09-23-medarot2-core-battle-systems-report.md` —
  AI-compiled; per repo policy not citable as evidence. Its Medal compatibility
  bonuses (+7 for Tortoise/Jellyfish/Bear) CONFLICT with S-C's +1 claim.
  See BACKLOG.md 2026-09-23.

## Medal Statistics

### Medal stat definitions

| Stat | Type | Range | Role |
|------|------|-------|------|
| Level | Medal | 1-100 | Overall Medal level; increases with XP [DOCUMENTED — S-A, S-B] |
| Attribute | Medal | 0-15 | Elemental/affinity type; matches part Attribute for compatibility [DOCUMENTED — S-A, S-B] |
| Compatibility | Medal | N/A | Bonus applied when part Attribute matches Medal Attribute [DOCUMENTED — S-A, S-B; magnitude UNVERIFIED] |
| Nature | Medal | 0-15 | Bias for Medal's behavior; influences Medaforce charge rate [DOCUMENTED — S-A, S-B] |
| Target | Medal | 0-15 | Aim/Target preference; biases which enemy parts are selected [DOCUMENTED — S-A, S-B] |
| Medaforce | Medal | 0-100 | Current Medaforce gauge level; depletes when using Medaforce actions [DOCUMENTED — S-A, S-B] |
| Skill Levels | Medal | 0-100 (each) | 11 values, one per skill type; scales effective stats for matching actions [DOCUMENTED — S-A, S-B] |

**Note on ranges:** Medapedia does not specify exact numeric ranges for Nature,
Target, or Attribute. The 0-15 range is inferred from Medarot 1 byte-sized fields
[S-C]; needs 2 CORE disassembly confirmation.

### Attribute system

Medals and parts both have an **Attribute** that determines compatibility [S-A, S-B].
The Medapedia Medals page lists common attributes but does not provide a complete
enumeration [S-B]. Medarot 1 disassembly shows Attributes as a byte field in both
Medal and part data [S-C]; 2 CORE likely inherits this.

**Known Attributes (from S-B, S-C):**
- Tortoise (テタン)
- Jellyfish (クラゲ)
- Bear (クマ)
- Kabuto (カブト)
- Kuwagata (クワガタ)
- Insect (昆虫)
- Bird (鳥)
- Beast (獣)
- Fish (魚)
- Robot (ロボット)
- Demon (悪魔)
- Plant (植物)

**Compatibility rule:**
- IF Medal.Attribute == Part.Attribute THEN compatibility bonus applies [DOCUMENTED — S-A, S-B]

**Compatibility bonus magnitude:**
- Kenshin_Xtreme guide: +1 to all part stats for Tortoise/Jellyfish/Bear [S-C]
- Owner report: +7 to all part stats for Tortoise/Jellyfish/Bear [S-E — NOT CITABLE]
- **Status: DOCUMENTED that compatibility exists; magnitude UNVERIFIED**

## Skill Types and Skill Levels

### The 11 skill types

Each Medal has 11 skill levels, one for each action skill type [S-A, S-B].
The skill types and their Medarot 2 CORE English names are:

| # | Skill Type | English (Metabee/Rokusho) | Notes |
|---|------------|----------------------------|-------|
| 1 | Strike | Strike | Melee basic attack [DOCUMENTED — S-A, S-C] |
| 2 | Berserk | Berserk/Reckless | High-damage melee, lower accuracy [DOCUMENTED — S-A, S-C] |
| 3 | Shoot | Shoot | Basic ranged attack [DOCUMENTED — S-A, S-C] |
| 4 | Snipe | Snipe/Aim Shot | High-accuracy ranged attack [DOCUMENTED — S-A, S-C] |
| 5 | Protect | Protect/Defend | Defensive action [DOCUMENTED — S-A, S-C] |
| 6 | Heal | Heal | HP restoration [DOCUMENTED — S-A, S-C] |
| 7 | Support | Support | Buff/debuff support [DOCUMENTED — S-A, S-C] |
| 8 | Disrupt | Disrupt/Interrupt | Status effects, action interruption [DOCUMENTED — S-A, S-C] |
| 9 | Set-up | Set-up | Preparatory actions [DOCUMENTED — S-A, S-C] |
| 10 | Special | Special | Special category actions [DOCUMENTED — S-A, S-C] |
| 11 | Other | Other | Miscellaneous/uncategorized actions [DOCUMENTED — S-A, S-C] |

**Skill type mapping note:** Medarot 1 uses byte values 01-0F for skills, but
Kimbles' notes show duplicates (Strike at 01 and 03, Berserk at 02 and 04, etc.)
[S-C]. Whether 2 CORE has a cleaner 1-to-1 mapping is **UNVERIFIED**.

### Skill level mechanics

**Rule: Skill level scaling**
1. When a part performs an action, the Medal's skill level for that action's
   Skill type is applied to the action's calculation [DOCUMENTED — S-A, S-B, parts-and-actions T0.3 rule 22]
2. Higher skill level = higher accuracy, faster charge, or more power for
   actions of that Skill type [DOCUMENTED — S-A, S-B]
3. The skill level scales the effective Power or Success of matching actions
   [HYPOTHESIS — see damage-and-success T0.4 F1 for proposed formula]

**Skill level progression:**
- Skill levels range from 0 to 100 [DOCUMENTED — S-A, S-B]
- Each skill level requires **approximately 8 uses** of actions of that skill type
  to level up [DOCUMENTED — S-C: "8 uses per skill level"]
- Total uses required to max a skill (0->100): 800 uses [DERIVED — S-C]
- All skill levels cap at 100 [DOCUMENTED — S-C]

**Test to verify skill level progression:**
- Start with a Medal with Shoot skill level 0.
- Use a Shoot-action part 8 times in battle.
- After battle, verify Shoot skill level increased to 1.
- Repeat to confirm the ~8 uses per level rate.

**Status: DOCUMENTED (rate and cap); formula for stat scaling is HYPOTHESIS (T0.4 scope).**

### Skill level interaction with actions

From parts-and-actions T0.3, rule 22:
- When an action is used, its Success is modified by the Medal's corresponding
  Skill level [DOCUMENTED — S-A]

The damage-and-success T0.4 spec proposes the following formula (HYPOTHESIS — S-B):
```
BaseDamage = Power + (Power * (SkillLevel / 100)) + (Success * 0.25)
```

This means:
- A Shoot action with Power=100 used by a Medal with Shoot skill level 50
  gets +50% Power: BaseDamage = 100 + (100 * 50/100) + (Success * 0.25) = 150 + (Success * 0.25)
- The same action with Shoot skill level 100 gets +100% Power: 200 + (Success * 0.25)

**Note:** The exact scaling formula is HYPOTHESIS and subject to verification
against disassembly (S-D) or in-game measurement.

## Medal Evolution

Medals have **evolution ranks** that unlock at specific Level thresholds [S-B, S-C].

**Evolution thresholds:**
- Level 10: First evolution
- Level 30: Second evolution
- Level 60: Third evolution

**Evolution effects:**
- For **Kabuto** and **Kuwagata** Medals: +100 to all stats at each evolution
  threshold [DOCUMENTED — S-C]
- For other Medals: evolution effects are **not documented** in any verified
  source [UNKNOWN]

**Test to verify evolution effects:**
- Level a Kabuto Medal to exactly level 10, observe stat changes.
- Level to 30 and 60, confirm +100 all stats at each threshold.
- Level a non-Kabuto/Kuwagata Medal through evolution thresholds to document
  their effects.

**Status: DOCUMENTED for Kabuto/Kuwagata; UNKNOWN for other Medals.**

## Medaforce

### Medaforce gauge

The **Medaforce gauge** is a special resource that charges over time and enables
Medaforce actions [S-A, S-B].

**Gauge mechanics:**
1. The Medaforce gauge starts at 0 at battle begin [DOCUMENTED — S-B]
2. The gauge **charges automatically over time** while the Medarot is active
   in battle [DOCUMENTED — S-A, S-B]
3. The charge rate is determined by the Medal's **Nature** and **Target** stats
   [HYPOTHESIS — S-B; exact formula UNVERIFIED]
4. The gauge maximum is **100** [DOCUMENTED — S-A, S-B]
5. Using a Medaforce action **consumes** Medaforce from the gauge [DOCUMENTED — S-B]

**Nature and Target influence:**
- Nature: affects how quickly Medaforce charges [DOCUMENTED — S-A, S-B]
- Target: affects targeting preferences and may influence Medaforce charge
  in some Medals [DOCUMENTED — S-A, S-B; exact interaction UNVERIFIED]

**Test to verify charge rate:**
- Equip Medals with different Nature values.
- Observe Medaforce gauge fill rate over identical battle conditions.
- Quantify the relationship between Nature and charge speed.

**Status: DOCUMENTED (gauge exists, max=100, depletes on use); charge rate formula UNKNOWN.**

### Medaforce actions

Medaforce actions are **special abilities tied to the Medal**, not to parts [S-A, S-B].
They consume the Medaforce gauge when used.

**Medaforce action characteristics:**
1. Medaforce actions are selected from the command line (not tied to a specific part)
   [DOCUMENTED — S-B]
2. Each Medal has a fixed set of Medaforce actions available [DOCUMENTED — S-B]
3. Medaforce actions consume a variable amount of Medaforce gauge (typically
   25, 50, or 100) [HYPOTHESIS — S-B; exact costs per Medal UNVERIFIED]
4. Medaforce actions cannot be used if the gauge is insufficient [DOCUMENTED — S-B]

**Known Medaforce action categories (from S-B):**
- Area-of-effect attacks
- Powerful single-target attacks
- Team-wide buffs
- Healing
- Special effects (e.g., instant part repair, status immunity)

**Test to verify Medaforce actions:**
- Use a Medaforce action with full gauge (100), observe gauge depletion.
- Attempt to use the same action with insufficient gauge, verify it fails.

**Status: DOCUMENTED (existence, selection); costs and effects per Medal UNKNOWN.**

### Charge command

From battle-flow T0.2 rule 6: the fighter may issue a "charge the Medaforce gauge"
command from the command line [DOCUMENTED — S-B].

**Charge command mechanics:**
1. Selecting "Charge" from the command menu causes the Medarot to **not move**
   to the active line [DOCUMENTED — S-B]
2. The Medaforce gauge charges at an **accelerated rate** during the Charge
   command [HYPOTHESIS — S-B; exact rate UNVERIFIED]
3. The Medarot remains at the command line and can issue another command
   immediately after the Charge completes [DOCUMENTED — S-B]

**Test to verify Charge command:**
- Use Charge command, observe Medaforce gauge increase.
- Compare gauge increase from Charge vs passive charging over same time.

**Status: DOCUMENTED (existence); accelerated rate magnitude UNKNOWN.**

## Rules (pseudocode)

Numbered rules for Medal, skill level, and Medaforce behavior.

### Medal compatibility

1. IF Medal.Attribute == Part.Attribute THEN ApplyCompatibilityBonus(Part) [DOCUMENTED — S-A, S-B]
2. CompatibilityBonus magnitude = UNKNOWN (conflict: +1 vs +7) [UNVERIFIED]

### Skill level progression

3. FOR each skill type (1-11): Medal.SkillLevel[skill] ranges 0-100 [DOCUMENTED — S-A, S-B]
4. ON action use of skill type S: Medal.XP[S] += 1 [DOCUMENTED — S-C]
5. IF Medal.XP[S] >= 8 THEN Medal.SkillLevel[S] += 1 AND Medal.XP[S] = 0 [DOCUMENTED — S-C]
6. Medal.SkillLevel[S] = min(Medal.SkillLevel[S], 100) [DOCUMENTED — S-C]

### Skill level application

7. ON action with Skill type S: EffectivePower = Power * (1 + Medal.SkillLevel[S] / 100) [HYPOTHESIS — S-B, see T0.4 F1]
8. ON action with Skill type S: EffectiveSuccess = Success + (Medal.SkillLevel[S] * SuccessFactor) [HYPOTHESIS — SuccessFactor UNVERIFIED; T0.4 scope]

### Medaforce gauge

9. ON battle start: Medal.Medaforce = 0 [DOCUMENTED — S-B]
10. ON each frame (or time unit): Medal.Medaforce += ChargeRate [DOCUMENTED — S-A, S-B]
11. ChargeRate = BaseRate * NatureModifier [HYPOTHESIS — exact formula UNVERIFIED]
12. Medal.Medaforce = min(Medal.Medaforce, 100) [DOCUMENTED — S-A, S-B]

### Medaforce actions

13. ON Medaforce action selection: IF Medal.Medaforce >= action.Cost THEN Medal.Medaforce -= action.Cost AND execute action ELSE fail [DOCUMENTED — S-B]
14. Medaforce action.Cost is Medal-specific [HYPOTHESIS — S-B; exact values UNVERIFIED]

### Charge command

15. ON Charge command: Medal.Medaforce += ChargeCommandBonus [DOCUMENTED — S-B]
16. ChargeCommandBonus > normal passive charge [HYPOTHESIS — S-B; exact value UNVERIFIED]

### Medal evolution

17. ON Medal.Level >= 10: TriggerEvolution(Medal, rank=1) [DOCUMENTED — S-B, S-C]
18. ON Medal.Level >= 30: TriggerEvolution(Medal, rank=2) [DOCUMENTED — S-B, S-C]
19. ON Medal.Level >= 60: TriggerEvolution(Medal, rank=3) [DOCUMENTED — S-B, S-C]
20. IF Medal.Type == Kabuto OR Medal.Type == Kuwagata: ON TriggerEvolution THEN Add 100 to all Medal stats [DOCUMENTED — S-C]
21. FOR other Medal types: Evolution effect = UNKNOWN [UNVERIFIED]

## Known unknowns / Open questions

- **Compatibility bonus magnitude:** +1 (Kenshin_Xtreme guide) vs +7 (owner report).
  Conflict documented in BACKLOG.md. [CONFLICT — needs disassembly or in-game verification]
- **Charge rate formula:** How exactly do Nature and Target affect Medaforce
  gauge charging? Is it multiplicative, additive, or threshold-based? [UNKNOWN]
- **Medaforce action costs:** What are the exact Medaforce costs for each Medal's
  Medaforce actions? [UNKNOWN]
- **Charge command bonus:** How much extra Medaforce does the Charge command
  provide compared to passive charging? [UNKNOWN]
- **Other Medal evolution effects:** What stat bonuses do non-Kabuto/Kuwagata
  Medals receive at evolution thresholds? [UNKNOWN]
- **Nature and Target stat ranges:** What are the valid numeric ranges for these
  stats? Medarot 1 uses byte fields (0-255), but 2 CORE may differ. [UNVERIFIED]
- **Skill level XP persistence:** Does XP toward the next skill level persist across
  battles, or is it reset after each battle? [UNKNOWN]
- **Nature stat effects:** Beyond Medaforce charging, does Nature affect any other
  mechanics (e.g., stat growth, action selection)? [UNKNOWN]
- **Target stat effects:** How exactly does Target/Aim bias the targeting selection
  algorithm? See battle-flow T0.2 known unknown. [UNKNOWN]
- **Medaforce gauge decay:** Does the Medaforce gauge decay over time or only
  when using Medaforce actions? [UNKNOWN]
- **Multiple Medaforce uses per battle:** Can a single Medarot use multiple
  Medaforce actions in one battle if it has sufficient gauge? [UNKNOWN]

## Verification plan

### Phase 0 (current): Spec documentation
1. Document all Medal/skill/Medaforce claims with explicit provenance and
   HYPOTHESIS/UNVERIFIED/UNKNOWN labels.
2. Cross-reference against existing verified sources (S-A, S-B, S-C).

### Phase 1: Disassembly cross-check (manual research)
1. Read Medarot 1 disassembly for:
   - Medal data structure and stat layouts
   - Skill level XP tracking and progression
   - Medaforce gauge implementation and charge rate
   - Medaforce action definitions and costs
   - Evolution trigger conditions and stat modifications
2. Map Medarot 1 findings to 2 CORE via S-A's continuity claim.
3. Record any Medarot 1 vs 2 CORE differences explicitly.

### Phase 2: In-game measurement
1. **Compatibility bonus:** Equip a Tortoise Medal with Tortoise-attribute parts
   and non-Tortoise parts. Compare stats to measure the bonus magnitude.
2. **Skill level progression:** Use a single action type repeatedly and track
   skill level increases. Confirm the ~8 uses per level rate.
3. **Medaforce charge rate:** Time how long it takes for the gauge to fill
   from 0 to 100 with different Nature values.
4. **Medaforce action costs:** Use Medaforce actions and observe gauge
   depletion amounts.
5. **Evolution effects:** Level various Medals through evolution thresholds
   and document stat changes.

### Phase 3: Engine invariant tests
Once Phase 1 engine is implemented, add these pytest invariants:
- `test_compatibility_bonus`: Verify parts with matching Attribute receive
  the compatibility bonus (once magnitude is VERIFIED)
- `test_skill_level_scaling`: Verify EffectivePower = Power * (1 + SkillLevel/100)
  (if formula is VERIFIED)
- `test_medaforce_charge`: Verify gauge increases at expected rate
- `test_medaforce_consumption`: Verify using a Medaforce action depletes gauge
  by correct amount
- `test_skill_level_cap`: Verify skill levels cannot exceed 100
- `test_evolution_trigger`: Verify evolution triggers at correct levels

## Derived test oracles

From the rules above, the following testable invariants can be derived:

- **Skill level cap:** No skill level exceeds 100, regardless of XP accumulation
  (rule 6).
- **Medaforce cap:** The gauge never exceeds 100 (rule 12).
- **Medaforce exhaustion:** A Medaforce action with cost > current gauge fails
  (rule 13).
- **Kabuto/Kuwagata evolution:** These Medals gain +100 to all stats at levels
  10, 30, and 60 (rules 17-20).
- **Skill level progression rate:** 8 uses of a skill type = +1 skill level
  (rules 4-5).
- **Compatibility:** Matching Medal/part Attributes always apply a bonus
  (rule 1), but the magnitude is UNKNOWN.

## Action Items for Next Tasks

- **T0.7 (Data schema):** Include Medal fields: Attribute, Compatibility,
  Nature, Target, Medaforce, Level, and 11 SkillLevel values. Include Part
  fields: Attribute (for compatibility matching).
- **T1.2 (Data loading):** Validate that Medal data includes all fields
  documented here.
- **T1.3 (Turn loop):** Implement Medaforce gauge charging during CRG/RAD
  phases, and Medaforce action execution.
- **Future:** Add pluggable formula overrides for compatibility bonus and
  Medaforce charge rate to support switching between HYPOTHESIS and
  VERIFIED implementations.
