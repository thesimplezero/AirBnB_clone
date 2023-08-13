#!/bin/bash

# Check if a file path argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <file-path>"
    exit 1
fi

file_path="$1"
output_file="diff.txt"

# Check if the provided file path exists
if [ ! -f "$file_path" ]; then
    echo "File '$file_path' not found."
    exit 1
fi

# Get the list of commit hashes where the file was modified
commit_hashes=$(git log --pretty=format:"%h" -- "$file_path")

# Iterate through commit hashes and generate the diffs
echo "Generating diffs for '$file_path'..."
for commit_hash in $commit_hashes; do
    diff=$(git show "$commit_hash:$file_path")
    echo "Commit: $commit_hash" >> "$output_file"
    echo "$diff" >> "$output_file"
    echo "" >> "$output_file"
done

echo "Diffs saved to '$output_file'."
