# Research Report: Medabots (GBA) / Medarot 2 Core — Battle Mechanics and Gameplay Systems

> **Provenance note (added by the maintaining session, 2026-09-23 — not part of the original
> report):** This report was supplied by the project's human owner as AI-compiled research
> input. It is preserved verbatim below, including its own source key ([S1]–[S8]).
> Citation spot-checks performed on commit:
> - **[S3-alt] Kenshin_Xtreme walkthrough** (https://gamefaqs.gamespot.com/gba/915188-medabots-metabee/faqs/24031)
>   — fetched and read; **verified live**.
> - **[S8] Rokusho (KWG-1)** (https://medarot.meowcorp.us/wiki/Rokusho_(KWG-1)) — page
>   exists; **verified live**.
> - **Medapedia main page** (https://medarot.meowcorp.us/wiki/Medapedia) — **verified live**.
> - **[S2] "Medals in Medarot 2 CORE" and "Actions in Medarot 2 CORE"** — both Medapedia
>   pages are currently **EMPTY**; the report's 30-Medal table and 60-action list could not
>   be re-verified from those URLs and likely trace to [S1] Fandom.
> - **[S1] Medabots Fandom wiki** — bot-blocked ("Please contact the site owner for
>   access"); **could not be verified by automated fetch**.
> - **[S4] gsk6390/tiomasta GameFAQs threads** — the "Explanation of game stats/mechanics
>   here" thread was independently verified live in session T0.1.
> - The supplied Wikipedia series URL did not resolve to a series article at fetch time.
> - **Compatibility-bonus discrepancy:** the verified Kenshin_Xtreme guide lists +1
>   compatibility for Tortoise/Jellyfish/Bear/Spider/Snake/Queen/Squid(Kraken)/Phoenix,
>   while the report's Medal table (section 49) lists +7 for those Medals. Unresolved —
>   see BACKLOG.md; do not treat either column as fact until checked against the
>   disassembly or the game itself.
>
> **Repo policy:** per AGENTS.md, community-tested material here is HYPOTHESIS-grade until
> a mechanics spec cites it against a verified oracle. Nothing in this report has
> ROM-source-code proof. Do not copy data tables from it into `data/` without independent
> verification of each value.

---

MEDABOTS (GBA) / MEDAROT 2 CORE
COMPREHENSIVE BATTLE-MECHANICS AND GAMEPLAY-SYSTEMS REPORT
Scope: Battle mechanics, Medabots, parts, stats, Medals, skills, actions, targeting/AI, timing, terrain, status effects, Medaforce, defense/evasion, damage, progression, and version-specific mechanical differences.
Explicitly excluded: story, characters as narrative subjects, dialogue, plot progression except where it determines access to battle-system resources.

RESEARCH STANDARD
-----------------
This report separates information into three confidence levels:

[DOCUMENTED]
Directly documented by the game's reference material, Fandom/Medapedia databases, or multiple long-standing game guides.

[COMMUNITY-TESTED]
Mechanics derived from repeated testing by experienced players, especially the long-running gsk6390/GameFAQs mechanics research and later follow-up testing. These are useful and often very specific, but are not presented as ROM-source-code proof unless a source actually establishes that.

[UNVERIFIED / NOT STATED]
Where available documentation does not establish an exact formula or algorithm, this report explicitly says so rather than filling the gap with an assumption.

The English GBA releases "Medabots: Metabee" and "Medabots: Rokusho" are the localized versions of "Medarot 2 Core", a GBA remake/update of Medarot 2. The GBA version retains the basic Medarot 2 structure but incorporates battle-system changes from later Medarot games, including separate HP for each part, the Target/Aim system, and player-configurable Auto rotations. [S1][S2][S7]


===============================================================================
1. CORE MODEL: WHAT A MEDABOT ACTUALLY IS
===============================================================================

A complete Medabot consists of six components:

1. Tinpet
   The mechanical frame/skeleton.

2. Medal
   The control/brain unit. It provides:
   - overall Medal level
   - compatibility/attribute
   - Target/Aim behavior
   - eight skill levels
   - Medaforce abilities

3. Head part
   Usually provides an ability with a finite number of uses per battle.

4. Right-arm part
   Provides an active ability.

5. Left-arm part
   Provides an active ability.

6. Leg part
   Provides the Medabot's movement/defensive/range-related stats and terrain behavior.

Male and female Tinpets exist, and parts are gender-compatible accordingly. Parts can otherwise be freely mixed; a Medabot does not have to use the "official" matching four-part set. Matching a Medal's compatibility attribute is what produces combat bonuses.

This is fundamentally why the game's build system is different from a conventional RPG character sheet: the Medal supplies evolving combat proficiency and behavior while the parts supply most of the concrete hardware and base statistics. [S3][S6]

[SOURCE: S3/S6]


===============================================================================
2. PARTS: THE FOUR BODY SLOTS
===============================================================================

HEAD PART
---------
Head parts have:

- Armor
- Rate of Success (ROS)
- Power
- Uses
- Skill
- Action
- Attribute

Head parts do not display Charge/Radiation in the same way arms do.

Armor:
  HP of the head part. At 0, it breaks.

ROS:
  Contributes to the success/accuracy/critical calculations.

Power:
  Determines the base strength of an attack or non-damage effect.

Uses:
  Number of times that head action can be used during the Robattle.

Important:
  Destroying the Leader's Head immediately ends the Robattle.

At the end of a Robattle, part Armor and head Uses are restored for the next battle. Destroyed parts are not permanently lost merely because they broke during combat. [S3]


ARM PARTS
---------
Right and left arms have:

- Armor
- Rate of Success
- Power
- Charge
- Radiation
- Skill
- Action
- Attribute

Charge (CRG):
  How long it takes the Medabot to move from its side of the arena to the center and execute the selected action.

Radiation (RAD):
  How long it takes to recover after the action, represented by the Medabot returning toward its side of the arena.

Lower CRG/RAD values mean faster cycling.

The older guides note that the right arm is USUALLY faster/less powerful and the left arm USUALLY slower/more powerful, but this is a design tendency rather than a universal mechanical rule. Individual parts determine their actual numbers. [S3]


LEG PARTS
---------
Legs are especially important because their statistics affect the entire Medabot rather than merely being "another HP part."

Leg statistics:

- Armor
- Propulsion
- Evasion
- Defense
- Proximity
- Remoteness
- Leg type / terrain compatibility

PROPULSION
  Affects movement speed during CRG/RAD.
  Also affects Berserk damage and trap-clearing behavior.

EVASION
  Affects whether attacks can be dodged.
  Later community testing also found that Evasion participates in damage reduction calculations, not merely the binary "did it dodge?" check.

DEFENSE
  Affects damage reduction and whether normal Part Defense can activate.

PROXIMITY
  Used by close-range/melee actions and several supportive actions.

REMOTENESS
  Used by ranged actions and several remote/support/disruption actions.

The exact numerical contribution of the leg statistics is discussed later under combat formulas. [S3][S4][S6]


===============================================================================
3. ACTIONS VS SKILLS VS ATTRIBUTES
===============================================================================

These are three DIFFERENT concepts and should not be conflated.

ACTION
------
The actual thing the Medapart does.

Examples:
  Sword
  Hammer
  Missile
  Laser
  Scout
  Defense
  Recovery
  Confusion
  Destroy
  etc.

SKILL
-----
The proficiency category that powers the action.

There are eight active skill categories in Medabots GBA:

1. Strike
2. Berserk
3. Shoot
4. Aim Shot
5. Defend
6. Heal
7. Support
8. Interrupt

The Japanese/Medapedia terminology differs in places:

- Strike = Strike
- Reckless = Berserk
- Shoot = Shoot
- Snipe = Aim Shot
- Protect = Defend
- Heal = Heal
- Support = Support
- Disrupt = Interrupt

The English GBA release uses the terms Berserk, Aim Shot, Defend, and Interrupt. [S2][S6]

ATTRIBUTE
---------
The compatibility category.

Examples:

- Grapple
- Shoot
- Optic
- Bomb/Explosive
- Gravity
- Formation/Set-up
- Movement/Flux
- Stop
- Bind
- Flow/Burn
- Cancel/Release
- Defense
- Heal/Recovery
- Anti-Air
- Anti-Sea
- Scan
- Conceal
- Time
- Interrupt/Disrupt
- Destroy
- Rebirth/Regenerate
- Teamwork/Link
- Counter
- Transform

An attribute is NOT the same thing as the Skill.

Example:
  Rokusho's Pipo Hammer is a Grapple-attribute part.
  Its action is Hammer.
  Its Skill is Berserk.

A Medal compatible with Grapple gains compatibility benefits from that part. [S2][S6]


===============================================================================
4. THE EIGHT SKILLS AND HOW THEY FUNCTION
===============================================================================

STRIKE
------
Close-range attack.

Documented characteristics:
- Quick Grapple-style attack.
- Targets the nearest opponent rather than freely choosing any distant target.
- Medium critical-hit characteristics in later community testing.
- The Medabot cannot normally activate Part Defense during the recovery period after using a melee action until it performs an appropriate non-melee action.

Typical actions:
  Sword
  status-inflicting physical attacks
  Destroy

[S3][S4]

BERSERK
-------
Powerful close-range attack.

Documented characteristics:
- Stronger than ordinary Strike attacks.
- Cannot evade normally after use during the recovery phase.
- Propulsion contributes additional attack Power.
- Standard documented relationship: half of Propulsion is added to Berserk attack Power.
- Commonly associated with Chain Reaction/penetrating destructive attacks.

Later community testing describes the post-Berserk vulnerability as a severe Evasion/Defense weakness during recovery, effectively making attacks against that Medabot much more likely to hit/crit.

Formula component documented by long-running mechanics research:

  Effective Berserk Power
  = Part Power + (Propulsion / 2)

[S3][S4]

SHOOT
-----
Normal ranged attack.

Documented characteristics:
- Ranged attack.
- Generally faster/lower-crit than Aim Shot.
- Does not inherit the special post-action evasion weakness associated with Aim Shot.

Typical actions:
  Rifle
  Gatling / Chain Gun
  Laser
  Beam
  Missile
  Napalm
  Anti-Air
  Anti-Sea
  Sacrifice

[S3][S4]

AIM SHOT
--------
Powerful/precision-oriented ranged attack.

Documented characteristics:
- Ranged attack.
- Has higher critical-hit characteristics than Shoot.
- The user's Medabot suffers a major evasion disadvantage during its recovery period.
- It can make targeted-part attacks especially dangerous because criticals bypass normal defensive redirection.

[S3][S4]

DEFEND
------
Defensive skill.

Typical actions:
  Defense
  Half Block
  Full Block
  traps
  Cross Attack setup
  Counter
  certain Medaforces

Defense actions can protect teammates and/or reduce incoming damage.

[S3][S5]

HEAL
----
Restorative skill.

Typical actions:
  Recovery
  Repair
  Reactivate
  AutoRecover
  Status Clear
  Trap Clear

[S3][S5]

SUPPORT
-------
Buff / acceleration / utility skill.

Typical actions:
  Scout
  Conceal
  Boost Charge
  Rapid Charge
  various stat-enhancing functions

[S3][S5]

INTERRUPT
---------
Disruption/counterplay skill.

Typical actions:
  Disable
  Confusion
  No Escape
  No Defense
  Charge Drain
  Ammo Drain
  Force Drain
  Force Bind
  Pushover
  Transform
  various transform variants

Interrupt parts can attack the opponent's combat process rather than simply subtract HP. [S3][S5]


===============================================================================
5. MEDAL STAT SYSTEM
===============================================================================

Every Medal has:

- Medal Level
- Attribute
- Compatibility Bonus
- Target/Aim
- eight Skill levels
- learned Medaforces
- Medal form/evolution state

MEDAL LEVEL
-----------
The overall Medal level increases through Robattle experience.

It affects combat performance and progression, including:

- base combat capability
- speed
- Evasion/Defense contributions
- Medaforce unlocks
- Medal transformations

Important breakpoints:

Level 10:
  First Medaforce

Level 30:
  Second Medaforce

Level 60:
  Third Medaforce

The older English guides also document a fourth transformation at Level 100 for the Kabuto and Kuwagata starter Medals, without a fourth Medaforce. [S3][S5]

NOTE:
The Fandom table header currently labels the third Medaforce as Lv.50, but its own detailed entries and the longstanding English guides consistently document the third Medaforce at Lv.60. This report therefore uses Lv.60. [S1][S3]


SKILL LEVELS
------------
Each of the eight Skills has its own proficiency level.

Maximum:

  100

Using a part increases the corresponding Skill's progress.

Example:

  Use Sword
    -> +1 Strike-use progress

  Use Pipo Hammer
    -> +1 Berserk-use progress

  Use Scout
    -> +1 Support-use progress

The older guide describes eight uses as one Skill-level increase, after which the usage counter resets and the cycle begins again.

Thus the Medal has a separate proficiency system for:
  Strike
  Berserk
  Shoot
  Aim Shot
  Defend
  Heal
  Support
  Interrupt

Higher Skill proficiency improves the corresponding actions' combat effectiveness. [S3][S6]


===============================================================================
6. COMPATIBILITY / MEDAL ATTRIBUTE
===============================================================================

A Medal's Attribute determines which Medapart attributes it is naturally compatible with.

Each Medal has a compatibility bonus.

When a part matches the Medal's attribute:

  the compatibility contribution is added to the Medabot's combat calculations.

The compatibility bonus contributes to:
- ROS
- Evasion/Defense according to the battle-system research
- effectiveness of many support/heal/Medaforce effects

An important property:

THE BONUS IS TEAM-WIDE WITH RESPECT TO THAT MEDABOT'S PART SET.

The widely documented example is a full four-part Rokusho set on a Kuwagata Medal:

  each part is compatible
  -> the total matching compatibility bonus is applied as a bonus source to the Medabot's relevant calculations.

Changing one part to an incompatible part reduces the total compatibility contribution, but the remaining compatibility contribution still applies to the Medabot rather than being restricted only to the compatible parts. [S3][S4]

This is one of the reasons mixed builds work: an incompatible part can still be made effective by the rest of the build and the Medal's Skill proficiency.


===============================================================================
7. TARGET / AIM SYSTEM = THE GBA'S SIMPLIFIED MEDAL AI
===============================================================================

This is one of the most important differences between original Medarot 2 and 2 Core.

Earlier Medarot games used Medal "personality/nature" systems that could decide things such as:

- favor high-HP opponents
- favor weak opponents
- support allies
- copy another teammate's behavior

Medarot 2 Core simplifies this.

The English game calls the stat:

  AIM

The Japanese concept is:

  Target

The Medal specifies a Skill type that it will preferentially target.

Examples:

  Medal Target = Shoot
    -> when choosing a targetable enemy, it tends to favor parts using Shoot.

  Medal Target = Defend
    -> tends to favor enemy Defend-type parts.

  Medal Target = Heal
    -> tends to favor Heal-type parts.

Therefore the Medal is functioning partly as a target-selection AI modifier.

This is NOT equivalent to giving the Medabot a completely independent AI brain.

It is primarily a targeting priority layered on top of the action chosen for the Medabot. [S2][S5][S6]

IMPORTANT:
Melee actions such as Strike/Berserk operate differently because they select nearby opponents rather than providing the same free target selection as ranged/remote actions.

[S3][S5]


===============================================================================
8. AUTO BATTLE / ROTATION SYSTEM
===============================================================================

The game has two different concepts that are sometimes incorrectly described as the same thing:

1. Medal Target/Aim
2. Auto Rotation

TARGET/AIM
----------
Determines who/what the Medabot prefers to target.

ROTATION
--------
Determines what action the Medabot is told to perform in sequence.

The player can configure a Medal's Rotation from the Medal menu.

Typical entries include:

  H = Head
  R = Right Arm
  L = Left Arm
  MF = Medaforce

The player can build a sequence.

Example:

  H
  R
  L
  R
  L

With Auto enabled, the Medabot cycles through the programmed sequence.

The rotation is action-turn specific.

Example:

Program:
  H -> R -> L

If the player manually uses L first, then turns Auto on, Auto does NOT rewind to H.

It continues from the corresponding point in the action sequence.

Auto can also be interrupted and returned to manual control by rapidly pressing B, except that Confusion prevents normal manual control.

[S3]

Therefore:

MEDAL TARGET = target-selection preference
ROTATION = action-selection script
AUTO = executes the rotation without manual orders


===============================================================================
9. ROBATTLE ARENA MODEL
===============================================================================

A Robattle is not a conventional turn-based RPG battle.

It is better described as:

  asynchronous command selection
  +
  timed movement phases
  +
  action execution
  +
  recovery phases

Your Medabots begin on the left.

Enemy Medabots begin on the right.

When an action is selected:

  CRG phase
    -> Medabot travels toward the center.

  ACTION
    -> attack/ability occurs.

  RAD phase
    -> Medabot recovers and travels back.

The next command can be issued according to the Medabot's battle state.

CRG and RAD numbers therefore directly determine how many useful actions a Medabot can produce over the course of a Robattle. [S3]


===============================================================================
10. ROBATTLE TIMER
===============================================================================

The game uses a configurable battle timer.

The documented battle lengths are:

  20 seconds
  30 seconds
  40 seconds

OR

  the battle ends immediately when a Leader's Head is destroyed.

Important peculiarity:

THE ROBATTLE TIMER DOES NOT SIMPLY COUNT REAL-WORLD SECONDS FROM THE MOMENT THE FIGHT STARTS.

According to the long-standing English guide:

  time counts during the Medabots' movement toward/away from the center
  time does NOT count while the player is selecting a command
  time does NOT count during action animations

This makes Charge/Radiation speed strategically important beyond merely "who attacks first."

A faster Medabot can effectively squeeze more movement/action cycles into the available timed battle window. [S3]


===============================================================================
11. WIN CONDITION / LEADER RULE
===============================================================================

You can field up to three Medabots.

The first selected Medabot is the:

  LEADER

The other two are:

  PARTNERS

Leader status is mechanically critical.

If the Leader's Head Armor reaches 0:

  the Robattle immediately ends.

This applies equally to the enemy.

A Partner can be shut down without immediately ending the Robattle and may potentially be reactivated by a Heal/Reactivate effect.

Therefore the battle is not simply:

  "reduce all enemy HP to zero"

It is structurally:

  protect your Leader's Head
  +
  disable/destroy the enemy Leader's Head
  +
  manage the survivability and usefulness of the remaining partners. [S3]


===============================================================================
12. TIMER EXPIRATION RESULT
===============================================================================

When the Robattle timer expires:

1. The side with more functioning Medabots wins.

2. If both sides have the same number of Medabots, the side with more functioning Medaparts wins.

The old English guide explicitly gives an unresolved hypothetical for further ties, so this report does NOT invent a third-level tie-break rule. [S3]


===============================================================================
13. PART DESTRUCTION
===============================================================================

Every part has independent Armor.

Therefore a Medabot can be:

  mostly destroyed
  but still functional,

or

  missing one or more arms
  while retaining its Head and remaining functions.

A destroyed part becomes unusable for the rest of that battle unless a Heal/Repair/Revive mechanism restores it.

Part destruction is strategically significant because:

- removing an arm disables that action
- removing a Head eliminates that Medabot completely
- removing Legs reduces the entire Medabot's mobility/defense/range statistics
- some Medaforces explicitly destroy specific parts
- Chain Reaction attacks can carry destruction forward

After the Robattle, broken parts are restored automatically. [S3][S5]


===============================================================================
14. LEG DESTRUCTION
===============================================================================

Legs are unusually important because they are the source of:

  Propulsion
  Evasion
  Defense
  Proximity
  Remoteness

Later community testing reports that when the Leg part is destroyed:

  the leg's five principal combat stats are halved

and the resulting loss also affects CRG/RAD movement speed.

Thus a Leg kill is not merely:

  "remove X Armor"

It is also a broad stat-debuff against the whole Medabot.

This makes leg-targeting attacks and Leg Crash Medaforces disproportionately important in long fights.

[COMMUNITY-TESTED: S4]


===============================================================================
15. TERRAIN AND LEG TYPES
===============================================================================

There are seven relevant leg types:

1. Flying / Air
2. Float
3. Multi-Legged
4. Bipedal / Two-Legged
5. Wheeled
6. Tank
7. Aquatic / Sea

Terrain categories correspond to different environmental situations.

DOCUMENTED RELATIONSHIPS:

GREENERY
  Plains / Grasslands
  Forest / Woods

  Best:
    Bipedal / Two-Legged

  Penalized:
    Wheels

MOUNTAIN
  Rock
  Valley

  Best:
    Multi-Legged

  Penalized:
    Wheels

CITY
  Street
  Room / Inside

  Best:
    Wheels

  Penalized:
    Multi-Legged

DESERT
  Wasteland
  Desert

  Best:
    Flying / Air

  Penalized:
    Aquatic / Sea
    Bipedal / Two-Legged

WATER
  Seashore
  Underwater

  Best:
    Aquatic / Sea

  Penalized:
    Flying / Air
    Bipedal / Two-Legged
    Wheels

TANK:
  Generally neutral across fields.

FLOAT:
  Broadly usable across fields and avoids the strong specialization/penalty extremes, although it does not receive the same specialized advantage as the best-matched leg type.

The exact internal numeric terrain modifiers are NOT reliably documented in the sources used here, so no invented "+5/+10" formula is given.

[S3][S4]


===============================================================================
16. PROPULSION
===============================================================================

Propulsion is primarily a leg stat.

It affects:

- CRG speed
- RAD speed
- Berserk Power
- Trap clearing
- movement efficiency

The strongest direct combat formula established by the long-running mechanics research is:

  Berserk effective Power
  =
  Part Power
  +
  (Propulsion / 2)

Propulsion therefore has a unique relationship with Berserk that ordinary Strike attacks do not have.

Later testing also established that Propulsion influences overall movement speed, but the exact movement-speed curve is nonlinear rather than a simple "one Propulsion point = one frame" relationship.

[COMMUNITY-TESTED: S4]


===============================================================================
17. PROXIMITY AND REMOTENESS
===============================================================================

These are leg-derived stats.

PROXIMITY
---------
Added to the effective ROS for actions relying on close range.

Documented associated actions:

- Strike
- Berserk
- Defend
- Heal

REMOTENESS
----------
Added to the effective ROS for actions relying on range.

Documented associated actions:

- Shoot
- Aim Shot
- Support
- Interrupt

The important conceptual model is:

  Close-range action
    -> Proximity matters

  Ranged/remote action
    -> Remoteness matters

This is why simply maximizing the attack part itself is not sufficient for a complete build. Leg selection can materially change the action's reliability/effectiveness.

[S3][S4]


===============================================================================
18. RATE OF SUCCESS (ROS)
===============================================================================

ROS is one of the most important numbers in the game.

It is NOT merely a simple "accuracy percentage."

The long-running battle mechanics research identifies ROS as a major contributor to:

- hit/success probability
- critical-hit probability
- damage/potency above base Power

The effective ROS is built from several components.

The well-established component model is:

  Total ROS =
      Part ROS
    + total matching Compatibility Bonus
    + relevant Medal Skill
    + Proximity OR Remoteness
    + temporary Scout contribution
    + other applicable effects

This model explains why a relatively weak-looking part can become much stronger on an appropriately trained Medal.

[S4]


===============================================================================
19. ROS -> DAMAGE
===============================================================================

This is one of the most heavily researched mechanics in the game.

The long-running gsk6390/GameFAQs testing established that effective ROS contributes additional damage.

The commonly reported approximation is:

  additional damage from ROS
  ≈ Total ROS / 4

or, in integer-game terms, an approximately one-point damage increase for each four effective ROS points.

The same research also established:

  minimum damage from an ordinary damaging part is its effective Power

and for Berserk:

  minimum damage =
    Part Power + Propulsion/2

This means defensive stats can reduce or eliminate the ROS-derived bonus portion of damage without necessarily reducing the attack all the way below its base Power.

Exact flooring/rounding behavior and some branch conditions of the damage routine have not been fully documented from the ROM in the sources used here, so this report does NOT pretend the community equation is a complete source-code-level formula.

[S4]

A later testing thread refined the conceptual model further by describing Power as the base damage/potency and ROS as a "potential" bonus that can be suppressed by defensive stats.

[S4 follow-up discussion]


===============================================================================
20. DEFENSE
===============================================================================

Defense is a whole-Medabot leg-derived stat.

It is NOT a separate defense value attached to each individual body part.

Defense has at least two different mechanical roles:

1. It reduces incoming damage when applicable.

2. It determines whether normal Part Defense can activate.

The old guides describe Defense generally as damage reduction.

Later testing reports a much more precise behavior:

- Part Defense can redirect damage.
- Defense participates in the defensive calculation.
- Normal Part Defense requires sufficient Defense to trigger.
- No Defense status can prevent effective Part Defense.
- Certain low-Defense builds can therefore fail to trigger normal Part Defense.

[COMMUNITY-TESTED: S4]


===============================================================================
21. EVASION
===============================================================================

Evasion determines whether a hit can be dodged.

Not every attack is necessarily dodgeable.

The classic guide description is:

  higher Evasion
  -> better chance to evade attacks that can be evaded.

Later community testing found that Evasion also participates in the incoming-damage calculation.

Thus Evasion has two layers:

  A. "Did the hit miss completely?"
  B. "If the attack connected, how much of the attack's bonus damage survives?"

This explains why Evasion can be useful even when an attack cannot simply be "dodged."

[S3][S4 COMMUNITY TESTING]


===============================================================================
22. CRITICAL HITS
===============================================================================

Critical hits are much more mechanically important than a conventional RPG's random critical.

The early documentation says:

- Strike: mediocre/so-so critical tendency
- Berserk: strong attack with destructive potential
- Aim Shot: high critical tendency
- Shoot: lower critical tendency

Later detailed testing indicates that critical hits are closely tied to the attacker's effective ROS relative to the target's Evasion/Defense.

The later mechanics research describes a threshold-style system:

  attacker offensive potential
      vs.
  defender Evasion + Defense

If the attacker's effective advantage is sufficiently large:

  critical becomes possible/likely

A critical hit:

- bypasses ordinary dodge resolution
- bypasses normal Part Defense
- deals the attack's full effective damage

This means criticals are not adequately modeled as:

  random "20% crit chance"

That simple model is not supported by the later testing.

There also appears to be a small randomized factor in the final resolution, so "critical determination is threshold-based" does NOT mean every mathematically similar attack necessarily behaves identically every single time.

[COMMUNITY-TESTED: S4]


===============================================================================
23. MELEE RECOVERY PENALTIES
===============================================================================

STRIKE
------
After a melee Strike action, the Medabot normally cannot use its ordinary Part Defense state during the vulnerable recovery period.

Later testing describes this as a Part-Defense lock rather than necessarily reducing the raw Defense stat itself.

BERSERK
-------
After Berserk, the Medabot is left with severely weakened defensive behavior during RAD.

Practically:

  Berserk = strong offense + major vulnerability

This is why Berserk is disproportionately dangerous on a Leader.

A Berserk Leader can produce excellent damage but can also expose itself to critical hits at exactly the wrong moment.

[S3][S4]


===============================================================================
24. AIM SHOT RECOVERY PENALTY
===============================================================================

Aim Shot has a corresponding drawback.

Later testing reports that during the Aim Shot recovery period:

  Evasion is severely reduced

The testing describes the reduction as approximately three-quarters of the normal value.

This produces:

  high offensive reliability/critical potential
  +
  very poor post-shot defensive safety

This is one of the central tradeoffs of Aim Shot.

[COMMUNITY-TESTED: S4]

The exact internal implementation should still be treated as a tested behavior rather than a source-code-proven formula.


===============================================================================
25. PART DEFENSE
===============================================================================

Part Defense is distinct from the leg's normal Defense stat.

DEFENSE PART
------------
Protects teammates by intercepting attacks.

The defending Medabot receives the damage instead of the originally targeted ally.

HALF BLOCK
----------
Protects teammates and nullifies attacks below its block threshold, while stronger attacks still damage the defender.

FULL BLOCK
----------
Protects teammates and completely prevents applicable incoming damage while the block is active.

However:

  A Full Block does NOT make its user untouchable when the user itself is directly targeted.

Later testing additionally established that:

- only damaging Medapart attacks are normally intercepted
- utility/status actions and Medaforces bypass ordinary guard interception
- Sacrifice-type attacks bypass normal defensive interception

[COMMUNITY-TESTED: S4]

The English guide also explicitly documents:

  Defense
  Half Block
  Full Block

as separate protective mechanics. [S3]


===============================================================================
26. PART DEFENSE DAMAGE REDIRECTION
===============================================================================

Later community testing reports the following detailed behavior:

When Part Defense activates:

- incoming damage is redirected into the defending Medabot's other parts
- the Head is excluded from normal damage-routing priority
- damage is distributed beginning with high-HP parts
- Defense provides additional damage reduction
- status effects applied by damaging attacks are dramatically shortened if Part Defense intercepted the attack

This matters because the defending Medabot is effectively sacrificing its own parts to protect allies.

[COMMUNITY-TESTED: S4]

Because this is the most detailed published player-testing available rather than a ROM-source-code transcription, the exact routing routine should be treated as "strongly evidenced" rather than absolute source-code fact.


===============================================================================
27. STATUS SYSTEM
===============================================================================

The game contains a large number of status effects.

A useful classification is:

DEBUFFS:
- Bind
- Can't Defend / No Defense
- Can't Evade / No Escape
- Confusion / Chaos
- Flow
- Movement
- Stop
- Useless

POSITIVE / DEFENSIVE STATES:
- AutoRecover
- Time / speed boost
- Defense / Half Block / Full Block
- Counter
- Conceal
- Scout
- status immunity
- trap immunity


BIND
----
Slows CRG/RAD movement.

The classic description is effectively:

  Medabot walks approximately twice as slowly.

This is one of the game's most important timing debuffs because the battle system is itself timing-driven.

[S3]


MOVEMENT
--------
Lowers ROS.

Therefore it affects:

- hit rate
- critical potential
- damage potential
- defensive skill activation indirectly where ROS is necessary

[S3][S4]


STOP
----
Stops the Medabot's movement cycle.

A stopped Medabot is temporarily unable to progress through normal CRG/RAD movement.

Later testing also finds that hitting a stopped Medabot is an excellent opportunity to create a critical because its effective Evasion/Defense situation is severely compromised.

[S3][S4]


FLOW
----
Damage-over-time effect.

The long-standing mechanics research established:

  Flow damage
  =
  approximately half the damage dealt by the attack that applied Flow

This includes the important result that the initial attack's full effective damage matters even if it destroyed the target part.

Example documented by gsk6390:

  attack deals 58 damage
  -> Flow damage becomes 29

If a later Flow attack replaces it with a 30-damage application:

  new Flow damage = 15

So Flow is not simply a fixed class-based damage number.

[S4]


NO DEFENSE
----------
Prevents the affected Medabot from successfully protecting itself/others with ordinary Defense mechanics.

This is particularly powerful because it removes the defensive mechanism that normally absorbs/redirects attacks.

It is also one of the documented ways to make status effects from damaging attacks persist normally instead of being shortened by Part Defense.

[S3][S4]


NO ESCAPE
---------
Prevents the Medabot from evading attacks.

[S3]


CONFUSION / CHAOS
-----------------
This is the closest thing the game has to an explicit "AI corruption" state.

The affected Medabot:

- performs random actions
- can select random targets
- can attack friend or foe

Therefore Confusion interferes with BOTH:

  what action the Medabot performs
  AND
  whom it targets

This is fundamentally different from Medal Aim, which merely biases target selection.

[S3][S5]


USELESS / DISABLE
-----------------
Prevents one specific Medapart from being used.

[S3][S5]


AUTO-RECOVER
------------
Restores Armor over time during CRG/RAD movement.

[S3]


TIME / BOOST
------------
Speeds up movement through CRG/RAD.

The classic guide describes the Medabot as walking approximately twice as fast.

[S3]


COUNTER
-------
Reflects sufficiently powerful incoming attacks.

Weak attacks can still damage the Counter state.

[S3][S5]


===============================================================================
28. STATUS STACKING / DEBUFF SLOT
===============================================================================

Later player testing reports a crucial limitation:

A Medabot can have only one conventional debuff active at a time.

Applying a new debuff replaces the previous debuff.

The tested four damaging status categories include:

  Flow
  Movement
  Bind
  Stop

When these are delivered through ordinary damaging attacks and intercepted by Part Defense, their duration becomes extremely short.

When delivered by:

- a non-damaging status part
- a dedicated Medaforce

the full status duration is retained.

This is why dedicated status Medaforces are dramatically more reliable than trying to apply every debuff through standard attacking arms.

[COMMUNITY-TESTED: S4]


===============================================================================
29. STABILITY / STATUS CLEAR
===============================================================================

The Stability / Status Clear part has two roles:

1. It can function as an active Heal action to clear statuses.

2. As an equipped effect, it grants immunity to status changes.

Likewise Trap Clear has both:

1. active trap removal
2. passive trap immunity

[S3][S5]


===============================================================================
30. TRAPS / FORMATIONS
===============================================================================

The game contains several defensive trap mechanics.

Grap Trap
---------
Hurts enemies using Strike/Berserk.

Shot Trap
---------
Hurts enemies using Shoot/Aim Shot.

Attack Clear
------------
Can prevent/cancel enemy attacks.

Cross Attack Set
----------------
Sets the setup state needed for Cross Attack Fire.

Cross Attack Fire
-----------------
Powerful follow-up attack requiring the setup state.

Later community testing reports:

- only one trap/formation slot can be active at once
- placing a different trap replaces/removes the previous trap
- trap damage is triggered by matching enemy actions
- higher Propulsion reduces how many attacks are required to clear traps
- Cross Attack style teamwork effects occupy the same overall formation space

[COMMUNITY-TESTED: S4]
[DOCUMENTED ACTION DEFINITIONS: S5]


===============================================================================
31. CHAIN REACTION / PIERCE-LIKE DAMAGE
===============================================================================

Some attacks have Chain Reaction / piercing behavior.

The basic effect:

  Attack Part A
       |
       +--> destroys target part
                  |
                  +--> excess/chain damage can continue onto another part

This is particularly important for:

- Hammer
- Missile
- certain Medaforces
- Destroy-style attacks where applicable

The exact chain-routing rules differ by action and are not fully documented in the sources used here, so this report does not invent a universal "always hits legs next" rule for ordinary attacks.

Trap-specific target routing should not be confused with normal Chain Reaction routing. [S3][S5]


===============================================================================
32. SPECIAL ATTACK TYPES
===============================================================================

SWORD
-----
Physical close-range attack.

HAMMER
------
Physical close-range attack.
Often Berserk.
Commonly associated with Chain Reaction.

BUG / VIRUS
-----------
Physical attacks that can apply Movement.

THUNDER / FREEZE
----------------
Physical attacks that can apply Stop.

HOLD / WAVE
-----------
Physical attacks that can apply Bind.

FIRE / MELT
-----------
Physical attacks that can apply Flow.

DESTROY
-------
Special destructive Grapple action.

It completely destroys parts rather than dealing normal damage, but only works under a specific timing condition:

  target must be in its cooldown / RAD phase.

This timing restriction is central to Destroy strategy.

[S5][S4]


===============================================================================
33. RANGED ATTACK TYPES
===============================================================================

RIFLE
------
Standard Shot.

GATLING / CHAIN GUN
-------------------
Standard Shot with its own Power/ROS/CRG/RAD statistics.

LASER
-----
Optical attack.

BEAM
----
Optical attack.

MISSILE
-------
Explosive attack.

NAPALM
------
Explosive attack.

BREAK
-----
Gravity attack.

PRESS
-----
Gravity attack.

ANTI-AIR
--------
Specialized against Flying/Air leg types.

ANTI-SEA
--------
Specialized against Aquatic/Sea leg types.

SACRIFICE
---------
Extremely unusual attack:

  the user's own Medapart is destroyed
  to deliver the attack.

[S5]


===============================================================================
34. OPTIC / GRAVITY / BOMB ATTRIBUTES
===============================================================================

OPTIC
-----
Laser and Beam receive a special Power behavior.

The documented mechanical result is:

  listed Part Power is doubled

Only the part's Power itself is doubled; the other ROS/compatibility/skill contributions are not simply doubled as well.

Example:

  listed Power = 31

  Optic effective base Power = 62

This makes Laser/Beam parts unusually strong once supported by the correct Medal. [S4][S5]


GRAVITY
-------
Break and Press receive the corresponding ROS behavior.

The part's own listed ROS is doubled.

Crucially:

  only the part's own ROS is doubled

not:

  Compatibility Bonus
  Medal Skill
  Proximity
  Remoteness

[S4][S5]


BOMB / EXPLOSIVE
----------------
Missile and Napalm have an important special property:

  they always hit

The later testing also identifies Bomb attacks as gaining Chain Reaction behavior under appropriate conditions.

This gives Bomb attacks a very different tactical role from ordinary accuracy-based attacks.

[S4][S5]


===============================================================================
35. MEDAFORCE SYSTEM
===============================================================================

Every Medal has up to three Medaforces.

They unlock at:

  Level 10
  Level 30
  Level 60

A Medaforce requires:

1. The Medal must have learned it.
2. The Medaforce gauge must contain enough MF.

The full gauge is:

  80 MF

Charging action:

  +40 MF

Taking damage:

  +20 MF

Individual Medaforces consume varying amounts:

  30
  40
  50
  60
  70
  80 MF

An 80-MF Medaforce therefore requires either:

  two charging actions

or

  a combination of charging and damage taken

to reach full capacity.

[S3][S5]


===============================================================================
36. MEDAFORCE DEFENSIVE INTERACTION
===============================================================================

Normal Medaforce attacks bypass ordinary:

- Dodge
- Part Defense
- Guard effects

Status Medaforces are different because they still depend on whether the target can receive that particular status.

Therefore:

  Direct offensive Medaforce
    -> not handled like a normal attack against dodge/Part Defense

  Status Medaforce
    -> status immunity/resistance can prevent its status effect

This is one reason Medaforce attacks can function as hard counters to defensive builds. [S3][S4]


===============================================================================
37. MEDAFORCE POWER FORMULA
===============================================================================

The best-known community-tested formula is:

  Medaforce Result
  =
  Base Medaforce Power
  +
  (Compatibility Bonus / 8)
  +
  (relevant Medal Skill / 8)

For example, the gsk6390 research describes:

  40 Skill
    -> +5 contribution

  100 Skill
    -> +12.5 contribution

before integer handling/rounding.

This formula applies to many damage and support Medaforces.

It is not the same as ordinary attack damage.

[S4]


===============================================================================
38. SCOUT
===============================================================================

Scout / Scan is one of the most influential Support mechanics.

Its function is to raise the effective ROS of the Medabot/team.

The old English guides describe it as:

  increasing Power and ROS

The later community research provides a more precise ROS-oriented model in which Scout increases the effective ROS of parts, and the bonus itself depends on:

- Scout part Power
- Compatibility
- Support Skill
- Remoteness

The research also reports that Scout effects stack across repeated uses.

This means Scout is not:

  "one buff that makes everyone accurate"

It is a scalable offensive-support system whose strength depends on the quality of the Scout part and the Medal powering it.

A commonly reported empirical formula is:

  Scout bonus
  =
    Scout Power
  + Compatibility/4
  + Support Skill/4
  + Remoteness/4

The formula is a community-tested result, not a ROM-source-code transcription.

[S4]


===============================================================================
39. CONCEAL
===============================================================================

Conceal raises the user's effective Evasion.

Its value is therefore twofold:

1. More complete dodges.
2. Lower effective damage when an attack does connect, according to later damage-resolution testing.

Unlike team-wide mobility Medaforces, normal Conceal is generally a self-centered effect.

[S3][S4]


===============================================================================
40. BOOST CHARGE / RAPID CHARGE
===============================================================================

BOOST CHARGE
------------
Speeds CRG/RAD cycling.

RAPID CHARGE
------------
A much more extreme timing manipulation:

  the selected ally's next movement/charge can be immediately accelerated to the next relevant phase.

These actions are therefore effectively "tempo manipulation" tools rather than damage skills.

[S5]


===============================================================================
41. DRAIN CHARGE
===============================================================================

Drain Charge simultaneously:

  slows the target
  speeds the user

It works by applying the Time/Bind-style timing states.

That makes it a tempo swing rather than a pure debuff.

[S3][S5]


===============================================================================
42. FORCE DRAIN / FORCE BIND / AMMO DRAIN
===============================================================================

FORCE DRAIN
-----------
Takes Medaforce from an enemy and gives it to the user.

AMMO DRAIN / USE DRAIN
----------------------
Reduces the enemy's remaining Head Uses while increasing the user's corresponding resource.

FORCE BIND
----------
Seals Medaforce use.

These are especially strong because they attack resources rather than Armor.

[S5]


===============================================================================
43. PUSHOVER
===============================================================================

Pushover is a particularly timing-sensitive Interrupt action.

It:

- erases the enemy's current order
- damages the Head if it hits during the enemy's CRG phase

The Medapedia documentation describes the Medaforce variant as:

  damaging enemies in CRG
  and dealing a minimal amount during RAD

The practical purpose is to punish enemies while they are committed to an attack.

[S3][S4][S5]


===============================================================================
44. TRANSFORM / CHANGE
===============================================================================

Transform parts temporarily become another part and use its action.

Variants include:

- Change
- Attack Change
- Defense Change
- Heal Change
- Interrupt Change

The original part returns afterward.

This allows an otherwise specialized Medabot to access abilities outside its nominal build.

Importantly, the resulting action is still considered an action of the Transform/Interrupt mechanism for game-rule purposes rather than simply becoming a normal permanent replacement part.

[S3][S5]


===============================================================================
45. FULL LIST OF THE 60 DOCUMENTED ACTIONS
===============================================================================

The Medapedia 2 Core action list identifies 60 attacks/actions/effects. [S5]

CLOSE-RANGE / GRAPPLE
1. Sword
2. Hammer
3. Bug
4. Virus
5. Thunder
6. Freeze
7. Hold
8. Wave
9. Fire
10. Melt
11. Destroy

RANGED / SHOT
12. Rifle
13. Gatling / Chain Gun
14. Laser
15. Beam
16. Missile
17. Napalm
18. Break
19. Press
20. Anti-Air
21. Anti-Sea
22. Sacrifice

SUPPORT
23. Scan / Scout
24. Conceal
25. Boost Charge
26. Instant Charge / Rapid Charge

DEFEND
27. Defense
28. Lesser Defense / Half Block
29. Perfect Defense / Full Block
30. Fight Trap / Grap Trap
31. Shoot Trap / Shot Trap
32. Attack Clear / Attack Clr
33. Cross Attack Set / Team Form
34. Cross Attack Fire / Team Attack
35. Counter / Counterattack

HEAL
36. Repair / Recovery
37. Revive / Repair
38. Resurrect / Reactivate
39. Auto-Repair / AutoRecover
40. Status Clear / Stability
41. Trap Clear / Break Form

INTERRUPT
42. Disable / Impair
43. Confuse / Confusion
44. No Dodge / No Escape
45. No Defend / No Defense
46. Charge Drain / Drain Chrg
47. Ammo Drain / Use Drain
48. Force Drain / Forcedrain
49. Force Control / Force Bind
50. Trip / Pushover
51. Transform / Change
52. Transform Attack / AttkChange
53. Transform Defense / DEF Change
54. Transform Recovery / HealChange
55. Transform Disrupt / ItrpChange

PASSIVE/EQUIP EFFECTS
56. Constant Charge / Accel Chrg
57. Negate Optical / CancelOptic
58. Negate Explosive / CancelBomb
59. Negate Gravity / CancelGrav
60. Reinforce / Strengthen

[S5]


===============================================================================
46. PASSIVE EQUIP EFFECTS
===============================================================================

Some parts do not behave like normal manually selected attacks.

CONSTANT CHARGE
  Reduces the user's normal Charge time.

NEGATE OPTICAL
  Prevents damage from Laser/Beam attacks against the user.

NEGATE EXPLOSIVE
  Prevents damage from Missile/Napalm attacks against the user.

NEGATE GRAVITY
  Prevents damage from Break/Press attacks against the user.

REINFORCE
  Raises the Power and ROS of the user's other parts.

STATUS CLEAR
  Gives status immunity while equipped.

TRAP CLEAR
  Gives trap immunity while equipped.

[S5]


===============================================================================
47. MEDAFORCE SPECIAL FORMS
===============================================================================

Several Medals have Medaforces that temporarily alter how their user's entire
part set behaves.

OPTIC FORM
----------
Makes the user's parts function with doubled Optic Power behavior.

BOMB FORM
---------
Gives the user's attacks Explosive behavior, including 100% accuracy/Chain effects
reported by battle testing.

GRAVITY FORM
------------
Doubles the user's part ROS where the Gravity behavior applies.

These are not ordinary permanent changes to the parts.

They are temporary Medaforce-derived modifications.

Later testing reports repeated casts do not simply multiply again indefinitely.

[COMMUNITY-TESTED: S4][DOCUMENTED: S2][S5]


===============================================================================
48. MEDAFORCE UTILITY TYPES
===============================================================================

The Medaforce system contains several broad classes:

DAMAGE
  Spiral Bolt
  Side Bolt
  Ultra Shot
  Damage Ball
  Life Drain
  Shrapnel Attack
  Dice Attack
  etc.

STAT BUFF
  PROX Up
  Remoteness Up
  Propulsion Up
  Mobility Up
  Power Increase
  Iron Wall
  Formation Power Up
  etc.

STATUS
  Movement
  Stop
  Bind
  Flow
  Confusion
  Useless
  etc.

RESOURCE
  Force Drain
  Medaforce Double
  etc.

DEFENSIVE FORM
  Optic Form
  Bomb Form
  Gravity Form
  Cancel Formation
  Absorption effects
  etc.

SPECIAL PART DESTRUCTION
  Destroyer
  Leg Crash
  Structureless
  Type Crash
  etc.

This makes the Medal system a much broader battle-role definition than simply
"which stats the character likes." [S2]


===============================================================================
49. ALL 30 MEDALS: ATTRIBUTE, AIM, AND STARTING SKILLS
===============================================================================

Skill order:
  ST = Strike
  BE = Berserk
  SH = Shoot
  AS = Aim Shot
  DE = Defend
  HE = Heal
  SU = Support
  IN = Interrupt

These are the relative Skill values when acquired, NOT the maximums.

#  Medal       Attribute        Bonus   Aim          ST BE SH AS DE HE SU IN
-- ----------- ----------------- ------ ------------ -- -- -- -- -- -- -- --
A  Kuwagata    Grapple           +4     Shoot        10 10  0  0  6  0  6  0
B  Kabuto      Shoot             +4     Strike        0  0 10 10  6  0  6  0
C  Tortoise    Optic             +7     Defend        6  0 10  6  0  6  0  0
D  Jellyfish   Bomb              +7     Heal          0  0  6 10  0  6  6  0
E  Bear        Gravity           +7     Support       0  6  8  8  6  0  0  0
F  Spider      Formation         +7     Interrupt     4  4  6  6 10  0  0  0
G  Snake       Movement          +7     Defend        8  8  0  0  4  6  4  0
H  Queen       Stop              +7     Heal          8  8  6  6  0  0  0  0
I  Kraken      Bind              +7     Support      10  6  4  0  4  0  6  0
J  Phoenix     Flow              +7     Interrupt     6 10  0  4  6  0  4  0
K  Unicorn     Cancel            +5     Interrupt     6  6  0  0  0 10  0  6
L  Ghost       Negate           +10     Shoot         0  0  0  0  6  6  6 10
M  Knight      Defense           +5     Strike        6  6  0  0 10  0  6  0
N  Mermaid     Recovery          +5     Aim Shot      0  0  0  6  6 10  6  0
O  Penguin     Revival           +5     Berserk       0  0  0  6  6 10  6  6
P  Bat         Anti-Air          +7     Berserk       8  0  8  0  0  0  6  6
Q  Kappa       Anti-Sea          +7     Aim Shot      8  0  8  0  6  6  0  0
R  Mouse       Scan              +6     Interrupt     6  0  0 10  0  0 10  0
S  Chameleon   Conceal          +10     Heal          0 10  6  0  0  0 10  0
T  Rabbit      Time              +7     Defend        0  6 10  0  0  0 10  0
U  Monkey      Interrupt         +8     Support       6  0  6  0  0  0  6 10
V  Devil       Destroy          +10     Berserk       6  6  6  6  0  0  0 10
W  Angel       Rebirth          +10     Aim Shot      0  0  0  0 10 10  0 10
X  Dragon      Teamwork          +7     Shoot         0  0  6  6 10  0  0 10
Y  Ninja       Counter           +7     Strike       10 10  0  0 10  0  0  0
Z  Alien       Transform         +9     Support       0  0  0  0  6  6  6 14
   Cat         None              +0     Defend        6 10  6 10  4  4  4  4
   ?           None              +0     Heal          6  6  6  6  6  6  6  6
   Bottlero    None              +0     Support       6 10  6 10  0  0  6  6
   !           None              +0     Interrupt     6  6  6  6  6  6  6  6

[S2]


===============================================================================
50. ALL 30 MEDALS: MEDAFORCES
===============================================================================

A KUWAGATA
  Lv10  Spiral Bolt       80
  Lv30  Side Bolt         60
  Lv60  PROX Up           40

B KABUTO
  Lv10  Ultra Shot        80
  Lv30  Damage Ball       60
  Lv60  Cancel Formation  30

C TORTOISE
  Lv10  Optic Form        40
  Lv30  Absorb Optic      70
  Lv60  Status Restore    40

D JELLYFISH
  Lv10  Bomb Form         40
  Lv30  Absorb Bomb       70
  Lv60  Remoteness Up     40

E BEAR
  Lv10  Gravity Form      40
  Lv30  Absorb Gravity   70
  Lv60  Leg Crash         70

F SPIDER
  Lv10  Attack Trap       60
  Lv30  Cancel Formation  30
  Lv60  Side Bolt         60

G SNAKE
  Lv10  Movement          50
  Lv30  Cancel Movement   60
  Lv60  Unbreakable Will  50

H QUEEN
  Lv10  Stop              50
  Lv30  Cancel Stop       60
  Lv60  Propulsion Up     40

I KRAKEN / SQUID
  Lv10  Bind              50
  Lv30  Cancel Bind       60
  Lv60  Pushover Attack   60

J PHOENIX
  Lv10  Flow              50
  Lv30  Cancel Flow       60
  Lv60  Anti-Protection   70

K UNICORN
  Lv10  Life Drain        70
  Lv30  Status Restore    40
  Lv60  Useless           50

L GHOST
  Lv10  Full Body Up      40
  Lv30  Full Body RAD     50
  Lv60  Shrapnel Attack   80

M KNIGHT
  Lv10  Iron Wall         40
  Lv30  Power Increase    40
  Lv60  Cancel Stop        60

N MERMAID
  Lv10  Total Recovery    60
  Lv30  Shrapnel Attack   80
  Lv60  Absorb Gravity    70

O PENGUIN
  Lv10  Full Revive       70
  Lv30  Unbreakable Will  50
  Lv60  Absorb Bomb       70

P BAT
  Lv10  Air Clearance     50
  Lv30  Propulsion Up     40
  Lv60  Type Crash        70

Q KAPPA
  Lv10  Sea Clearance     50
  Lv30  Mobility Up       40
  Lv60  Medaforce Double  50

R MOUSE
  Lv10  Ultimate Scan      30
  Lv30  Proximity Up      40
  Lv60  Structureless     70

S CHAMELEON
  Lv10  Ultimate Conceal   30
  Lv30  Remoteness Up     40
  Lv60  Damage Ball        60

T RABBIT
  Lv10  Full Charge        40
  Lv30  Pushover Attack    60
  Lv60  Cancel Bind        60

U MONKEY
  Lv10  Full Confusion     50
  Lv30  Useless            50
  Lv60  Cancel Flow        60

V DEVIL
  Lv10  Full Destroy       70
  Lv30  Structureless     70
  Lv60  Full Body RAD      50

W ANGEL
  Lv10  Crazy Medaforce    60
  Lv30  Medaforce Double   50
  Lv60  Power Increase     40

X DRAGON
  Lv10  Formation Power Up 40
  Lv30  Leg Crash          70
  Lv60  Absorb Optic       70

Y NINJA
  Lv10  Protector          50
  Lv30  Stance Cancel      70
  Lv60  Mobility Up        40

Z ALIEN
  Lv10  Dice Attack        60
  Lv30  Type Crash         70
  Lv60  Cancel Movement    60

CAT
  Lv10  Total Recovery     60
  Lv30  Attack Trap        60
  Lv60  Dice Attack        60

?
  Lv10  Full Revive        70
  Lv30  Full Destroy       70
  Lv60  Protector          50

!
  Lv10  Ultra Shot         80
  Lv30  Full Confusion     50
  Lv60  Life Drain         70

BOTTLERO / BOTRO
  Lv10  Spiral Bolt        80
  Lv30  Crazy Medaforce    60
  Lv60  Stop               50

[S2]


===============================================================================
51. WHAT THE IMPORTANT MEDAFORCES ACTUALLY DO
===============================================================================

SPIRAL BOLT
  Damage to all parts of one enemy.
  Base Power documented as 20 in the detailed mechanics testing.

SIDE BOLT
  Hits one part of every enemy.
  Base Power documented as 30.

PROX UP
  Raises Proximity for the allied side.

ULTRA SHOT
  Combines the Power of the user's Shoot/Aim Shot parts into one attack.
  Targets one enemy.
  Chain damage.
  Base Power component:
      10 + total Power of Shoot/Aim Shot parts.

DAMAGE BALL
  Damage scales from lost HP/damage suffered.
  Chain damage.

CANCEL FORMATION
  Makes the user immune to relevant traps.

OPTIC FORM
  Makes the user's attacking parts use Optic-style double-Power behavior.

ABSORB OPTIC
  Converts applicable Optic hits into healing.

STATUS RESTORE
  Clears statuses from allied Medabots.

BOMB FORM
  Gives Bomb-style accuracy/Chain behavior to applicable attacks.

ABSORB BOMB
  Converts Bomb attacks into healing.

REMOTENESS UP
  Raises allied Remoteness.

GRAVITY FORM
  Gives Gravity-style doubled part ROS behavior.

ABSORB GRAVITY
  Converts Gravity attacks into healing.

LEG CRASH
  Destroys enemy Legs.

ATTACK TRAP
  Sets a trap damaging enemies when they attack.

MOVEMENT
  Applies Movement to all enemies.

CANCEL MOVEMENT
  Makes allies immune to Movement.

STOP
  Applies Stop to all enemies.

CANCEL STOP
  Makes allies immune to Stop.

PROPULSION UP
  Raises allied Propulsion.

BIND
  Applies Bind to all enemies.

CANCEL BIND
  Makes allies immune to Bind.

PUSHOVER ATTACK
  Cancels enemy orders and harms Head during enemy CRG.

FLOW
  Applies Flow damage-over-time to all enemies.

CANCEL FLOW
  Makes allies immune to Flow.

LIFE DRAIN
  Damages one enemy and heals the user for a portion of the damage.

USELESS
  Prevents a part from being used.

FULL BODY UP
  Restores Head Uses for allies.

FULL BODY RAD
  Forces enemies to the start of their RAD cycles.

SHRAPNEL ATTACK
  Damages the user's own parts and deals corresponding damage to an enemy.

IRON WALL
  Raises the user's Defense.

POWER INCREASE
  Raises the user's Power.

TOTAL RECOVERY
  Restores Armor on allied unbroken parts.

FULL REVIVE
  Restores allied broken parts to low Armor.

UNBREAKABLE WILL
  Raises Power according to broken allied parts.

AIR CLEARANCE
  Applies negative status effects to Flying enemies.

SEA CLEARANCE
  Applies negative status effects to Sea enemies.

MEDAFORCE DOUBLE
  Doubles the rate at which allies accumulate Medaforce.

ULTIMATE SCAN
  Raises your Scan level while reducing the enemy's.

STRUCTURELESS
  Destroys enemy Defense parts.

ULTIMATE CONCEAL
  Raises your Conceal state while reducing the enemy side's.

FULL CHARGE
  Manipulates enemy CHG timing.

FULL CONFUSION
  Randomizes enemy action and target selection.

FULL DESTROY
  Instantly destroys one enemy part while the target is in RAD.

CRAZY MEDAFORCE
  Drains enemy MF to 0 and then deals damage based on the amount drained.

FORMATION POWER UP
  Raises Cross Attack strength.

STANCe CANCEL / ANTI-PROTECTION
  Protects allies from Counterattack effects.

PROTECTOR
  Provides a chance for the Defending Medabot to counterattack.

DICE ATTACK
  Damage is determined by a random/die-based result.

TYPE CRASH
  Deals heavy damage to enemies with the same Leg type as the user.

[S2][S4]


===============================================================================
52. IMPORTANT MEDAFORCE FORMULA EXAMPLES
===============================================================================

STANDARD DAMAGE-STYLE MEDAFORCE:

  result
  =
  Base Power
  +
  Compatibility/8
  +
  Medal Skill/8

EXAMPLE:
  Base = 20
  Compatibility = 16
  Skill = 40

  approximate result:
    20 + 2 + 5
    = 27

This illustrates why Medal Skill and compatibility matter even though the
Medaforce itself has a fixed base Power.

[COMMUNITY-TESTED: S4]


ULTRA SHOT:

  Base component
  =
  10
  +
  total Power of Shoot/Aim Shot parts

Then compatibility and the appropriate Medal Skill contribute according to
the Medaforce scaling model.

It therefore directly rewards building a Medabot around ranged-part Power.

[S4]


===============================================================================
53. MEDAL EVOLUTION / TRANSFORMATION
===============================================================================

Medal evolution is not purely cosmetic.

At documented milestones the Medal:

  changes form
  improves battle performance
  unlocks a Medaforce

The commonly documented milestones are:

  Lv10
    first transformation
    first Medaforce

  Lv30
    second transformation
    second Medaforce

  Lv60
    third transformation
    third Medaforce

  Lv100
    additional transformation for Kabuto/Kuwagata starter Medals
    no additional Medaforce

The old guides specifically describe transformed Medals as gaining stronger
combat statistics and improved speed/accuracy/evasion behavior.

[S3][S5]


===============================================================================
54. MEDAL SKILL TRAINING STRATEGY AS A MECHANIC
===============================================================================

Because Skill proficiency improves only through actual use:

  Sword user
    -> naturally levels Strike

  Hammer user
    -> naturally levels Berserk

  Scout user
    -> naturally levels Support

  Shield user
    -> naturally levels Defend

etc.

This produces a feedback loop:

  use skill
    -> Skill levels increase
    -> corresponding action improves
    -> using that action becomes more effective
    -> Medal develops into that role

Unlike games where character XP alone determines attack strength, Medabots has:

  Medal Level
  +
  Skill Level
  +
  Part statistics
  +
  compatibility
  +
  leg statistics

all contributing to the final combat result.

[S3][S6]


===============================================================================
55. WHY "LEVEL 100" DOES NOT MEAN EVERY STAT IS 100
===============================================================================

A Medal has two separate progression dimensions:

OVERALL MEDAL LEVEL
  Determines progression/evolution/Medaforce access and contributes to general
  combat performance.

SKILL LEVEL
  Separate proficiency value from 0-100 for each of the eight skills.

Therefore a Level 100 Medal can still have:

  high Strike
  low Berserk
  medium Shoot
  very high Support
  etc.

The player can create a highly specialized Medal rather than every skill being
automatically maxed.

[S3][S6]


===============================================================================
56. MEDABOT SPEED IS A COMPOSITE RESULT
===============================================================================

There is no single "Speed" stat displayed that simply determines turn order.

Effective CRG/RAD speed depends on:

- Part Charge
- Part Radiation
- Leg type
- terrain compatibility
- Propulsion
- Medal Level
- active timing buffs/debuffs
- some passive effects

The exact speed curve is nonlinear.

Later testing demonstrated that low CRG/RAD differences produce relatively small
frame differences while very high values become dramatically slower.

Therefore:

  CRG 3 vs 6
  is not simply "twice as fast"

and:

  CRG 18 vs 8
  can be vastly more consequential than the raw number difference suggests.

[COMMUNITY-TESTED: S4]


===============================================================================
57. HEAD PART SPEED
===============================================================================

The classic game documentation does not display Charge/Radiation on Head parts.

Later community testing reports that the game's effective internal handling treats
Head actions as approximately equivalent to a fixed Charge/Radiation value of 6.

That means:

  putting a normally slow attack on the Head
  can preserve much of its Power
  while avoiding the normal slow arm CRG/RAD values.

This is one reason some Head weapons can be significantly stronger in practice
than their visible statistics initially suggest.

[COMMUNITY-TESTED: S4]

This should not be mistaken for a documented UI value; it is an inferred/tested
internal behavior.


===============================================================================
58. RIGHT ARM / LEFT ARM / HEAD BUILD IMPLICATION
===============================================================================

Because all three attacking slots share the same Medal/Leg system, the same
Medabot can be designed around:

  three ranged attacks
  three melee attacks
  attack + utility
  support + attack
  defense + attack
  status + attack
  etc.

There is no universal requirement to equip a "matching set."

A very common conceptual pattern is:

  Head
    utility or limited-use high-value effect

  Right Arm
    faster repeatable action

  Left Arm
    stronger/slower action

  Legs
    chosen to support the entire role

But that is a build pattern, not a hard rule. [S3]


===============================================================================
59. RESOURCE ECONOMY DURING A ROBATTLE
===============================================================================

A Medabot is balancing several simultaneous resources:

ARMOR
  Separate HP pools for Head, Arms, Legs.

HEAD USES
  Finite use count for Head.

MEDAFORCE
  0-80 gauge.

TIME
  20/30/40 second Robattle clock.

CRG/RAD
  Determines how quickly actions cycle.

DEFENSIVE STATE
  Part Defense / Counter / Conceal / other active protection.

STATUS SLOT
  Debuffs can alter the entire Medabot's combat cycle.

PART AVAILABILITY
  Broken arms remove options.

This makes the battle system more like a resource-management simulator than a
standard "pick move -> calculate HP -> repeat" RPG.

[S3][S4][S5]


===============================================================================
60. THREE-MEDABOT TEAM DESIGN
===============================================================================

A team can consist of up to three Medabots.

The system naturally supports role specialization:

OFFENSE
  Strike
  Berserk
  Shoot
  Aim Shot

DEFENSE
  Defend
  Counter
  traps

SUSTAIN
  Heal
  Repair
  Revive
  Reactivate

SUPPORT
  Scout
  Conceal
  Boost Charge
  stat buffs

DISRUPTION
  Interrupt
  statuses
  resource drains
  order cancellation

Because all three units act asynchronously, this becomes a synchronization
problem:

  one Medabot attacks
  one protects
  one manipulates the next cycle

rather than three characters simply taking fixed turns.

[S3][S5]


===============================================================================
61. LEADER VS PARTNER BUILD CONSIDERATIONS
===============================================================================

Leader status is mechanically special because:

  Head destroyed
    -> immediate loss

This changes the value of risky offensive mechanics.

For example:

  Berserk
    -> high damage
    -> severe RAD vulnerability

  Aim Shot
    -> high critical potential
    -> severe RAD evasion vulnerability

A non-Leader can theoretically take such risks more safely because the battle does
not automatically end when that Medabot is shut down.

This is a direct consequence of the Leader rule rather than a balance theory
invented for this report.

[S3][S4]


===============================================================================
62. VERSION DIFFERENCES RELEVANT TO BATTLE
===============================================================================

The two principal English GBA versions are:

  Medabots: Metabee
  Medabots: Rokusho

Their core battle engine is effectively the same.

The primary differences are:

- starter Medal
- starter Medabot parts
- version-exclusive Medals
- version-exclusive Medabots/parts/enemies
- some acquisition locations

There are 30 Medals total in the combined GBA game data.

A single playthrough can obtain 20.

Two versions are required for all 30 because of version exclusives.

Kabuto-version exclusives include:
  Kabuto
  Tortoise
  Jellyfish
  Bear
  Spider
  Devil
  Dragon

Kuwagata-version exclusives include:
  Kuwagata
  Snake
  Queen
  Kraken
  Phoenix
  Angel
  Ninja

Some Medals have different acquisition locations between versions, and the
Bottlero Medal requires the complete collection.

[S2]


===============================================================================
63. STARTER MEDABOT EXAMPLES
===============================================================================

ROKUSHO (KWG-1)
---------------
Head:
  Antenna
  Attribute: Grapple
  Skill: Support
  Armor: 50
  ROS: 18
  Power: 42
  Uses: 5
  Action: Scout

Right Arm:
  Chanbara Sword
  Attribute: Grapple
  Skill: Strike
  Armor: 20
  ROS: 32
  Power: 22
  CRG: 3
  RAD: 4
  Action: Sword

Left Arm:
  Pipopeco / Picopeco Hammer
  Attribute: Grapple
  Skill: Berserk
  Armor: 20
  ROS: 11
  Power: 39
  CRG: 4
  RAD: 5
  Action: Hammer

Legs:
  Tatacker
  Attribute: Grapple
  Type: Bipedal
  Armor: 45
  Propulsion: 28
  Evasion: 32
  Defense: 36
  Proximity: 22
  Remoteness: 9

[S8]

METABEE / KBT-1
---------------
The localized English documentation identifies the standard starter set as:

Head:
  Missile

Right Arm:
  Revolver / Rifle-family ranged weapon

Left Arm:
  Submachine Gun / Chain Gun-family ranged weapon

Legs:
  Ochitsuka

The exact display names differ between localization/reference sources, but the
central mechanical distinction is stable:

  Metabee starter design = ranged
  Rokusho starter design = melee

[S3][S9]


===============================================================================
64. THE "AI" MODEL OF AN OPPONENT
===============================================================================

The enemy Medabot behavior should NOT be conceptualized as one giant modern AI
algorithm.

The best-supported model is a layered rules system:

LAYER 1
  Available parts and actions

LAYER 2
  Medal Skill proficiency

LAYER 3
  Medal Target/Aim preference

LAYER 4
  programmed/defined action sequencing
  (Rotation/Auto concept)

LAYER 5
  battle-state restrictions
  - broken parts
  - Head Uses
  - Medaforce gauge
  - statuses
  - timing state
  - defensive state

LAYER 6
  target availability and battle conditions

The player's Medal screen exposes Target and Rotation because these are important
parts of the combat behavior system.

What is NOT reliably documented in the sources used here is an exact complete
pseudo-code dump of the enemy CPU's internal decision tree.

Therefore no fake statement such as:

  "the CPU chooses its move using a 37%/21% weighted AI table"

is justified.

The factual statement is:

  Medal Target influences target selection;
  Rotation/Auto can determine action sequences;
  statuses such as Confusion can replace normal decision-making with random
  action/target selection.

[S2][S3][S5][S6]


===============================================================================
65. CONFUSION IS NOT THE SAME AS MEDAL AIM
===============================================================================

Normal Medal Aim:

  "Prefer this class of target."

Confusion:

  "Normal target/action control is corrupted."

Therefore:

  Aim = deterministic preference layer

  Confusion = randomized behavior layer

This distinction is important when analyzing the game's AI.

[S3][S5]


===============================================================================
66. ATTACK RESOLUTION: PRACTICAL MODEL
===============================================================================

A useful factual approximation of a standard attack's resolution is:

1. Select action.

2. Enter CRG.

3. Determine target according to action type + Medal Target + current state.

4. Enter attack resolution.

5. Build effective offense:
     Part ROS
   + Medal Skill
   + Compatibility
   + Proximity/Remoteness
   + temporary buffs such as Scout
   + attack-specific modifiers.

6. Compare against defensive factors:
   - Evasion
   - Defense
   - active defensive state
   - status effects
   - action-specific modifiers

7. Determine:
   - miss
   - ordinary hit
   - critical
   - special effect/status
   - chain/pierce behavior

8. Apply Power/base effect.

9. Add applicable ROS-derived bonus.

10. Route damage to the resulting part/defender.

11. Enter RAD.

12. Apply RAD-phase effects/status damage.

This is a conceptual model assembled from documented and tested mechanics. It
should not be read as source-code pseudocode because the exact integer routines
and branch ordering are not fully published in the sources used here.

[S3][S4][S5]


===============================================================================
67. WHAT IS ACTUALLY RANDOM
===============================================================================

Randomness exists, but less of the system is purely random than it first appears.

Known/strongly evidenced random elements include:

- some final damage variation
- Dice Attack
- random actions/targets under Confusion
- certain Counter/Protective effects
- some status application outcomes
- some attack-resolution factors

The later mechanics research specifically argues against interpreting critical hits
as a simple independent random percentage.

Therefore:

  not every miss/crit/damage variation
  = "RNG stat"

Many results are driven by deterministic relationships between attacker and
defender stats, with random resolution layered on top.

[S4]


===============================================================================
68. MEDAFORCE / PART ROLE INTERACTION
===============================================================================

One of the game's strongest design characteristics is that Medaforces often reward
a specific Medabot architecture.

Examples:

KABUTO
  Ultra Shot
    -> wants high Power Shoot/Aim Shot parts

KUWAGATA
  Spiral Bolt / Side Bolt
    -> wants strong melee/compatibility/skill investment

TORTOISE
  Optic Form
    -> wants Laser/Beam-style parts

JELLYFISH
  Bomb Form
    -> wants Missile/Napalm

BEAR
  Gravity Form
    -> wants high-ROS Break/Press

SPIDER
  Attack Trap
    -> wants defensive/formation play

MOUSE
  Proximity Up + Scan
    -> wants Support-oriented construction

DEVIL
  Destroy
    -> wants destructive timing play

ANGEL
  Medaforce Double
    -> wants team resource acceleration

This is why the Medal is not merely a stat bonus: it effectively defines a
battle-combat architecture.

[S2][S4]


===============================================================================
69. WHY MIXED PARTS WORK
===============================================================================

A common misunderstanding is:

  "Medal is Shoot, therefore every part has to be Shoot."

That is false.

The game allows mixing.

A Medal gives:

  compatibility bonus
  +
  skill proficiency
  +
  Target behavior
  +
  Medaforce

while each individual part contributes:

  Armor
  Power
  ROS
  CRG
  RAD
  action
  attribute
  skill

Thus a mixed build can deliberately sacrifice perfect compatibility in one slot
in exchange for a superior action.

Example concept:

  Kabuto Medal

  Head:
    Support part

  Right:
    Shoot

  Left:
    Aim Shot

The Shoot/Aim Shot parts receive strong Skill support while the unusual Head may
provide utility.

The system explicitly permits this kind of mixing.

[S3][S6]


===============================================================================
70. IMPORTANT RESOURCE / STAT RELATIONSHIPS
===============================================================================

PART POWER
  Base damage/effect strength.

PART ROS
  Accuracy/critical/damage-potential contributor.

MEDAL SKILL
  Adds skill-specific effectiveness.

COMPATIBILITY
  Adds a cross-part compatibility contribution.

PROXIMITY
  Helps close-range actions and certain nearby support functions.

REMOTENESS
  Helps ranged and remote support/disruption functions.

PROPULSION
  Changes movement speed and Berserk Power.

EVASION
  Determines dodging and contributes to defensive resolution.

DEFENSE
  Enables/strengthens Part Defense and damage reduction.

MEDAL LEVEL
  Improves broad combat performance and progression.

This explains why there is no single "best stat."

[S3][S4][S6]


===============================================================================
71. ADVANCED COMBAT FORMULA STATUS
===============================================================================

FORMULAS WITH STRONG COMMUNITY EVIDENCE:

A) Total ROS

  TotalROS =
      PartROS
    + Compatibility
    + Skill
    + Proximity/Remoteness
    + Scout/other applicable bonuses

B) Berserk Power

  EffectivePower =
      PartPower
    + Propulsion/2

C) ROS damage contribution

  approximately:
    TotalROS / 4

D) Medaforce scaling

  approximately:
    BasePower
    + Compatibility/8
    + Skill/8

