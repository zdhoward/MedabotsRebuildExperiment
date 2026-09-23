# Source Index

Working bibliography. Every mechanics spec must cite entries from here.
Link-verified 2026-09-23 (session T0.1). Mark anything unverified as UNVERIFIED in specs.

## Primary references — Medapedia (community wiki)

- **Battle system** — https://medarot.meowcorp.us/wiki/Battle_system
  Leader-defeat victory condition, 3v3 lane layout, command line → active line movement
  loop, and the shooting-vs-melee targeting split (ranged pre-selects targets; melee always
  hits the enemy closest to the active line). Says the battle system "has remained mostly
  unchanged since Medarot 1" — our justification for using the Medarot 1 disassembly as the
  primary oracle for a Medarot 2 CORE target. Primary source for T0.2.

- **Stats** — https://medarot.meowcorp.us/wiki/Stats
  The master stats reference: medal stats (level, skill levels, attribute/compatibility,
  nature/target, Medaforce) vs part stats (head/arm: action, skill, armor, power, success,
  charge, cooldown, uses; legs: leg type, propulsion, evasion/mobility, defense, proximity,
  remoteness). Lists the 11 series skills (Strike, Berserk/Reckless, Shoot, Snipe/Aim Shot,
  Protect/Defend, Heal, Support, Disrupt/Interrupt, Set-up, Special, Other). Primary source
  for T0.3, T0.4, T0.5.

- **Leg type** — https://medarot.meowcorp.us/wiki/Leg_type
  The seven leg types (Bipedal, Multi-leg, Wheeled, Tank, Hover/Float, Flying, Aquatic) and
  the terrain bonus/penalty system. Flying/Aquatic have high stats but are vulnerable to
  Anti-Air/Anti-Sea. Primary source for T0.6.

- **Medal** — https://medarot.meowcorp.us/wiki/Medals
  Medal attribute, compatibility bonus, nature/target, XP leveling, skill levels, evolution
  ranks (levels 0/10/30/60/100 in GB-era games), and the Medaforce/Charge gauge. Primary
  source for T0.5.

- **Parts** — https://medarot.meowcorp.us/wiki/Parts
  Short overview: head + right arm + left arm + legs = one battle-ready Medarot on a Tinpet;
  parts destroyed in battle stay down for that battle. Context for T0.3/T0.8.

- **User:Kimbles/Medarot 1 Hacking Notes** —
  https://medarot.meowcorp.us/wiki/User:Kimbles/Medarot_1_Hacking_Notes
  Community research into Medarot 1's part data layout (per-part byte fields: attribute,
  action, armor, skill, success, power, pierce, uses/charge, cooldown, leg type) and a full
  action list. Use for cross-checking our T0.7 data schemas — numbers, not code.

- **Guide: Medarot 2 / 2 CORE / Medabots guide** —
  https://medarot.meowcorp.us/wiki/Guide:Medarot_2_/_2_CORE_/_Medabots_guide
  Play-oriented guide to the exact English game we target (leg types, compatibility, medal
  proficiencies, battle walkthroughs). Secondary/corroborating source.

## Community research — forums

- **GameFAQs board: "Explanation of game stats/mechanics here" (Medabots: Metabee GBA)** —
  https://gamefaqs.gamespot.com/boards/915188-medabots-metabee/79284943
  tiomasta's empirical mechanics breakdown of the exact game we target: crits are
  deterministic (ROS vs evasion+defense), part defense passes damage to highest-HP parts,
  Evasion and Defense each subtract 25% of their value from damage, ROS adds 25% of itself
  as bonus damage, attack-type weaknesses during recovery turns, terrain speed multipliers,
  debuff stacking rules. Some claims lack stated methodology — treat as HYPOTHESIS until
  cross-checked against the disassembly. Key input for T0.4.

- **GameFAQs: Imaku's Guide and Walkthrough (Medabots: Metabee)** —
  https://gamefaqs.gamespot.com/gba/915188-medabots-metabee/faqs/32327
  English-language walkthrough covering robattle mechanics, leader/partner team order, and
  part categories in the official English terms. Secondary source for T0.2/T0.3.

- **Medabots Discord (community research hub)** — join via the decomp projects below.
  Where Medapedia authors and disassembly contributors hang out. Ask-before-assert source;
  anything learned here must be reproduced from a citable source before it enters a spec.

## Disassembly projects (READ-ONLY ORACLES — clean-room reference, never copy)

- **Medarot 1 (GB): Medabots/medarot1** — https://github.com/Medabots/medarot1
  Medarot 1 disassembly/translation (RGBDS). Primary behavior oracle: the battle system is
  mostly unchanged since Medarot 1 (per Medapedia Battle system), so charge/cooldown timing,
  success rolls, and part behavior cross-checks come from here. Read code, cite file+label,
  never copy.

- **Medarot 3 (GBC): Medabots/medarot3** — https://github.com/Medabots/medarot3
  Medarot 3 disassembly/translation. Secondary oracle; useful for mechanics that 2 CORE
  inherited into the GBC era.

- **Medarot 4 (GBC): Medabots/medarot4** — https://github.com/Medabots/medarot4
  Medarot 4 disassembly/translation. Secondary oracle, same caveats as medarot3.

- **Medarot Parts Collection GB: Medabots/medarot1-pc** — https://github.com/Medabots/medarot1-pc
  Parts Collection disassembly/translation. Useful for part data organization research (T0.7).

## Reference games

- **Medabots: Metabee / Rokusho (GBA)** — English release of Medarot 2 CORE (remake of
  Medarot 2). The system we target: the Medarot 2 CORE battle system. All empirical
  behavior claims should be phrased against this game.

## Usage rules

- Reading disassembly = allowed (understanding, verification).
- Copying code/data = never. Cite everything. Mark UNVERIFIED when unsure.
- Forum/Discord claims start as HYPOTHESIS; they need a disassembly cross-check or an
  in-game measurement before a spec marks them VERIFIED.
