@echo off
setlocal enabledelayedexpansion

REM Get current directory and convert to WSL path
set "CUR_WIN=%CD%"
set "CUR_WSL=%CUR_WIN%"
set "CUR_WSL=%CUR_WSL:\=/%"
set "CUR_WSL=%CUR_WSL:C:=/mnt/c%"
set "CUR_WSL=%CUR_WSL:c:=/mnt/c%"

REM Get repo root (where this script is)
set "REPO_WIN=%~dp0"
set "REPO_WIN=%REPO_WIN:~0,-1%"
set "REPO_WSL=%REPO_WIN%"
set "REPO_WSL=%REPO_WSL:\=/%"
set "REPO_WSL=%REPO_WSL:C:=/mnt/c%"
set "REPO_WSL=%REPO_WSL:c:=/mnt/c%"

REM Run test script in WSL
wsl --exec bash -c "cd '%CUR_WSL%' && '%REPO_WSL%/tools/test_code.sh'"

endlocal
