#!/bin/bash

# Step 1: Show all branches and their changes
echo "List of branches:"
git branch -vv

# Prompt for the branch to merge
read -p "Enter the name of the branch you want to merge to main: " merge_branch

# Step 2: Suggest a strategy to move forward
echo "Please choose a strategy:"
echo "1. Merge"
echo "2. Rebase"
read -p "Enter the number of your chosen strategy: " strategy

# Execute the chosen strategy
if [ $strategy -eq 1 ]; then
    # Merge strategy
    git merge $merge_branch
elif [ $strategy -eq 2 ]; then
    # Rebase strategy
    git rebase $merge_branch
else
    echo "Invalid strategy choice."
    exit 1
fi

# Step 3: Merge to main without conflicts
git checkout main
git merge $merge_branch

# Clean up
git branch -d $merge_branch

echo "Process completed."
