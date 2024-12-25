#!/bin/zsh
git pull origin main
git add .
git commit -m "${1:-committed by git_sync.sh}"
git push origin main
echo "Git sync complete!"
