#!/bin/bash
echo "Cleaning table..."

# We just replace the old table with a empty one
cp scripts/clean_index.html docs/index.html
echo "Table has been reset"