E) Flow

  approximately:
    50% of initial damage dealt by the attack that applied Flow

FORMULAS THAT REMAIN INCOMPLETELY DOCUMENTED:

- exact Defense division branch conditions
- exact Medal-Level damage/defense contribution at every level
- exact final randomization factor
- exact critical-threshold implementation
- exact integer rounding sequence
- complete CRG/RAD movement-speed function
- precise terrain modifier numbers
- exact target-selection weighting between preferred and non-preferred parts

This report deliberately does NOT invent these values.

[S4]


===============================================================================
72. ADVANCED DAMAGE MODEL FROM LATER TESTING
===============================================================================

A later follow-up mechanics analysis summarizes the system conceptually as:

  attacker potential offense
  =
    Power
    +
    ROS-derived bonus

  defender potential defense
  =
    Evasion
    +
    Defense
    +
    compatibility/level effects

The effective offensive/defensive difference determines how much bonus damage
survives.

The important practical conclusions from the testing are:

- Power is the guaranteed floor.
- ROS controls accuracy and damage potential.
- High Evasion can suppress offensive bonus.
- Defense contributes to Part Defense and damage reduction.
- Criticals bypass ordinary defensive handling.
- minimum damage does not drop below effective Power.

This is a better model of the system than treating it like:

  Attack - Defense = damage

