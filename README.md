# Ice Cream to Fight Over - Modular Structure

*Last verified: 2026-03-06*

## Quick Start

### 1. Create Directory Structure
```bash
mkdir -p front_matter recipes back_matter
```

### 2. Split the Current COMPLETE File

You'll need to manually split `Ice_Cream_to_Fight_Over_COMPLETE.md` into individual files following this structure:

**Front Matter Files:**
- `front_matter/01_title_and_intro.md` - From "# Ice Cream to Fight Over" through end of Introduction
- `front_matter/02_what_makes_different.md` - "## What Makes These Recipes Different" section
- `front_matter/03_the_flavors.md` - "## The Flavors" list
- `front_matter/04_how_to_use.md` - "## How to Actually Use This Book" section
- `front_matter/05_philosophy.md` - "## The Philosophy" section
- `front_matter/06_difficulty_ratings.md` - "## A Note on Difficulty" section
- `front_matter/07_custard_fundamentals.md` - "## The Custard Fundamentals" section
- `front_matter/08_final_thoughts.md` - "## Final Thoughts" section

**Recipe Files:**
Each recipe gets its own file starting from the `# Recipe Name` heading through the end of its Notes section:

- `recipes/01_atole_de_anis.md`
- `recipes/02_chili_mango.md`
- `recipes/03_earl_grey_burnt_honey.md`
- ... (through 27)

**Back Matter:**
- `back_matter/99_closing.md` - The "That's All, Homie" closing section

### 3. Compile the Book

**Using Python:**
```bash
python compile_book.py
```

**Using Bash:**
```bash
chmod +x compile_book.sh
./compile_book.sh
```

**Output:** `Ice_Cream_to_Fight_Over_COMPLETE.md`

---

## Workflow with Claude

### Editing Individual Sections

**Instead of:** "Edit the introduction"
**Say:** "Edit front_matter/01_title_and_intro.md"

**Instead of:** "Fix Recipe 15"  
**Say:** "Edit recipes/15_rum_banana.md"

### Requesting New Content

"Create recipes/28_new_recipe.md following the style guide"

### Generating Split Files

You can ask Claude to:
- "Extract recipes/12_appalachian_pawpaw_maple.md from the COMPLETE file"
- "Generate all recipe files from the COMPLETE file"
- "Split front_matter/01_title_and_intro.md from the COMPLETE file"

---

## GitHub Workflow

The book is version controlled at: https://github.com/cpitzi/ice_cream_book

### Basic Workflow with Claude

**When editing individual files:**
1. Tell Claude which file to edit: `"Edit recipes/08_miso_matcha.md"`
2. Claude makes the changes and provides the updated file
3. Download and replace in your local repo
4. Commit changes:
   ```bash
   git add recipes/08_miso_matcha.md
   git commit -m "Adjusted matcha ratio in miso matcha recipe"
   git push
   ```

**For compilation:**
```bash
python compile_book.py
git add Ice_Cream_to_Fight_Over_COMPLETE.md
git commit -m "Recompiled book with latest changes"
git push
```

### Optional: Exclude Compiled File from Git

If you prefer to only track modular files and compile locally, add this to `.gitignore`:
```
Ice_Cream_to_Fight_Over_COMPLETE.md
```

This keeps your repo clean with only the source files tracked. Compile the complete book whenever you need it locally.

### Commit Message Style

Good examples:
- `"Update difficulty rating for pawpaw recipe"`
- `"Fix typo in custard fundamentals"`
- `"Add note about candied ginger storage to sichuan plum"`
- `"Recompile book after recipe edits"`

---

## File Naming Conventions

**Front Matter:** `##_descriptive_name.md` (numbered for order)
**Recipes:** `##_recipe_name.md` (numbered to match recipe order)
**Back Matter:** `99_*.md` (high number to sort last)

**Rules:**
- Use underscores for spaces
- Lowercase everything
- Numbers are zero-padded (01, 02, etc.)
- Recipe filenames should match actual recipe titles (lowercase, underscored)

---

## Benefits of This Structure

✅ Work on individual recipes without loading everything
✅ Easy version control per file
✅ Request specific edits by filename
✅ Simple compilation when you need the full book
✅ Can reorganize easily (just rename/reorder files)
✅ Each file stays well under token limits

---

## Next Steps

1. Create the directory structure
2. Manually split COMPLETE file OR ask Claude to help extract specific files
3. Test compilation script
4. Start working on individual files with Claude
