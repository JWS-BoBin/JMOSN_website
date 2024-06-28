#!/bin/bash

echo "Git and VS Code Diagnostic Information"
echo "======================================"

echo "\nGit Version:"
git --version

echo "\nGit Configuration:"
git config --list

echo "\nVS Code Version:"
code --version

echo "\nVS Code Extensions:"
code --list-extensions

echo "\nRepository Size:"
du -sh .

echo "\nNumber of files in repository:"
git ls-files | wc -l

echo "\nLast few Git operations (from .git/logs/HEAD):"
tail -n 10 .git/logs/HEAD

echo "\nGit status:"
git status

echo "\nNetwork connectivity test (to github.com):"
ping -c 4 github.com