because the actual game is combining multiple offensive and defensive layers.

[COMMUNITY-TESTED: S4]


===============================================================================
73. WHY LASER, GRAVITY, BOMB, AND MELEE FEEL SO DIFFERENT
===============================================================================

LASER / BEAM
  high base Power
  Power doubles
  often slower
  can be vulnerable to CancelOptic

BREAK / PRESS
  ROS doubles
  high reliability/critical potential
  can be vulnerable to CancelGrav

MISSILE / NAPALM
  effectively unmissable
  Bomb behavior
  can be countered by CancelBomb

STRIKE
  fast
  weaker than Berserk
  moderate critical characteristics
  defensively vulnerable during melee recovery

BERSERK
  highest melee damage potential
  Propulsion bonus
  Chain behavior
  severe RAD vulnerability

AIM SHOT
  high critical potential
  targeted/ranged
  severe RAD evasion vulnerability

SHOOT
  faster and safer ranged option
  lower critical bias

These are deliberate tradeoffs between:

  Power
  accuracy
  critical potential
  speed
  survivability
  counterability.

[S3][S4][S5]


===============================================================================
74. MEDAFORCE COUNTERPLAY
===============================================================================

The game contains a surprisingly systematic set of counters.

OPTIC
  countered by CancelOptic / Absorb Optic

