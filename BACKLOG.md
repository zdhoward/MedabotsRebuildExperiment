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
