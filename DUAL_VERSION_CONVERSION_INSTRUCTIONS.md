# Dual-Version Conversion Instructions

## What You're Doing

Converting recipe files (and `back_matter/99_closing.md`) to support two compiled versions of the book -- vulgar (HOMIE voice with profanity) and clean (kid-friendly, still conversational) -- using inline markers processed by `compile_book.py`.

## Marker Syntax

**Inline** (words/short phrases):
```
This is {{v: fucking critical | seriously critical }} and you should {{v: not half-ass it | not skip it }}.
```

**Block** (rare, for entire paragraphs that differ):
```
{{v:start}}
Vulgar-only paragraph here.
{{v:end}}
{{c:start}}
Clean-only paragraph here.
{{c:end}}
```

## What Gets Wrapped in Markers

1. **Profanity** -- fuck, shit, damn, hell, ass, bastard, goddamn, batshit, dipshit, dumbass, etc. This is the primary target.
2. **Casual addresses** -- homie, dude, chief, slugger, tiger, ace, dawg, kemosabe, buckaroo, hotshot, champ, cowboy, my guy. Clean alternatives: friend, pal, buddy.
3. **Vulgar idioms** -- "shitting the bed," "half-ass," "tastes like ass," "like a dumbass," "weird-ass," "fake-ass," etc.

## What Does NOT Get Wrapped

- Technical content, measurements, temperatures, instructions
- Cultural context and history
- Non-profane casual language ("nerd," "degenerate," "gremlin" are fine without markers unless paired with profanity)
- Words that look like matches but aren't profanity ("class," "pass," "hassle," "bastardizing," "Hass avocados")

## Clean Version Guidelines

- Must still sound **conversational and casual** -- not formal or sanitized
- Replace profanity with natural-sounding alternatives, not euphemisms
- "fucking incredible" -> "seriously incredible" or "absolutely incredible" (not "freaking incredible")
- "hell" -> "beyond belief," "enormously," or restructure the sentence
- Addresses like "homie" -> "friend" or "pal" (not "buddy" every time -- vary it)
- The clean version should read like it was *written* clean, not like profanity was find-and-replaced out

## Process Per File

1. **Read the file** completely
2. **Identify all profanity, vulgar idioms, and casual addresses** -- scan carefully, they're scattered throughout including in headings, bold text, parentheticals, and Notes sections
3. **Add `{{v: vulgar | clean }}` markers** around each instance
4. **Verify the clean alternative reads naturally** in context -- read the sentence with just the clean version to check flow
5. **Do NOT change anything else** -- no rewriting, no added content, no removed content, no reformatting. The only change should be wrapping existing text in markers.
6. **Compile both versions**: `python compile_book.py`
7. **Validate the clean version** is profanity-free for the converted file: `grep -inE '\bfuck|\bshit\b|\bdamn\b|\bhell\b|\bgoddam|\bbastard|\bdipshit|\bdumbass|\bjackass|\bhalf-ass|\bbatshit' Ice_Cream_to_Fight_Over_COMPLETE_CLEAN.md`
8. **Commit** with a message like: `Convert [recipe name] to dual-version markers`
9. **Push** to the assigned branch
10. **Create a PR** and provide the link to the user

## Typical Marker Count

- A typical recipe has **8-20 markers** (3-5 profanities + 2-4 addresses + assorted vulgar idioms)
- Shorter files like `back_matter/99_closing.md` may have only 3-5

## Reference Examples

For examples of well-converted files, look at:
- `recipes/13_atole_de_anis.md` (clean, moderate marker count)
- `recipes/17_brown_butter_pecan.md` (heavy profanity, lots of markers)
- `front_matter/07_custard_fundamentals.md` (longest file, ~20 markers)
- `front_matter/04_how_to_use.md` (short file, dense profanity)

## Files Still Needing Conversion

**Recipes:** 02, 03, 04, 05, 06, 07, 08, 11, 12, 14, 15, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28

**Back matter:** `back_matter/99_closing.md`

Batch 3-5 files per session to keep context manageable.