BOMB
  countered by CancelBomb / Absorb Bomb

GRAVITY
  countered by CancelGrav / Absorb Gravity

MOVEMENT
  countered by Cancel Movement

STOP
  countered by Cancel Stop

BIND
  countered by Cancel Bind

FLOW
  countered by Cancel Flow

TRAPS
  countered by Trap Clear / Cancel Formation-type effects

COUNTER
  countered by Stance Cancel / Anti-Protection

DEFENSE
  countered by No Defense / Structureless

HEAD USES
  attacked by Ammo Drain

MEDAFORCE
  attacked by Force Drain / Crazy Medaforce / Force Bind

This demonstrates that the system was designed around interaction rather than
pure numerical power escalation.

[S2][S5]


===============================================================================
75. STATUS + TIMING INTERACTIONS
===============================================================================

Some of the game's strongest interactions emerge because status effects modify
the clock rather than simply damage HP.

BIND
  slows the opponent's cycle.

STOP
  halts the cycle entirely.

TIME / BOOST
  accelerates the user's cycle.

DRAIN CHARGE
  creates simultaneous timing changes.

PUSHOVER
  can erase an action while the enemy is committed to it.

FULL BODY RAD
  resets enemies to their recovery cycle.

DESTROY
  specifically waits for RAD.

