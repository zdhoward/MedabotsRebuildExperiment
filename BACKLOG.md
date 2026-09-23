# BACKLOG

Discoveries, bug reports, and ideas the agent records during sessions. The agent NEVER
implements from here. Humans promote items into ROADMAP.md via PR.

Format:
`- [date] [task context] idea/finding — evidence/source (optional: proposed micro-task)`

- [2026-09-23] [T0.1 source survey] Medapedia has no general "Actions" page (it's empty), but
  per-game "Actions in Medarot N" pages exist (e.g. Actions in Medarot 9). For T0.3 the
  action taxonomy should come from the Stats page skill list plus the Medarot 1 hacking
  notes action list, cross-checked against the medarot1 disassembly.
  — https://medarot.meowcorp.us/wiki/Actions , User:Kimbles/Medarot 1 Hacking Notes.
- [2026-09-23] [T0.1 source survey] tiomasta's GameFAQs thread claims crits in Medabots GBA
  are deterministic (ROS vs evasion+defense) with a small random factor, and that Evasion
  and Defense each subtract 25% of their value from damage. Community-tested, methodology
  not stated — prime HYPOTHESIS material to verify against the medarot1 disassembly in T0.4.
  — GameFAQs board "Explanation of game stats/mechanics here" (Medabots: Metabee).
- [2026-09-23] [T0.1 source survey] Kimbles' Medarot 1 hacking notes document the raw part
  byte layout (attribute, action, armor, skill, success, power, pierce, uses/charge,
  cooldown) and leg stat layout (armor, speed, mobility, fighting, shooting, scan,
  conceal) — directly informs the field set for the T0.7 data schemas.
  — Medapedia: User:Kimbles/Medarot 1 Hacking Notes.
- [2026-09-23] [T0.1 follow-up: owner-supplied 2 Core report] The owner supplied a compiled
  battle-mechanics report (docs/research/reports/). Citation spot-checks found: (1) the
  Medapedia pages it cites for the 30-Medal table and 60-action list ("Medals in Medarot
  2 CORE", "Actions in Medarot 2 CORE") are EMPTY — that data likely traces to the
  Fandom wiki, which is bot-blocked and unverifiable by automated fetch; (2) the report's
  Medal compatibility bonuses (+7 Tortoise/Jellyfish/Bear/etc.) CONFLICT with the verified
  Kenshin_Xtreme guide (+1 for the same medals; +4 Kabuto/Kuwagata matches both). The
  compatibility-bonus column must not enter data/ or a spec without disassembly or in-game
  verification — report section 49 vs Kenshin_Xtreme FAQ (gamefaqs.gamespot.com/gba/915188-medabots-metabee/faqs/24031).
- [2026-09-23] [T0.1 follow-up] The compiled report's [S7] cites "Kimbles' Medarot 2 Core
  Hacking Notes"; only the Medarot 1 hacking notes were found on Medapedia. If 2 Core
  hacking notes exist, find and verify the URL before citing them in a spec.
- [2026-09-23] [T0.1 follow-up] Verified from the Kenshin_Xtreme guide: skill levels cap at
  100 and level ~8 uses per skill level; medal evolution at 10/30/60 (+100 stat-only for
  Kabuto/Kuwagata). These are now documented guide claims (secondary source) for T0.5.
- [2026-09-23] [T0.2 battle-flow spec] Autocon's Rokusho guide (GameFAQs faqs/35357) is now
  verified live and appended to sources.md. It documents the timer rules (40/30/20 s; time
  counts only during movement toward/away from the active line) — but it EXPLICITLY leaves
  the third-level timer tie-break unresolved ("I'm not sure, but I think..."). The engine
  must not implement a third tie-break level until in-game or disassembly evidence exists.
  — https://gamefaqs.gamespot.com/gba/915189-medabots-rokusho/faqs/35357
- [2026-09-23] [T0.2 battle-flow spec] Version difference spotted on the Medapedia Battle
  system page: in GB-era games a ranged attack whose pre-selected target was destroyed
  mid-charge FAILS; Medarot DS/7 instead retarget. 2 CORE should follow the GB-era
  behavior, but the exact 2 CORE outcome deserves one in-game confirmation before the
  engine freezes it. — https://medarot.meowcorp.us/wiki/Battle_system
- [2026-09-23] [T0.2 battle-flow spec] No indexed source publishes the Target/Aim
  weighting algorithm (both Medapedia and Autocon confirm the bias exists, neither says how
  candidates are scored). Prime candidate for a medarot1 disassembly cross-check when T0.4
  starts; until then the engine needs a pluggable, explicitly-labeled approximation.
- [2026-09-23] [T0.2 session friction] PROMPT.md §3 references scripts/run_telemetry.py,
  which does not exist yet. Non-simulation sessions skip it gracefully (T0.1, T0.2 both
  did). First simulation-related task will need it created — roadmap owner decision.
- [2026-09-24] [T0.3 parts & actions spec] Medapedia Stats page (S-2) and Kenshin_Xtreme
  guide (S-4) together enumerate **41 distinct action types** across **8 skill categories**
  (Strike, Berserk, Shoot, Aim Shot, Defend, Heal, Support, Interrupt) and **24 attribute
  types** for part compatibility. The action taxonomy is now complete for T0.3 acceptance.
  — https://medarot.meowcorp.us/wiki/Stats, https://gamefaqs.gamespot.com/gba/915188-medabots-metabee/faqs/24031
- [2026-09-24] [T0.3 parts & actions spec] Kenshin_Xtreme guide documents the only
  verified damage formula in current sources: **Effective Berserk Power = Part Power + (Propulsion / 2)**.
  This becomes a primary test oracle for T0.4. — S-4.
- [2026-09-24] [T0.3 parts & actions spec] Head parts have **7 stats** (no CRG/RAD display),
  Arm parts have **8 stats** (CRG, RAD present), Leg parts have **7 stats** including
  terrain compatibility. The stat counts are now canonical per Medapedia Stats (S-2).
- [2026-09-24] [T0.3 parts & actions spec] Medapedia Leg type page (S-3) lists **7 leg
  types** (Bipedal, Multi-leg, Wheeled, Tank, Hover/Float, Flying, Aquatic) — complete list
  for T0.6 terrain matrix work. — https://medarot.meowcorp.us/wiki/Leg_type
- [2026-09-24] [T0.3 parts & actions spec] Several action types (Chain Reaction, Half
  Block, Full Block, Counter, Cross Attack setup, AutoRecover, Status Clear, Trap Clear,
  Boost Charge, Rapid Charge, No Escape, No Defense, Charge Drain, Ammo Drain, Force
  Drain, Force Bind, Pushover) are documented ONLY by Kenshin_Xtreme (S-4). These need
  cross-verification against Medarot 1 disassembly or Medapedia before entering data/
  for T0.8. — proposed micro-task: verify Kenshin_Xtreme action list against medarot1.
- [2026-09-24] [T0.3 parts & actions spec] **Open gap**: No source confirms whether Head
  Uses can be restored mid-battle via Heal actions, or only between battles. Marked
  UNKNOWN in spec; affects engine design for Heal skill implementation in T1.x.
- [2026-09-24] [T0.3 parts & actions spec] **Open gap**: tiomasta's claim that crits are
  deterministic (ROS vs Evasion+Defense) with a small random factor remains HYPOTHESIS
  grade (methodology unstated). Carried forward from T0.1 BACKLOG note; still needs
  disassembly or controlled in-game test to verify. — S-7.
