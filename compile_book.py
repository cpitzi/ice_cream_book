#!/usr/bin/env python3
"""
Compile Ice Cream to Fight Over from modular files.

Usage:
    python compile_book.py                  # compile both versions
    python compile_book.py --version vulgar # vulgar version only
    python compile_book.py --version clean  # clean version only

Output:
    Ice_Cream_to_Fight_Over_COMPLETE.md         (vulgar)
    Ice_Cream_to_Fight_Over_COMPLETE_CLEAN.md   (clean)

Inline markers in source files control per-version text:

    Inline swap:   {{v: vulgar text | clean text }}
    Vulgar block:  {{v:start}} ... {{v:end}}
    Clean block:   {{c:start}} ... {{c:end}}
"""

import argparse
import os
import re
from pathlib import Path


def get_markdown_files(directory):
    """Get all markdown files from a directory, sorted naturally."""
    dir_path = Path(directory)
    if not dir_path.exists():
        return []
    md_files = sorted(dir_path.glob('*.md'))
    return [str(f) for f in md_files]


def resolve_inline_markers(text, version):
    """Resolve {{v: vulgar | clean }} inline markers."""
    def replace_inline(match):
        vulgar_text = match.group(1).strip()
        clean_text = match.group(2).strip()
        return vulgar_text if version == 'vulgar' else clean_text

    return re.sub(r'\{\{v:\s*(.*?)\s*\|\s*(.*?)\s*\}\}', replace_inline, text)


def resolve_block_markers(text, version):
    """Resolve {{v:start}}...{{v:end}} and {{c:start}}...{{c:end}} block markers."""
    if version == 'vulgar':
        # Keep vulgar blocks, remove clean blocks
        text = re.sub(r'\{\{v:start\}\}\n?(.*?)\{\{v:end\}\}\n?', r'\1', text, flags=re.DOTALL)
        text = re.sub(r'\{\{c:start\}\}\n?(.*?)\{\{c:end\}\}\n?', '', text, flags=re.DOTALL)
    else:
        # Keep clean blocks, remove vulgar blocks
        text = re.sub(r'\{\{c:start\}\}\n?(.*?)\{\{c:end\}\}\n?', r'\1', text, flags=re.DOTALL)
        text = re.sub(r'\{\{v:start\}\}\n?(.*?)\{\{v:end\}\}\n?', '', text, flags=re.DOTALL)
    return text


def resolve_markers(text, version):
    """Resolve all version markers in text."""
    text = resolve_inline_markers(text, version)
    text = resolve_block_markers(text, version)
    # Clean up any double blank lines left by block removal
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text


def compile_book(version='vulgar'):
    """Compile all sections into complete book for the given version."""

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
    complete_content = resolve_markers(complete_content, version)

    if version == 'clean':
        output_file = 'Ice_Cream_to_Fight_Over_COMPLETE_CLEAN.md'
    else:
        output_file = 'Ice_Cream_to_Fight_Over_COMPLETE.md'

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(complete_content)

    label = "CLEAN" if version == "clean" else "VULGAR"
    print(f"\nCompiled [{label}] -> {output_file}")
    print(f"   Total sections: {len(output)}")
    print(f"   Front matter: {len(front_matter_files)} files")
    print(f"   Recipes: {len(recipe_files)} files")
    print(f"   Back matter: {len(back_matter_files)} files")
    print(f"   Total size: {len(complete_content):,} characters")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Compile Ice Cream to Fight Over cookbook.')
    parser.add_argument(
        '--version',
        choices=['vulgar', 'clean', 'both'],
        default='both',
        help='Which version to compile (default: both)',
    )
    args = parser.parse_args()

    if args.version == 'both':
        compile_book('vulgar')
        print()
        compile_book('clean')
    else:
        compile_book(args.version)