Therefore a large portion of Medabots combat is effectively:

  action economy control

rather than:

  HP attrition.

[S3][S4][S5]


===============================================================================
76. DESTROY STRATEGY
===============================================================================

Destroy is mechanically unusual.

It does not care about normal Armor in the same way as a conventional attack.

Instead:

  if the target is in RAD
      -> a qualifying Destroy action can completely destroy a part

This creates a direct relationship between:

  opponent's timing state
  + your own CRG/RAD
  + target selection
  + offensive pressure

A Destroy-focused build is therefore trying to make its opponent enter the exact
state in which Destroy becomes valid.

The Devil Medal's Full Destroy explicitly uses this concept against an enemy in
RAD.

[S2][S4][S5]


===============================================================================
77. WHY THE LEGS ARE A HIGH-VALUE TARGET
===============================================================================

Destroying Legs produces a cascading reduction because the Leg supplies:

  Propulsion
  Evasion
  Defense
  Proximity
  Remoteness

Therefore losing Legs means losing:

  speed
  evasion
  defensive reliability
  melee effectiveness
  ranged effectiveness

Later testing also reports that these statistics are halved upon Leg destruction.

Thus:

  Leg destruction
  != merely 1/4 of the body being gone

It is a whole-Medabot performance collapse.

[S4]

