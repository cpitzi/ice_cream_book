#!/usr/bin/env python3
"""
Compile Ice Cream to Fight Over from modular files.

Usage:
    python compile_book.py

Output:
    Ice_Cream_to_Fight_Over_COMPLETE.md
"""

import os
from pathlib import Path


def get_markdown_files(directory):
    """Get all markdown files from a directory, sorted naturally."""
    dir_path = Path(directory)
    if not dir_path.exists():
        return []
    md_files = sorted(dir_path.glob('*.md'))
    return [str(f) for f in md_files]


def compile_book():
    """Compile all sections into complete book."""

    front_matter_files = get_markdown_files('front_matter')
    recipe_files = get_markdown_files('recipes')
    back_matter_files = get_markdown_files('back_matter')

    all_files = front_matter_files + recipe_files + back_matter_files

    if not all_files:
        print("No markdown files found in front_matter/, recipes/, or back_matter/")
        print("   Make sure you've created the modular file structure.")
        return

    output = []
    for filepath in all_files:
        if not os.path.exists(filepath):
            print(f"Warning: {filepath} not found, skipping...")
            continue

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            output.append(content)
            print(f"  Added: {filepath}")

    complete_content = '\n\n---\n\n'.join(output)

    output_file = 'Ice_Cream_to_Fight_Over_COMPLETE.md'

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(complete_content)

    print(f"\nCompiled -> {output_file}")
    print(f"   Total sections: {len(output)}")
    print(f"   Front matter: {len(front_matter_files)} files")
    print(f"   Recipes: {len(recipe_files)} files")
    print(f"   Back matter: {len(back_matter_files)} files")
    print(f"   Total size: {len(complete_content):,} characters")


if __name__ == '__main__':
    compile_book()
