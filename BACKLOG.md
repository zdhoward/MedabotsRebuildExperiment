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
- [2026-09-24] [T0.3 parts-actions spec] Kimbles' Medarot 1 Hacking Notes (Medapedia)
  provide **16-byte part layouts** for both head/arm and legs, including the crucial
  distinction: head/arm byte 0x07 = Uses (for heads) or Charge (for arms), byte 0x08 =
  always 00 (heads) or Cooldown (arms). This confirms heads have finite uses while arms
  are infinite. Same layout for 2 CORE needs disassembly verification.
  — https://medarot.meowcorp.us/wiki/User:Kimbles/Medarot_1_Hacking_Notes
- [2026-09-24] [T0.3 parts-actions spec] Kimbles documents **~40 distinct actions** in
  Medarot 1 (hex 00-37 with gaps), with a 60-slot table. The owner report's claim of
  "60 actions in 2 CORE" cannot be verified because Medapedia's "Actions in Medarot 2
  CORE" page is EMPTY. The exact action count for 2 CORE remains UNKNOWN.
  — https://medarot.meowcorp.us/wiki/User:Kimbles/Medarot_1_Hacking_Notes
- [2026-09-24] [T0.3 parts-actions spec] Medapedia Stats page lists **11 skills** but
  Kimbles' skill byte mapping (01-0F) shows duplicates: Strike at 01 and 03, Berserk at
  02 and 04, Heal at 0A and 0B, Protect at 08 and 09, Support at 07/0C/0D. Whether 2 CORE
  has a cleaner 1-to-1 skill→byte mapping is UNVERIFIED.
  — https://medarot.meowcorp.us/wiki/Stats, https://medarot.meowcorp.us/wiki/User:Kimbles/Medarot_1_Hacking_Notes
- [2026-09-24] [T0.3 parts-actions spec] Leg parts have **10 stats** in Medarot 1:
  Attribute, Leg type, Armor, Speed, Mobility, Fighting (Melee), Shooting, Scan, Conceal,
  plus anti-type flags at 0x0D/0x0E. Conceal stat is hidden in Medarot 1's stat screen
  but visible in Medarot 2. This layout needs 2 CORE disassembly confirmation.
  — https://medarot.meowcorp.us/wiki/User:Kimbles/Medarot_1_Hacking_Notes
- [2026-09-23] [pipeline ops] Same-day reruns of daily_agent can collide on session
  branch names (session/YYYY-MM-DD-<task-id>); the workflow's PR step no-ops if a PR
  is already open, but a fresh agent push to the same branch stacks commits on the old
  session. Proposed micro-task: suffix branch names on collision.
  — .github/workflows/daily_agent.yml "Open session PR" step.
- [2026-09-23] [pipeline ops] Session-branch discovery uses a 45-minute freshness
  window on refs/remotes/origin/session/*; a run whose agent pushes nothing while a
  <45-min-old session branch exists can gate the wrong branch.
  — .github/workflows/daily_agent.yml "Discover pushed session branch" step.
- [2026-09-23] [pipeline ops] PRs opened or pushed with the workflow GITHUB_TOKEN
  never trigger ci.yml pull_request checks (GitHub design). The daily run's publish
  gate substitutes; a manual `gh workflow run ci.yml --ref <branch>` re-validates any
  session branch if needed.
  — .github/workflows/ci.yml workflow_dispatch trigger.
- [2026-09-24] [pipeline ops] T0.4 post/session_report recorded commit_sha 7853b2b, a pre-amend
  hash unreachable on origin. The daily runner's publish gate passed only because the
  agent's loose objects were still in the workspace; any fresh clone (PR CI
  validate-post job) would reject it. Fixed in-branch (f71707c recorded; same fix
  pattern as T0.3 commit d9ff84c). Root cause: agent records commit_sha before its
  final amend/push. Proposed micro-task: prompt/HANDOFF guidance to record commit_sha
  only after the final push, or re-derive it in the PR step.
  — temp/session_report.json, scripts/validate_post.py commit check
- [2026-09-25] [T0.5 medals-medaforce spec] The compatibility bonus conflict
  (Kenshin_Xtreme +1 vs compiled report +7) resurfaced during Medal spec authoring.
  This now **blocks Phase 1**: T0.7 data schemas need the field type, and T0.8
  seed dataset needs actual values. Medapedia Medals page confirms the existence
  of compatibility bonuses but does not publish magnitudes. Prime candidate for
  medarot1 disassembly verification (justified by Medapedia's "mostly unchanged
  since Medarot 1" claim) — or controlled in-game measurement.
  — S-M (existence confirmed), S-K (+1 claim), compiled report section 49 (+7 claim)