===============================================================================
78. WHY SUPPORT MEDALS CAN BECOME OFFENSIVE
===============================================================================

Support Skills do not necessarily mean "non-damage."

Examples:

  Scout
    -> improves ROS
    -> ROS improves accuracy
    -> ROS improves damage potential
    -> ROS helps critical potential

  Remoteness Up
    -> stronger ranged/support actions

  Proximity Up
    -> stronger melee/support actions

  Medaforce Double
    -> faster access to offensive Medaforces

Therefore a support-oriented Medal can indirectly generate substantial offensive
power.

[S4][S5]


===============================================================================
79. WHY A HIGH-ROS PART CAN OUTPERFORM A HIGH-POWER PART
===============================================================================

Because Power is the floor while ROS contributes:

- hit probability
- critical probability
- extra damage

a high-Power low-ROS weapon is not automatically superior to a lower-Power
high-ROS weapon.

The actual result depends upon:

  enemy Evasion
  enemy Defense
  Medal Skill
  compatibility
  Proximity/Remoteness
  Scout
  action type
  timing state

This is exactly why the game's numbers often look counterintuitive when evaluated
in isolation.

[S4]


===============================================================================
80. WHY COMPATIBILITY BONUSES SCALE BETTER THAN THEY LOOK
===============================================================================

