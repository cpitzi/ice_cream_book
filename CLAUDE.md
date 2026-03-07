# CLAUDE.md - AI Assistant Guide for Ice Cream to Fight Over

**Last Updated:** 2026-03-07
**Repository:** ice_cream_book
**Project Type:** Modular Markdown-based Cookbook

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Repository Structure](#repository-structure)
3. [Content Organization](#content-organization)
4. [Development Workflow](#development-workflow)
5. [Git Workflow](#git-workflow)
6. [Build & Compilation](#build--compilation)
7. [Style Guide Essentials](#style-guide-essentials)
8. [The HOMIE Voice](#the-homie-voice)
9. [AI Assistant Guidelines](#ai-assistant-guidelines)
10. [Common Tasks & Commands](#common-tasks--commands)
11. [Quality Assurance Checklist](#quality-assurance-checklist)
12. [Technical Specifications](#technical-specifications)

---

## Project Overview

### What This Is

**"Ice Cream to Fight Over: 27 Recipes You'll Fuck Up At Least Once"** is a professionally-written cookbook featuring sophisticated international ice cream recipes with detailed cultural context, technique instruction, and a distinctive conversational voice.

**Key Characteristics:**
- 27 complete ice cream recipes spanning international cuisines
- Modular file structure optimized for version control and collaborative editing
- Comprehensive style guide with strict formatting and voice requirements
- Plain text markdown only (NO emojis, symbols, or decorative Unicode)
- Professional-quality content with casual, educational "HOMIE voice"
- Four-tier difficulty system (CHILL → LEGIT → THE REAL DEAL → A FUCKING ORDEAL)

**Target Audience:** Home cooks with basic ice cream experience seeking challenging, international flavors with cultural context and detailed instruction.

**Project Maturity:** Fully developed with established conventions, comprehensive documentation, and production-ready content.

---

## Repository Structure

```
ice_cream_book/
├── .git/                          # Git repository
├── front_matter/                  # Book introduction (9 files, ~31KB)
│   ├── 01_table_of_contents.md
│   ├── 02_title_and_intro.md
│   ├── 03_what_makes_different.md
│   ├── 04_philosophy.md
│   ├── 05_how_to_use.md
│   ├── 06_difficulty_ratings.md
│   ├── 07_the_flavors.md
│   ├── 08_custard_fundamentals.md
│   └── 09_final_thoughts.md
├── recipes/                       # Individual recipes (27 files, ~325KB)
│   ├── 01_cardamom_pistachio_kulfi.md
│   ├── 02_vietnamese_avocado.md
│   ├── ... (27 total)
│   ├── 27_new_orleans_chicory_beignet.md
│   └── re.sh                      # Recipe renumbering utility
├── back_matter/                   # Closing content (1 file, ~4KB)
│   └── 99_closing.md
├── Ice_Cream_to_Fight_Over_COMPLETE.md  # Compiled output (~345KB)
├── README.md                      # Workflow documentation
├── STYLE_GUIDE.md                 # Comprehensive style guide (515 lines)
├── CLAUDE.md                      # This file
├── EXAMPLE_front_matter_01_title_and_intro.md
├── EXAMPLE_recipe_02_chili_mango.md
├── compile_book.py                # Python compilation script
└── compile_book.sh                # Bash compilation script
```

### Directory Purposes

| Directory | Purpose | Files | Size |
|-----------|---------|-------|------|
| `front_matter/` | Book introduction, TOC, philosophy, fundamentals | 9 numbered files | 31KB |
| `recipes/` | Individual recipe files | 27 numbered files | 325KB |
| `back_matter/` | Closing remarks | 1 file | 4KB |
| Root | Build scripts, documentation, compiled output | 7 files | ~355KB |

---

## Content Organization

### Modular Design Philosophy

The project uses a **modular-first approach** for several critical reasons:

1. **Version Control Granularity:** Individual file changes tracked separately
2. **AI Assistant Optimization:** Specific files loaded without entire 345KB document
3. **Collaborative Editing:** Multiple people can work on different recipes simultaneously
4. **Flexible Reorganization:** Recipe order changed by renumbering files
5. **Token Efficiency:** Each recipe file is 7-18KB (well within context limits)

### File Naming Conventions

**Front Matter:** `##_descriptive_name.md`
- Zero-padded numbers (01, 02, etc.)
- Numbered for sequential order
- Lowercase with underscores for spaces

**Recipes:** `##_recipe_name.md`
- Zero-padded numbers (01-27)
- Currently ordered by difficulty
- Lowercase with underscores
- **Never include nationality in filename** (use regions, cities, or dish names)

**Back Matter:** `99_*.md`
- High number to sort last alphabetically

### Recipe Organization (Current Order)

Recipes are numbered 01-27 in difficulty-based order:
- **01-03:** CHILL difficulty
- **04-16:** LEGIT difficulty
- **17-25:** THE REAL DEAL difficulty
- **26-27:** A FUCKING ORDEAL difficulty

**Note:** Recipe order can be changed by renumbering files and recompiling.

---

## Development Workflow

### Editing Individual Files

**Preferred Approach:**
```
Request: "Edit recipes/08_miso_matcha.md"
Action: Load specific file, make changes, save
```

**Avoid:**
```
Request: "Edit Recipe 8" or "Fix the miso recipe"
Better: Use exact filename with path
```

### Adding New Content

**New Recipe:**
```
1. Create recipes/##_recipe_name.md
2. Follow STYLE_GUIDE.md structure exactly
3. Include all required sections (see Recipe Structure below)
4. Test compilation
5. Commit with descriptive message
```

**Modifying Front Matter:**
```
1. Edit specific file: front_matter/##_section_name.md
2. Verify consistent voice with other front matter
3. Test compilation
4. Commit
```

### Workflow Steps

1. **Identify target file** by exact path
2. **Read file** to understand current state
3. **Make changes** following style guide
4. **Save file** with proper encoding (UTF-8)
5. **Test compilation** (optional but recommended)
6. **Commit changes** with descriptive message
7. **Push to branch** (if working in git workflow)

---

## Git Workflow

### Current Branch

**Active Branch:** `claude/claude-md-mi6fyi978ce21pnr-019jNus9dKds9SXH4hMkodJQ`

**Remote:** `http://local_proxy@127.0.0.1:58280/git/cpitzi/ice_cream_book`

### Branching Strategy

**Development branches:**
- All development occurs on Claude-specific feature branches
- Branch naming: `claude/claude-md-*` with session ID
- Never push to main/master without explicit permission

### Commit Message Style

**Format:** Imperative mood, concise, descriptive

**Good Examples:**
- `Update difficulty rating for pawpaw recipe`
- `Fix typo in custard fundamentals`
- `Add note about candied ginger storage to sichuan plum`
- `Recompile book after recipe edits`
- `Adjust matcha ratio in miso matcha recipe`

**Bad Examples:**
- `Updated stuff` (too vague)
- `Fixed things in Recipe 8` (use filename)
- `WIP` (not descriptive)
- `asdf` (meaningless)

### Git Commands

**Individual file editing:**
```bash
git add recipes/08_miso_matcha.md
git commit -m "Adjusted matcha ratio in miso matcha recipe"
git push -u origin claude/claude-md-mi6fyi978ce21pnr-019jNus9dKds9SXH4hMkodJQ
```

**After compilation:**
```bash
python compile_book.py
git add Ice_Cream_to_Fight_Over_COMPLETE.md
git commit -m "Recompile book with latest changes"
git push -u origin claude/claude-md-mi6fyi978ce21pnr-019jNus9dKds9SXH4hMkodJQ
```

**Push retry logic:**
- Always use `git push -u origin <branch-name>`
- Branch must start with `claude/` and match session ID
- If network errors occur, retry up to 4 times with exponential backoff (2s, 4s, 8s, 16s)

### Optional: Exclude Compiled File

Add to `.gitignore` if you want to track only source files:
```
Ice_Cream_to_Fight_Over_COMPLETE.md
```

---

## Build & Compilation

### Compilation Scripts

**Python (Preferred):**
```bash
python compile_book.py                  # compile both versions (default)
python compile_book.py --version vulgar # vulgar version only
python compile_book.py --version clean  # clean/kid-friendly version only
```

**Bash (Alternative -- does NOT support dual versions):**
```bash
chmod +x compile_book.sh
./compile_book.sh
```

**Output files:**
- `Ice_Cream_to_Fight_Over_COMPLETE.md` (vulgar/HOMIE voice)
- `Ice_Cream_to_Fight_Over_COMPLETE_CLEAN.md` (clean/kid-friendly voice)

### Dual-Version System

The book supports two versions compiled from a **single set of source files** using inline markers. The vulgar version uses the full HOMIE voice with profanity; the clean version replaces profanity with kid-friendly alternatives while keeping the same casual, conversational tone.

**Inline swap marker** -- for words or short phrases:
```markdown
This step is {{v: fucking critical | seriously critical }} and you
should {{v: not half-ass it | not skip it }}.
```

**Block markers** -- for longer passages that differ significantly:
```markdown
{{v:start}}
Vulgar-only paragraph goes here.
{{v:end}}
{{c:start}}
Clean-only paragraph goes here.
{{c:end}}
```

**Rules for markers:**
- First value (before `|`) = vulgar, second = clean
- Keep both variants natural-sounding -- the clean version should still feel conversational
- Markers can appear anywhere in the markdown (titles, paragraphs, notes, etc.)
- Files without markers compile identically for both versions
- Typical recipe has ~8-15 markers (profanity + casual addresses)
- Block markers (`{{v:start}}`/`{{c:start}}`) are for rare cases where entire paragraphs differ

**Migration status:** All source files have been converted. Any file without markers compiles identically for both versions.

### Compilation Behavior

1. **Auto-discovery:** Finds all `.md` files in each directory
2. **Alphabetical order:** Sorts files naturally by filename
3. **Concatenation:** Joins sections with `\n\n---\n\n` separator
4. **Marker resolution:** Processes `{{v: ... | ... }}` and block markers per version
5. **UTF-8 encoding:** Preserves proper character encoding
6. **Statistics:** Reports file counts and total character count

### No External Dependencies

- Python script uses only standard library (`os`, `pathlib`, `re`, `argparse`)
- Bash script uses only standard utilities
- No package managers (npm, pip, etc.)
- No build configuration files
- No version requirements

---

## Style Guide Essentials

### CRITICAL: Text-Only Content

**This is non-negotiable and the #1 rule:**

**PROHIBITED:**
- ❌ Emojis (they corrupt files and display inconsistently)
- ❌ Special symbols (checkmarks, arrows, decorative bullets)
- ❌ Decorative characters or Unicode art
- ❌ Any non-standard text characters

**ALLOWED:**
- ✅ Em dashes (—) for interrupting thoughts
- ✅ Degree symbol (°F) for temperatures
- ✅ Accent marks (café, mála) with proper UTF-8
- ✅ Foreign characters with correct Unicode
- ✅ Standard punctuation only

**Test:** Can you copy-paste into plain text editor without corruption? If yes, it's acceptable.

**If you see corrupted encoding** (`â€"` or `Ã©`), fix immediately.

### Recipe Structure (Required)

Every recipe must follow this exact structure:

```markdown
# Recipe Name
*Tagline (italicized)*

**Difficulty:** [RATING] - [Paragraph explanation in HOMIE voice]
**Total Time:** [X-Y hours] ([Parenthetical about time breakdown])

[Opening paragraph(s) with context/warnings]

## Ingredients

**Component Name:**
- Ingredient with amount
- Another ingredient

## Instructions

**Component Name (with timing if relevant):**

Instruction paragraphs in prose form (not numbered steps).

Another paragraph if needed.

## Notes

**Note Title:**
Content explaining sourcing, technique, cultural context, etc.

**Cultural Context:** (for international recipes)
**Sourcing Guidance:** (where applicable)
**Technique Deep-Dives:** (if relevant)
**Make-Ahead Guidance:** (if multi-component)
**Allergen Information:** (nuts, wheat, soy only - NOT milk/eggs)
**What it Tastes Like:** (ALWAYS final note)
```

### Required Elements Checklist

Every recipe MUST have:

- [ ] Clean title (plain text, no emojis/symbols, no nationalities)
- [ ] Italicized tagline
- [ ] Difficulty rating with HOMIE-style explanation paragraph
- [ ] Total time with funny parenthetical
- [ ] Opening paragraph(s) with context/warnings
- [ ] Grouped ingredient lists with bold headers
- [ ] Instruction sections with bold component headers
- [ ] Notes section with bold note titles
- [ ] Cultural context note (for international recipes)
- [ ] "What it tastes like" as final note
- [ ] Allergen information (if contains nuts/wheat/soy)
- [ ] Make-ahead guidance (if components can be prepped ahead)
- [ ] Proper UTF-8 encoding (no corrupted characters)
- [ ] HOMIE voice throughout (3-5 profanities, casual address)
- [ ] 2-4 teaching moments
- [ ] NO non-text characters anywhere

### Difficulty System

**CHILL:**
- No custard anxiety
- Minimal technique
- Almost no opportunity for catastrophic failure
- Examples: Bơ Chanh, basic blends

**LEGIT:**
- Multiple components
- Sustained attention required
- Solid fundamentals needed
- Most recipes fall here

**THE REAL DEAL:**
- Narrow margins for error
- Techniques that can go wrong in seconds
- Expect to fuck something up at least once
- Examples: Brown butter recipes, candy work

**A FUCKING ORDEAL:**
- Extreme sourcing difficulty
- Professional techniques
- Multi-day commitment
- Genuine insanity
- Examples: Pawpaw Maple (limited availability), Chicory Beignet (complexity)

---

## The HOMIE Voice

### Core Elements

The HOMIE voice is what makes this cookbook distinctive. It's **casual, educational, self-deprecating, and genuinely helpful**—like a smart friend who's already made all the mistakes teaching you what actually works.

**Key Components:**

1. **Casual Address** (2-4 times per recipe)
   - homie, dude, friendo, buddy, dawg, friend, pal, chief, boss
   - Example: "Listen, chief—this timing matters."

2. **Conversational Asides** (in parentheses)
   - "(Ask me how I know. Actually, don't.)"
   - "(You'll thank me later.)"
   - "(This is a hill I will die on.)"

3. **Collaborative Framing**
   - "We're in this together" not "You're doing this alone"
   - "Let's fuck this up and learn something"
   - "We've all been there"

4. **Strategic Profanity** (3-5 per recipe)
   - Words: shit, damn, fuck, hell, ass
   - Use for **emphasis**, not decoration
   - "This step is fucking critical" > "This is pretty important"
   - Don't force it—if unnatural, skip it

5. **Emphasis Techniques**
   - **ALL CAPS** for critical points: "Do NOT skip this step"
   - *Italics* for stress: "The *timing* here matters"
   - Sentence fragments. For impact.
   - Start with And/But/So when natural

6. **Anticipate Reader Experience**
   - "I know you want to stir. Don't."
   - "You'll spend ten minutes staring wondering if it's ready"
   - "Yes, it's supposed to be that yellow"
   - "Fair warning—this burns FAST"

7. **Self-Deprecation** (process, never reader)
   - "This will take forever"
   - "You'll definitely burn the first batch"
   - "I've burned this three times"
   - **NEVER:** "You'll probably mess this up because you're careless"

8. **Technical Accuracy**
   - Never sacrifice accuracy for humor
   - Explain "why" in relatable terms
   - Real-world comparisons: "color of good bourbon"

### What HOMIE Voice Is NOT

- ❌ Mean-spirited or putting down alternatives
- ❌ Fake enthusiasm or forced positivity
- ❌ Losing clarity for the sake of humor
- ❌ Bragging or showing off
- ❌ Unexplained jargon
- ❌ More than 5-6 profanities per recipe (becomes forced)

### Voice Examples

**TOO FORMAL:**
> "One should ensure the mixture reaches the appropriate temperature before proceeding."

**HOMIE VOICE:**
> "Get this to 175°F, homie. No shortcuts."

---

**TOO APOLOGETIC:**
> "Sorry, but this is really important and you need to pay attention to it."

**HOMIE VOICE:**
> "This step is fucking important—don't space out now."

---

**CORPORATE MANUAL:**
> "Monitor the temperature carefully to prevent overcooking."

**HOMIE VOICE:**
> "Watch this like a hawk. It goes from perfect to scrambled in about 5 seconds."

---

## AI Assistant Guidelines

### When Working on This Repository

1. **Always read the STYLE_GUIDE.md first** when making content changes
2. **Use exact file paths** when requesting edits: `recipes/08_miso_matcha.md`
3. **Preserve HOMIE voice** in all content modifications
4. **Never add emojis or decorative symbols** under any circumstance
5. **Verify UTF-8 encoding** is correct (no corrupted characters)
6. **Check all required elements** are present before completing edits
7. **Test compilation** after significant changes (optional but recommended)
8. **Write descriptive commit messages** in imperative mood
9. **Run a consistency check when renaming** - When renaming a recipe or any key term, ALWAYS grep the entire repo for the old name before committing. Recipe names appear in multiple places: the recipe file itself, `front_matter/07_the_flavors.md`, `STYLE_GUIDE.md`, `CLAUDE.md`, and possibly other documentation. Use `grep -r "OldName" .` to find all references.

### Dual-Version Markers

When editing content that contains profanity or version-specific language, use inline markers:
- **Inline:** `{{v: vulgar text | clean text }}` for words/phrases
- **Block:** `{{v:start}}...{{v:end}}` / `{{c:start}}...{{c:end}}` for paragraphs
- Both variants must read naturally -- the clean version should still be conversational
- Wrap profanity, casual addresses ("homie" vs "friend"), and vulgar idioms
- Do NOT wrap technical content, cultural context, or recipe instructions that are identical in both versions

### Content Modification Rules

**DO:**
- ✅ Maintain conversational, casual tone
- ✅ Include 3-5 strategic profanities per recipe (wrapped in `{{v: ... | ... }}` markers)
- ✅ Use "homie/dude/chief/buddy" 2-4 times per recipe (wrapped in markers)
- ✅ Provide cultural context for international recipes
- ✅ Explain techniques with teaching moments (2-4 per recipe)
- ✅ Use ranges for measurements ("3-4 egg yolks")
- ✅ Describe churning by doneness, never estimate time
- ✅ Include allergen notes for nuts/wheat/soy (NOT milk/eggs)

**DON'T:**
- ❌ Add emojis, symbols, or decorative Unicode
- ❌ Use nationalities in recipe titles
- ❌ Estimate churn times ("20-25 minutes")
- ❌ Say "according to your ice cream maker's instructions"
- ❌ Skip difficulty rating explanation
- ❌ Skip total time parenthetical
- ❌ Omit "What it Tastes Like" final note
- ❌ Over-explain basic custard technique (reference fundamentals instead)

### File Editing Protocol

**Before Editing:**
1. Read target file completely
2. Review STYLE_GUIDE.md if content changes involved
3. Understand context and current voice

**During Editing:**
1. Preserve exact formatting structure
2. Maintain UTF-8 encoding
3. Keep HOMIE voice consistent
4. Verify all required elements present

**After Editing:**
1. Scan for non-text characters (emojis, symbols)
2. Check encoding (no corrupted UTF-8)
3. Verify structure matches style guide
4. Confirm voice is consistent
5. Test compilation if major changes

### Teaching Moments

Every recipe should have **2-4 teaching moments** that explain:

- **Scientific:** Why ingredients work (chemistry, physics)
- **Cultural/Historical:** Origins, significance, traditions
- **Technique Rationale:** Why this method matters
- **Ingredient Deep-Dives:** What it is, why it's special

**Example - Scientific:**
> "Browning butter—beurre noisette if you want to be fancy about it—transforms it from sweet-cream richness to deep, nutty, almost hazelnut-like complexity. The milk solids caramelize, creating literally HUNDREDS of new flavor compounds."

**Example - Cultural:**
> "Kulfi dates back to the Mughal era in 16th-century India. The word 'kulfi' comes from the Persian 'qulfi' meaning 'covered cup'—it was traditionally frozen in metal cones packed in ice and salt."

**Where Teaching Moments Go:**
- Opening paragraphs (brief context)
- Instructions (quick technique explanations)
- **Notes section** (detailed deep-dives - primary home)

---

## Common Tasks & Commands

### Edit a Recipe

```bash
# 1. Read the file
Read recipes/##_recipe_name.md

# 2. Make changes (follow STYLE_GUIDE.md)

# 3. Save file

# 4. Commit
git add recipes/##_recipe_name.md
git commit -m "Descriptive message about changes"
git push -u origin <branch-name>
```

### Add a New Recipe

```bash
# 1. Create file with proper numbering
Write recipes/##_new_recipe.md

# 2. Follow recipe structure exactly (see STYLE_GUIDE.md)

# 3. Verify all required elements present

# 4. Test compilation
python compile_book.py

# 5. Commit
git add recipes/##_new_recipe.md
git add Ice_Cream_to_Fight_Over_COMPLETE.md
git commit -m "Add new recipe: [recipe name]"
git push -u origin <branch-name>
```

### Modify Front Matter

```bash
# 1. Read target file
Read front_matter/##_section_name.md

# 2. Make changes (maintain voice consistency)

# 3. Save file

# 4. Test compilation
python compile_book.py

# 5. Commit
git add front_matter/##_section_name.md
git add Ice_Cream_to_Fight_Over_COMPLETE.md
git commit -m "Update [section name]"
git push -u origin <branch-name>
```

### Recompile Book

```bash
# Python (preferred) - compiles both versions by default
python compile_book.py

# Single version only
python compile_book.py --version vulgar
python compile_book.py --version clean

# Bash (alternative - vulgar only, no marker support)
chmod +x compile_book.sh
./compile_book.sh

# Verify output
ls -lh Ice_Cream_to_Fight_Over_COMPLETE*.md

# Commit if satisfied
git add Ice_Cream_to_Fight_Over_COMPLETE.md Ice_Cream_to_Fight_Over_COMPLETE_CLEAN.md
git commit -m "Recompile book with latest changes"
git push -u origin <branch-name>
```

### Fix Encoding Issues

```bash
# Scan for corrupted characters
grep -r "â€"" recipes/
grep -r "Ã©" recipes/

# Fix in individual files
# Replace â€" with —
# Replace Ã© with proper UTF-8 é

# Verify UTF-8 encoding
file recipes/*.md
# Should show: UTF-8 Unicode text
```

---

## Quality Assurance Checklist

### Pre-Commit Review Process

When reviewing a recipe before committing, check in this order:

1. **Non-text characters:**
   - [ ] Scan entire recipe for emojis
   - [ ] Check for symbols (✓, →, •)
   - [ ] Look for decorative Unicode
   - [ ] **Action:** MUST be removed immediately

2. **Encoding:**
   - [ ] Scan for corrupted characters (`â€"`, `Ã©`, etc.)
   - [ ] Verify proper UTF-8 for accents and foreign characters
   - [ ] **Action:** Fix all corrupted encoding

3. **Structure:**
   - [ ] Difficulty explanation present and uses HOMIE voice
   - [ ] Total time with parenthetical present
   - [ ] All required sections included
   - [ ] Bold headers in Ingredients and Instructions
   - [ ] "What it Tastes Like" as final note

4. **Allergens:**
   - [ ] Nuts/wheat/soy noted if present
   - [ ] NOT noting milk/eggs (this is ice cream)
   - [ ] Vegan recipes called out

5. **Voice:**
   - [ ] Count profanity (3-5 instances?)
   - [ ] "homie/dude/pal" usage (2-4 times?)
   - [ ] Conversational tone throughout
   - [ ] Self-deprecating but encouraging
   - [ ] Technical accuracy maintained

6. **Cultural depth:**
   - [ ] International recipes have substantive cultural context
   - [ ] Origins and significance explained
   - [ ] Honest about adaptations
   - [ ] Ethical sourcing guidance if relevant

7. **Teaching moments:**
   - [ ] 2-4 present throughout recipe
   - [ ] Good depth and educational value
   - [ ] Mix of scientific, cultural, technique rationale
   - [ ] Primarily in Notes section

8. **Technical clarity:**
   - [ ] Temperatures specified (°F)
   - [ ] Ranges provided ("3-4 egg yolks")
   - [ ] Visual cues included
   - [ ] Churning described by doneness (not time)
   - [ ] No phrase "according to your ice cream maker's instructions"

9. **Notes completeness:**
   - [ ] Sourcing guidance (if specialty ingredients)
   - [ ] Technique deep-dives (if complex methods)
   - [ ] Cultural context (if international)
   - [ ] Make-ahead guidance (if multi-component)
   - [ ] "What it Tastes Like" (ALWAYS final note)

### Master Reference Recipes

When unsure about structure or voice, reference these exemplar recipes:

- **Overall structure and voice:** Recipe 13 (Atole de Anis)
- **Cultural depth:** Recipe 07 (Wattleseed & Macadamia), Recipe 03 (Cardamom-Pistachio Kulfi)
- **Teaching moments:** Recipe 17 (Brown Butter Pecan)
- **Complex recipe management:** Recipe 27 (New Orleans Chicory Coffee & Beignet)
- **Egg-free recipes:** Recipe 03 (Cardamom-Pistachio Kulfi), Recipe 02 (Bơ Chanh)

---

## Technical Specifications

### File Format

- **Format:** Markdown (GitHub-flavored)
- **Extension:** `.md`
- **Encoding:** UTF-8
- **Line endings:** Unix (LF)
- **Character limit per line:** None (but keep readable)

### Measurements & Units

- **System:** US customary (cups, tablespoons, teaspoons)
- **Temperature:** Fahrenheit (°F with proper UTF-8 degree symbol)
- **Weight:** Pounds/ounces for produce context
- **Precision:** Ranges preferred ("3-4 egg yolks" not "3.5 yolks")

### Temperature Guidelines

| Type | Temperature | Notes |
|------|-------------|-------|
| Standard custard | 170-175°F | Sometimes noted as "to 175°F" |
| Light custard | 170-175°F | Emphasize lighter than usual |
| Caramel | Visual (deep amber, copper penny) | Visual beats temp |
| Soft ball stage | 240°F | Include visual cues too |
| Frying | Specific (e.g., 360°F for beignets) | Precision matters |

**Rule:** Provide temperature when precision matters, visual cues when appearance is more reliable.

### Churning Guidance (CRITICAL)

**DO NOT:**
- ❌ Estimate churn times ("20-25 minutes")
- ❌ Use phrase "according to your ice cream maker's instructions"

**DO:**
- ✅ Describe doneness: "until soft-serve consistency"
- ✅ Provide visual cues: "should look thick and pale cream-colored"
- ✅ Note variations: "May take longer than usual due to fruit content"
- ✅ Give context: "The ricotta makes this denser than standard custard"

**Why:** Equipment varies too widely. Readers need visual/textural cues, not time estimates that will be wrong.

### Version Control

- **Git:** Standard git repository
- **Remote:** `http://local_proxy@127.0.0.1:58280/git/cpitzi/ice_cream_book`
- **Hooks:** None currently configured
- **Branch naming:** `claude/claude-md-*` with session ID
- **Commit style:** Imperative mood, descriptive
- **Line length:** No strict limit (but keep commit messages under 72 chars first line)

### Build System

- **Languages:** Python 3 (preferred), Bash (alternative)
- **Dependencies:** None (standard library only)
- **Build time:** < 1 second (simple concatenation)
- **Output size:** ~345KB (8,200+ lines)
- **Incremental builds:** Not supported (full rebuild each time)
- **Caching:** None

---

## Quick Reference Card

### THE RULES (Essential Checklist)

✅ **Plain text only** - no emojis, no symbols, no decorative Unicode
✅ **Proper encoding** - fix corrupted characters on sight
✅ **NO nationalities in titles** - use regions, cities, or dish names
✅ **Difficulty + Total Time with HOMIE explanations** - required
✅ **3-5 strategic profanities** per recipe for emphasis
✅ **2-4 teaching moments** per recipe
✅ **Allergens for nuts/wheat/soy only** (not milk/eggs)
✅ **Cultural context for international recipes** - go deep
✅ **"What it tastes like" as final note** - always
✅ **Churning: describe doneness, never estimate time**
✅ **Voice: conversational, self-deprecating, technically accurate**

### File Paths Quick Reference

```
front_matter/##_section_name.md    - Intro, TOC, philosophy, fundamentals
recipes/##_recipe_name.md          - Individual recipes
back_matter/99_closing.md          - Closing remarks
STYLE_GUIDE.md                     - Comprehensive style documentation
README.md                          - Workflow guide
compile_book.py                    - Build script (Python)
compile_book.sh                    - Build script (Bash)
```

### Common Commands

```bash
# Read a file
Read recipes/##_recipe_name.md

# Compile book
python compile_book.py

# Commit changes
git add [file]
git commit -m "Descriptive message"
git push -u origin <branch-name>

# Check file encoding
file recipes/*.md

# Search for corrupted encoding
grep -r "â€"" recipes/
```

---

## Additional Resources

- **STYLE_GUIDE.md** - Full style guide (515 lines, authoritative)
- **README.md** - Workflow documentation
- **EXAMPLE_recipe_02_chili_mango.md** - Complete example recipe
- **EXAMPLE_front_matter_01_title_and_intro.md** - Front matter example
- **front_matter/08_custard_fundamentals.md** - Comprehensive custard tutorial

---

## Summary for AI Assistants

This is a **professional cookbook project** with:

1. **Strict style requirements** (read STYLE_GUIDE.md before content changes)
2. **Modular file structure** (edit individual files, not complete book)
3. **Distinctive voice** (HOMIE voice - casual, educational, strategic profanity)
4. **Plain text only** (absolutely NO emojis or decorative Unicode)
5. **Cultural respect** (deep context for international recipes required)
6. **Technical accuracy** (temperatures, measurements, technique explanations)
7. **Educational focus** (2-4 teaching moments per recipe)
8. **Git workflow** (descriptive commits, branch naming conventions)

**Most Important:**
- Always use exact file paths
- Preserve HOMIE voice
- Never add emojis or symbols
- Verify all required elements present
- Test compilation after significant changes
- Write descriptive commit messages

**When in doubt:** Reference STYLE_GUIDE.md or ask for clarification.

---

*This document was created to help AI assistants understand the ice_cream_book repository structure, conventions, and workflows. Last updated by Claude on 2025-11-19.*
