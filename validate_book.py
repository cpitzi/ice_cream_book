#!/usr/bin/env python3
"""
Validate compiled book versions for quality issues.

Checks:
  1. No unprocessed {{v:...}} or {{c:...}} markers in compiled output
  2. Clean version contains no profanity
  3. No corrupted UTF-8 encoding patterns
  4. Every recipe has required structural elements
  5. No duplicate recipe titles

Exit code 0 = all checks pass, 1 = failures found.
"""

import argparse
import re
import sys
from pathlib import Path


VULGAR_FILE = "Ice_Cream_to_Fight_Over_COMPLETE.md"
CLEAN_FILE = "Ice_Cream_to_Fight_Over_COMPLETE_CLEAN.md"

# Profanity pattern for clean version check.
PROFANITY_BROAD_RE = re.compile(
    r'\bfuck|\bshit\b|\bdamn\b|\bgoddam|\bdipshit|\bdumbass|\bjackass|\bhalf-ass|\bbatshit',
    re.IGNORECASE
)

# Corrupted UTF-8 patterns (mojibake).
ENCODING_ERRORS = [
    (r'â€"', 'corrupted em dash'),
    (r'â€"', 'corrupted em dash variant'),
    (r'â€™', 'corrupted right single quote'),
    (r'â€œ', 'corrupted left double quote'),
    (r'â€\x9d', 'corrupted right double quote'),
    (r'Ã©', 'corrupted e-acute'),
    (r'Ã¨', 'corrupted e-grave'),
    (r'Ã¼', 'corrupted u-umlaut'),
    (r'Ã±', 'corrupted n-tilde'),
    (r'Ã¶', 'corrupted o-umlaut'),
    (r'Ã¡', 'corrupted a-acute'),
    (r'Ã­', 'corrupted i-acute'),
    (r'Ã³', 'corrupted o-acute'),
    (r'Ã§', 'corrupted c-cedilla'),
]

# Required recipe sections.
REQUIRED_SECTIONS = [
    (r'^# .+', 'Recipe title (# heading)'),
    (r'\*\*Difficulty:\*\*', 'Difficulty rating'),
    (r'\*\*Total Time:\*\*', 'Total time'),
    (r'^## Ingredients', 'Ingredients section'),
    (r'^## Instructions', 'Instructions section'),
    (r'^## Notes', 'Notes section'),
    (r'(?i)\*\*What [Ii]t [Tt]astes [Ll]ike', '"What it tastes like" note'),
]


def read_file(path):
    """Read file contents, return None if missing."""
    p = Path(path)
    if not p.exists():
        return None
    return p.read_text(encoding='utf-8')


def check_unprocessed_markers(content, filename):
    """Check for leftover {{v:...}} or {{c:...}} markers."""
    errors = []
    for i, line in enumerate(content.splitlines(), 1):
        if '{{v:' in line or '{{c:' in line:
            errors.append(f"  {filename}:{i}: unprocessed marker: {line.strip()[:80]}")
    return errors


def check_profanity(content, filename):
    """Check clean version for profanity."""
    errors = []
    # Known false positives to skip.
    false_positives = {
        'hells', 'shelling', 'shell', 'damson', 'dammed',
        'class', 'pass', 'passing', 'hassle', 'brass',
        'assess', 'assist', 'assignment', 'assume', 'assembly',
    }

    for i, line in enumerate(content.splitlines(), 1):
        for match in PROFANITY_BROAD_RE.finditer(line):
            word_start = match.start()
            # Extract the full word around the match.
            word_match = re.search(r'\b\w+\b', line[max(0, word_start - 5):word_start + 20])
            if word_match:
                full_word = word_match.group().lower()
                if full_word in false_positives:
                    continue
            snippet = line.strip()[:100]
            errors.append(f"  {filename}:{i}: profanity detected: {snippet}")
    return errors


def check_encoding(content, filename):
    """Check for corrupted UTF-8 encoding patterns."""
    errors = []
    for pattern, description in ENCODING_ERRORS:
        for i, line in enumerate(content.splitlines(), 1):
            if pattern in line:
                errors.append(f"  {filename}:{i}: {description}: {line.strip()[:80]}")
    return errors


def extract_recipes(content):
    """Split compiled book into individual recipes by # heading."""
    recipes = []
    lines = content.splitlines()
    current_title = None
    current_lines = []
    in_recipes = False

    for line in lines:
        # Detect recipe section (after front matter, before back matter).
        # Recipes start with "# " and have a difficulty rating.
        if line.startswith('# ') and not line.startswith('# Ice Cream') and not line.startswith('# The End'):
            if current_title and in_recipes:
                recipes.append((current_title, '\n'.join(current_lines)))
            current_title = line
            current_lines = [line]
            in_recipes = True
        elif in_recipes:
            current_lines.append(line)

    # Don't forget the last recipe.
    if current_title and in_recipes:
        recipes.append((current_title, '\n'.join(current_lines)))

    return recipes