Compatibility affects more than the icon's visible +X.

The same compatibility contribution can feed into:

  attack ROS
  support effectiveness
  Medaforce effectiveness
  defensive values

Thus the benefit of a matching part can propagate through several separate
subsystems.

That is why a modest visible compatibility number can have a larger practical
effect than a casual inspection suggests.

[S3][S4]


===============================================================================
81. WHAT HAPPENS WHEN A PART IS BROKEN
===============================================================================

HEAD BREAK
  Medabot shuts down.
  If Leader -> Robattle ends.

ARM BREAK
  Corresponding action disappears.
  Remaining parts continue functioning.

LEG BREAK
  The Medabot loses a large fraction of its mobility/defensive/range statistics.

DEACTIVATED PARTS
  Can potentially be restored by Heal/Repair/Revive mechanics.

AFTER ROBATTLE
  Broken parts are automatically restored.

[S3][S4][S5]


===============================================================================
82. HEALING IS NOT ONE THING
===============================================================================

The Heal skill contains several distinct mechanics:

RECOVERY
  Restores Armor on existing unbroken parts.

REPAIR / REVIVE
  Restores broken parts.

REACTIVATE
  Brings a shut-down Medabot back into action.

AUTORECOVER
  Applies a periodic healing state.

STATUS CLEAR
  Removes statuses.

TRAP CLEAR
  Removes traps / grants trap immunity.

This is why a "Healer" can be built as:

  Armor healer
  part-repair specialist
  resurrection specialist
  status cleanser
  trap cleanser
  or some combination.

[S5]


===============================================================================
83. IMPORTANT MEDAL-SPECIFIC SPECIALIZATION PATTERNS
===============================================================================

KUWAGATA
  Melee-centric.

KABUTO
  Ranged-centric.

TORTOISE
  Optic.

JELLYFISH
  Bomb.

BEAR
  Gravity.

SPIDER
  Traps/Formations.

SNAKE
  Movement debuffs.

QUEEN
  Stop.

KRAKEN
  Bind.

PHOENIX
  Flow.

UNICORN
  status normalization/cancel.

GHOST
  attack negation / disruption.

KNIGHT
  Defense.

MERMAID
  Healing.

PENGUIN
  Revive.

BAT
  Anti-Air.

KAPPA
  Anti-Sea.

MOUSE
  Scan.

CHAMELEON
  Conceal.

RABBIT
  Time/charge manipulation.

MONKEY
  Disruption.

DEVIL
  Destroy.

ANGEL
  Rebirth/resource utility.

DRAGON
  Teamwork.

NINJA
  Counter.

ALIEN
  Transform.

CAT
  mixed support.

?
  mixed support/special.

!
  balanced/no-attribute generalist.

BOTTLERO
  mixed offensive/special.

These are the game's intended mechanical identities, but the ability to mix parts
means the Medal does not hard-lock the Medabot into that role.

[S2]


===============================================================================
84. VERSION-EXCLUSIVE MEDAL LIST
===============================================================================

KABUTO VERSION ONLY
  Kabuto
  Tortoise
  Jellyfish
  Bear
  Spider
  Devil
  Dragon

KUWAGATA VERSION ONLY
  Kuwagata
  Snake
  Queen
  Kraken
  Phoenix
  Angel
  Ninja

OTHER IMPORTANT EXCLUSIVITY
  Mermaid/Knight locations differ by version.
  Ghost/Unicorn locations differ by version.
  Penguin OR Alien can be obtained from the Fiyun Fortress decision.
  Cat OR ? can be obtained from the corresponding postgame sidequest outcome.
  Bottlero requires the other 29 Medals.

[S2]


===============================================================================
85. TOTAL MEDAL COLLECTION
===============================================================================

Total:
  30 Medals

Obtainable in one playthrough:
  20

Required for all 30:
  both game versions / appropriate transfers or equivalent collection route

This is separate from the number of individual Medabots and parts.

[S2]


===============================================================================
86. TOTAL MEDABOT DATA
===============================================================================

Medarot 2 Core contains:

  120 Medabots

The Medarot database contains the complete part configurations for those bots.

Each Medabot has:

  1 Head
  1 Right Arm
  1 Left Arm
  1 Leg set

Parts are reusable/customizable rather than permanently bound to a single
Medabot frame.

Therefore:

  120 catalogued Medabots
  does NOT mean merely "120 characters."

It is a collection of modular combat hardware configurations that can be
recombined by the player.

[S2][S6]


===============================================================================
87. PART STAT REFERENCE
===============================================================================

HEAD/ARM:
  Attribute
  Skill
  Action
  Armor
  Power
  ROS
  Charge
  Radiation
  Uses (Head only)

LEGS:
  Attribute
  Leg Type
  Armor
  Propulsion
  Evasion
  Defense
  Proximity
  Remoteness

MEDAL:
  Level
  Attribute
  Compatibility Bonus
  Target/Aim
  Skill levels
  Medaforces

This is the complete core stat architecture relevant to Robattles.

[S6]


===============================================================================
88. PRACTICAL BUILD EQUATION
===============================================================================

To evaluate an attacking Medabot, the relevant information is roughly:

PART:
  Power
  ROS
  CRG
  RAD
  Action
  Skill
  Attribute

MEDAL:
  Level
  Skill proficiency
  Compatibility
  Target
  available Medaforces

LEGS:
  Propulsion
  Evasion
  Defense
  Proximity
  Remoteness
  terrain type

BATTLE STATE:
  buffs
  debuffs
  Scout
  Conceal
  defensive state
  current CRG/RAD state
  damaged/broken parts
  Head Uses
  Medaforce

OPPONENT:
  same information.

This is much closer to the real game's architecture than a simplified:

  Attack
  Defense
  Speed

three-stat model.


===============================================================================
89. WHAT THE GAME IS REALLY DOING DURING A "TURN"
===============================================================================

A useful mental model is:

  COMMAND
    |
    v
  TARGET SELECTION
    |
    v
  CRG
    |
    v
  ACTION
    |
    +--> status / trap / resource effect
    |
    +--> hit / miss
    |
    +--> critical / normal
    |
    +--> damage / healing
    |
    +--> part destruction
    |
    v
  RAD
    |
    +--> vulnerable state / attack restrictions
    |
    +--> Flow/AutoRecover/etc.
    |
    v
  READY FOR NEXT COMMAND

And multiple Medabots are doing this concurrently.

