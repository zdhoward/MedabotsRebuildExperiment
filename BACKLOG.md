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
