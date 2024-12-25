@echo off
:: 设置分支名称
set BRANCH=main

:: 拉取远程最新代码
echo Pulling latest changes from %BRANCH% branch...
git pull origin %BRANCH%

:: 添加所有更改
echo Adding changes to staging...
git add .

:: 提交更改，支持自定义提交信息
set /p COMMIT_MSG=Enter commit message (default: committed by git_sync.bat): 
if "%COMMIT_MSG%"=="" set COMMIT_MSG=committed by git_sync.bat
git commit -m "%COMMIT_MSG%"

:: 推送到远程仓库
echo Pushing changes to %BRANCH% branch...
git push origin %BRANCH%

echo Git sync complete!
pause
