#!/bin/bash
# Compile Ice Cream to Fight Over from modular files

echo "Compiling book..."

# Create/clear output file
> Ice_Cream_to_Fight_Over_COMPLETE.md

# Add front matter
for file in front_matter/*.md; do
    if [ -f "$file" ]; then
        cat "$file" >> Ice_Cream_to_Fight_Over_COMPLETE.md
        echo -e "\n\n---\n\n" >> Ice_Cream_to_Fight_Over_COMPLETE.md
        echo "✓ Added: $file"
    fi
done

# Add recipes (sorted numerically)
for file in recipes/*.md; do
    if [ -f "$file" ]; then
        cat "$file" >> Ice_Cream_to_Fight_Over_COMPLETE.md
        echo -e "\n\n---\n\n" >> Ice_Cream_to_Fight_Over_COMPLETE.md
        echo "✓ Added: $file"
    fi
done

# Add back matter
for file in back_matter/*.md; do
    if [ -f "$file" ]; then
        cat "$file" >> Ice_Cream_to_Fight_Over_COMPLETE.md
        echo -e "\n\n---\n\n" >> Ice_Cream_to_Fight_Over_COMPLETE.md
        echo "✓ Added: $file"
    fi
done

echo ""
echo "✅ Book compiled successfully!"
echo "   Output: Ice_Cream_to_Fight_Over_COMPLETE.md"