def check_recipe_structure(content, filename):
    """Check that each recipe has all required structural elements."""
    errors = []
    recipes = extract_recipes(content)

    if not recipes:
        errors.append(f"  {filename}: no recipes found in compiled output")
        return errors

    for title, recipe_text in recipes:
        recipe_name = title.lstrip('# ').strip()
        # Skip non-recipe sections that might be in front/back matter.
        if any(skip in recipe_name.lower() for skip in [
            'ice cream to fight over', 'table of contents', 'what makes',
            'philosophy', 'how to use', 'the flavors', 'difficulty ratings',
            'custard fundamentals', 'final thoughts', 'the end', 'closing',
            "that's all",
        ]):
            continue

        for pattern, description in REQUIRED_SECTIONS:
            if not re.search(pattern, recipe_text, re.MULTILINE):
                errors.append(f"  {filename}: recipe '{recipe_name}' missing: {description}")

    return errors


def check_duplicate_titles(content, filename):
    """Check for duplicate recipe titles."""
    errors = []
    titles = re.findall(r'^# (.+)$', content, re.MULTILINE)
    seen = {}
    for title in titles:
        if title in seen:
            errors.append(f"  {filename}: duplicate title: '{title}'")
        seen[title] = True
    return errors


def main():
    parser = argparse.ArgumentParser(description='Validate compiled book versions.')
    parser.add_argument(
        '--strict', action='store_true',
        help='Treat all checks as errors (default: profanity and structure are warnings)',
    )
    args = parser.parse_args()

    all_errors = []
    warnings = []
    checks_run = 0

    # Check both compiled files exist.
    vulgar = read_file(VULGAR_FILE)
    clean = read_file(CLEAN_FILE)

    if vulgar is None:
        all_errors.append(f"  MISSING: {VULGAR_FILE} not found. Run: python compile_book.py")
    if clean is None:
        all_errors.append(f"  MISSING: {CLEAN_FILE} not found. Run: python compile_book.py")

    if vulgar is None or clean is None:
        print("FAIL: compiled files missing")
        for e in all_errors:
            print(e)
        return 1

    # 1. Unprocessed markers.
    print("Check: unprocessed markers...")
    checks_run += 1
    errors = check_unprocessed_markers(vulgar, VULGAR_FILE)
    errors += check_unprocessed_markers(clean, CLEAN_FILE)
    if errors:
        print(f"  FAIL ({len(errors)} issues)")
        all_errors.extend(errors)
    else:
        print("  PASS")

    # 2. Clean version profanity.
    print("Check: clean version profanity-free...")
    checks_run += 1
    errors = check_profanity(clean, CLEAN_FILE)
    if errors:
        # Deduplicate.
        errors = list(dict.fromkeys(errors))
        if args.strict:
            print(f"  FAIL ({len(errors)} issues)")
            all_errors.extend(errors)
        else:
            print(f"  WARNING ({len(errors)} issues — non-blocking until all recipes converted)")
            warnings.extend(errors)
    else:
        print("  PASS")

    # 3. Encoding checks (both versions).
    print("Check: UTF-8 encoding integrity...")
    checks_run += 1
    errors = check_encoding(vulgar, VULGAR_FILE)
    errors += check_encoding(clean, CLEAN_FILE)
    if errors:
        print(f"  FAIL ({len(errors)} issues)")
        all_errors.extend(errors)
    else:
        print("  PASS")

    # 4. Recipe structure (check vulgar version — it has all content).
    print("Check: recipe structure completeness...")
    checks_run += 1
    errors = check_recipe_structure(vulgar, VULGAR_FILE)
    if errors:
        if args.strict:
            print(f"  FAIL ({len(errors)} issues)")
            all_errors.extend(errors)
        else:
            print(f"  WARNING ({len(errors)} issues — non-blocking until all recipes complete)")
            warnings.extend(errors)
    else:
        print("  PASS")

    # 5. Duplicate titles.
    print("Check: no duplicate titles...")
    checks_run += 1
    errors = check_duplicate_titles(vulgar, VULGAR_FILE)
    if errors:
        print(f"  FAIL ({len(errors)} issues)")
        all_errors.extend(errors)
    else:
        print("  PASS")

    # 6. Source file encoding (check individual source files).
    print("Check: source file encoding...")
    checks_run += 1
    source_errors = []
    for directory in ['front_matter', 'recipes', 'back_matter']:
        for md_file in sorted(Path(directory).glob('*.md')):
            content = md_file.read_text(encoding='utf-8')
            source_errors += check_encoding(content, str(md_file))
    if source_errors:
        print(f"  FAIL ({len(source_errors)} issues)")
        all_errors.extend(source_errors)
    else:
        print("  PASS")

    # Summary.
    print(f"\n{'=' * 50}")
    if warnings:
        print(f"WARNINGS: {len(warnings)} profanity issue(s) in clean version (non-blocking)\n")
        for w in warnings:
            print(w)
        print()
    if all_errors:
        print(f"FAILED: {len(all_errors)} issue(s) found across {checks_run} checks\n")
        for e in all_errors:
            print(e)
        return 1
    else:
        print(f"ALL PASSED: {checks_run} checks, 0 issues")
        return 0


if __name__ == '__main__':
    sys.exit(main())
