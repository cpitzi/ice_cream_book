#!/usr/bin/env python3
"""
Compile Ice Cream to Fight Over from modular files.

Usage: python compile_book.py
Output: Ice_Cream_to_Fight_Over_COMPLETE.md
"""

import os
from pathlib import Path

def compile_book():
    """Compile all sections into complete book."""
    
    # Define file order
    front_matter_files = [
        'front_matter/01_title_and_intro.md',
        'front_matter/02_what_makes_different.md',
        'front_matter/03_the_flavors.md',
        'front_matter/04_how_to_use.md',
        'front_matter/05_philosophy.md',
        'front_matter/06_difficulty_ratings.md',
        'front_matter/07_custard_fundamentals.md',
        'front_matter/08_final_thoughts.md',
    ]
    
    # All 27 recipe files
    recipe_files = [f'recipes/{i:02d}_*.md' for i in range(1, 28)]
    
    # Find actual recipe filenames (handles wildcard)
    recipe_paths = []
    for pattern in recipe_files:
        matches = list(Path('recipes').glob(pattern.split('/')[-1]))
        if matches:
            recipe_paths.append(str(matches[0]))
        else:
            print(f"Warning: No file found matching {pattern}")
    
    back_matter_files = [
        'back_matter/99_closing.md'
    ]
    
    # Combine all sections
    all_files = front_matter_files + sorted(recipe_paths) + back_matter_files
    
    # Read and concatenate
    output = []
    for filepath in all_files:
        if not os.path.exists(filepath):
            print(f"Warning: {filepath} not found, skipping...")
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            output.append(content)
            print(f"✓ Added: {filepath}")
    
    # Write complete book
    complete_content = '\n\n---\n\n'.join(output)
    
    output_file = 'Ice_Cream_to_Fight_Over_COMPLETE.md'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(complete_content)
    
    print(f"\n✅ Compiled book saved to: {output_file}")
    print(f"   Total sections: {len(output)}")
    print(f"   Total size: {len(complete_content):,} characters")

if __name__ == '__main__':
    compile_book()