That is the central reason the battle system feels like a "real-time/auto-turn" RPG
rather than traditional alternating turns.


===============================================================================
90. WHAT "REAL-TIME" MEANS HERE
===============================================================================

It is NOT an action game in the reflex-control sense.

The player does not manually move Medabots around.

Instead:

  player selects commands
  ->
  game simulates movement/timing
  ->
  Medabot executes action
  ->
  game simulates recovery
  ->
  next command becomes available

Thus the most accurate description is:

  real-time asynchronous command combat

or:

  timed semi-real-time turn system

rather than:

  pure real-time action combat.


===============================================================================
91. WHAT MAKES THE SYSTEM STRATEGIC
===============================================================================

The major strategic axes are:

1. ACTION POWER
   How hard does the part hit?

2. ACTION RELIABILITY
   How much effective ROS does it have?

3. CRITICAL POTENTIAL
   Can it overcome the enemy's defenses?

4. SPEED
   How quickly does it cycle?

5. SURVIVABILITY
   Can it survive its own RAD vulnerability?

6. RESOURCE ECONOMY
   How many Head Uses / MF resources does it have?

7. PART REDUNDANCY
   Can it continue functioning after an arm is broken?

8. LEADER SAFETY
   Can the Head survive?

9. STATUS CONTROL
   Can it slow/disable/stop the opposing machine?

10. COUNTERPLAY
   Does the opponent have Cancel/Absorb/Defense against its primary attack?

11. TERRAIN
   Are the Legs operating in a favorable environment?

12. TEAM SYNCHRONIZATION
   Do the three Medabots' timing cycles complement one another?

This is why an apparently weaker part can outperform a stronger-looking one when
the complete team/state is considered.


===============================================================================
92. HARD FACTS VS COMMON MISCONCEPTIONS
===============================================================================

MISCONCEPTION:
  "It is just Pokémon with robots."

FACT:
  The combat engine is asynchronous, uses individual part HP, independent
  CRG/RAD timing, eight Medal Skills, compatibility, target AI, Leg-derived
  stats, status timing, defensive interception, and Medaforce resources.

MISCONCEPTION:
  "The Medal determines all four parts."

FACT:
  Parts are freely mixable within gender restrictions. Medal compatibility
  changes effectiveness; it does not force a set.

MISCONCEPTION:
  "ROS is just accuracy."

FACT:
  ROS also contributes to critical behavior and damage/potency.

MISCONCEPTION:
  "Defense is just armor."

FACT:
  Leg-derived Defense affects defensive resolution and Part Defense.

MISCONCEPTION:
  "Speed is just Propulsion."

FACT:
  Effective timing depends heavily on CRG/RAD plus Leg/Medal/state factors.

MISCONCEPTION:
  "Critical hits are just random."

FACT:
  Later testing indicates they are strongly tied to offensive/defensive
  threshold relationships.

MISCONCEPTION:
  "Destroy just does huge damage."

FACT:
  Destroy is a special timing-based part-destruction mechanic tied to the
  target being in RAD.

MISCONCEPTION:
  "Confusion only changes targeting."

FACT:
  It can randomize both action and target.

MISCONCEPTION:
  "Auto is an independent AI that invents actions."

FACT:
  Player Auto follows the configured Rotation sequence.

[S2][S3][S4][S5][S6]


===============================================================================
93. KNOWN LIMITATIONS OF THE AVAILABLE RESEARCH
===============================================================================

The battle system is unusually obscure for a GBA RPG.

The strongest public sources are:

- game databases
- old GameFAQs guides
- long-running player mechanics tests
- Medarot/Medapedia documentation
- reverse-engineering notes

But the publicly documented material does NOT provide a complete verified disassembly
of every combat routine.

Therefore these values should NOT be presented as proven until source-code work
confirms them:

- exact crit threshold
- exact damage randomization sequence
- every integer-floor operation
- every Defense-vs-Level branch
- exact CRG/RAD frame function
- exact terrain numeric modifiers
- exact enemy AI weighting
- exact target-selection probability tables
- complete status duration formulas
- exact internal stacking order of every buff/debuff

Where this report includes those areas, it labels them as community-tested or says
that the exact routine remains undocumented.


===============================================================================
94. WHAT WOULD REQUIRE ROM-LEVEL RESEARCH TO FINISH THE SYSTEM
===============================================================================

A complete reverse-engineering project would need to identify:

A. Part data tables
   - Armor
   - ROS
   - Power
   - CRG
   - RAD
   - Uses
   - Skill
   - Attribute
   - action ID

B. Leg data tables
   - Armor
   - Propulsion
   - Evasion
   - Defense
   - Proximity
   - Remoteness
   - terrain modifier

C. Medal tables
   - attribute
   - compatibility
   - target
   - initial Skill values
   - growth
   - level progression
   - Medaforce IDs

D. Battle routines
   - target selection
   - CRG calculation
   - RAD calculation
   - status timing
   - hit resolution
   - critical resolution
   - damage calculation
   - Part Defense
   - Chain Reaction
   - trap handling
   - resource gain

E. CPU decision routines
   - action selection
   - target selection
   - Rotation execution
   - state-dependent behavior

F. Terrain routines
   - exact numerical modifiers

G. Medaforce routines
   - exact scaling
   - stacking
   - state interaction

There is existing reverse-engineering documentation specifically for Medarot 2 Core
showing that the game has separately mapped text/data structures and that the
Japanese/English versions differ in memory organization, which makes a ROM-level
approach feasible in principle. [S7]


===============================================================================
95. MOST IMPORTANT TAKEAWAY: THE GAME'S ACTUAL COMBAT MODEL
===============================================================================

The most accurate high-level model is:

  MEDAL
    =
      role
      + target AI preference
      + skill proficiency
      + compatibility
      + progression
      + Medaforce

  PARTS
    =
      actual actions
      + base Power
      + ROS
      + Armor
      + timing
      + special mechanics

  LEGS
    =
      timing
      + evasion
      + defense
      + melee/ranged modifiers
      + terrain

  BATTLE STATE
    =
      CRG/RAD
      + statuses
      + buffs
      + traps
      + broken parts
      + MF
      + Head Uses
      + defensive state

  TEAM
    =
      three simultaneous state machines
      + Leader failure condition

  TIMER
    =
      external pressure on the entire system

That is why Medabots GBA has substantially more combat depth than its simple
RPG presentation suggests.


===============================================================================
96. CONDENSED "GAME ENGINE" MODEL
===============================================================================

For someone trying to reproduce the system, this is the closest defensible
conceptual specification:

MEDABOT
{
    tinpet_gender,
    medal,
    head,
    right_arm,
    left_arm,
    legs
}

MEDAL
{
    level,
    attribute,
    compatibility_bonus,
    target,
    skills[8],
    medaforces[3],
    transformation_state
}

PART
{
    attribute,
    skill,
    action,
    armor,
    power,
    ros,
    charge,
    radiation,
    uses
}

LEGS
{
    leg_type,
    armor,
    propulsion,
    evasion,
    defense,
    proximity,
    remoteness
}

BATTLE_STATE
{
    current_phase,
    remaining_battle_time,
    selected_action,
    target,
    crg,
    rad,
    statuses,
    buffs,
    traps,
    medaforce,
    head_uses,
    broken_parts,
    defensive_state,
    leader_state
}

ATTACK_PIPELINE
{
    choose_action
    choose_target
    calculate_crg
    execute_action
    calculate_ros
    calculate_defensive_state
    determine_miss_or_hit
    determine_critical
    calculate_damage_or_effect
    resolve_status
    resolve_chain
    resolve_part_destruction
    update_resources
    enter_rad
    resolve_rad_effects
}

This is a faithful high-level representation of the documented/tested mechanics,
not a claim that the original executable literally uses this exact software
architecture.


===============================================================================
97. SOURCE KEY / RESEARCH ANNOTATION
===============================================================================

[S1]
Medabots Wiki / Fandom
"Medabots (GBA)" / "Medabots (GBA)/Medals" / Medaforces / Medabots pages.
Used for:
  - 30-Medal roster
  - Medal attributes
  - Target/Aim
  - Medaforce listings
  - GBA-specific database structure

[S2]
Medapedia
"Medarot 2 Core"
"Medals in Medarot 2 Core"
"Actions in Medarot 2 Core"
"Medarots in Medarot 2 Core"
Used for:
  - 30-Medal table
  - attributes
  - compatibility bonuses
  - Target/Aim
  - initial Skill values
  - all 60 documented actions
  - Medaforce names/effects/costs
  - version exclusives
  - 120-Medarot database

[S3]
GameFAQs
Autocon, "Medabots: Rokusho - Guide and Walkthrough"
Version 1.3, updated 2015.
Used for:
  - Medabot construction
  - part stats
  - Medal pages
  - Skill leveling
  - statuses
  - Robattle flow
  - timer behavior
  - Leader condition
  - Auto/Rotation
  - Medaforce gauge
  - action descriptions
(Alternate GBA walkthrough consulted: Kenshin_Xtreme, "Medabots RPG Walkthrough",
v3.50, 2004 — https://gamefaqs.gamespot.com/gba/915188-medabots-metabee/faqs/24031)

[S4]
GameFAQs discussion / mechanics research
"Info about flow damage?"
and later
"Explanation of game stats/mechanics here"
Used for:
  - effective ROS components
  - ROS->damage contribution
  - Berserk + Propulsion
  - Flow damage behavior
  - critical/defensive research
  - Scout formula
  - Medaforce formula
  - Optic/Gravity/Bomb behavior
  - Leg-stat behavior
  - Part Defense testing
  - status stacking
  - later refinements to the damage model
IMPORTANT:
  This is community testing, not presented as ROM-source-code proof.

[S5]
Medapedia
"Stats"
Used for:
  - formal definition of Medal/Part/Leg statistics
  - Skill categories
  - compatibility
  - Target/Aim
  - Charge/Radiation
  - Uses
  - Propulsion
  - Evasion
  - Defense
  - Proximity
  - Remoteness
(https://medarot.meowcorp.us/wiki/Stats)

[S6]
Medapedia
"Template:Stats-M2C"
and related 2 Core stat references.
Used for:
  - exact 2 Core part-stat schema
  - attribute/skill/action relationships

[S7]
Medapedia
"Kimbles' Medarot 2 Core Hacking Notes"
Used for:
  - ROM/data-structure context
  - Japanese vs English memory/layout differences
  - confirmation that 2 Core is the GBA remake of Medarot 2

[S8]
Medapedia
"Rokusho (KWG-1)"
Used for:
  - concrete starter Medabot stats
(https://medarot.meowcorp.us/wiki/Rokusho_(KWG-1))

[S9]
Localized English game documentation for the Metabee starter set
(part names as rendered in the English GBA release).


===============================================================================
98. FINAL FACTUAL SUMMARY
===============================================================================

Medabots GBA is an RPG wrapped around a modular asynchronous combat engine.

The core unit is not a conventional character with a few stats.

Instead:

  Medal
    controls progression, proficiency, targeting, compatibility, Medaforce

  Parts
    control the actual attacks/abilities and their base statistical behavior

  Legs
    control movement, defense, evasion, melee/ranged modifiers, and terrain

  Battle state
    controls timing, statuses, traps, resources, part availability and
    vulnerability

  Team
    controls Leader protection and three-unit synchronization

  Timer
    creates a finite combat-action economy

The most important mechanical interactions are:

  Part Power
  +
  Part ROS
  +
  Medal Skill
  +
  Compatibility
  +
  Proximity/Remoteness
  +
  Propulsion
  +
  Evasion
  +
  Defense
  +
  timing state
  +
  status state
  +
  target behavior
  +
  Medaforce
  +
  terrain.

The battle system therefore cannot be accurately reduced to:

  Attack > Defense > HP

A much closer description is:

  modular hardware
  +
  evolving proficiency
  +
  target-selection AI
  +
  asynchronous timing
  +
  deterministic stat interactions
  +
  selective randomness
  +
  defensive interception
  +
  part-level destruction
  +
  status/resource control.

The remaining major unknowns are not basic game rules; they are the exact
low-level formulas and CPU routines. Those can be investigated further through
ROM disassembly/testing, but where the public research does not establish them,
this report intentionally leaves them unresolved instead of inventing values.

END OF REPORT
