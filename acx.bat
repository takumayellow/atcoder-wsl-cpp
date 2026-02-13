@echo off
setlocal enabledelayedexpansion

REM Get the directory where this script is located (Windows path)
set "REPO_WIN=%~dp0"
REM Remove trailing backslash
set "REPO_WIN=%REPO_WIN:~0,-1%"

REM Convert Windows path to WSL path (C:\Users\... -> /mnt/c/Users/...)
set "REPO_WSL=%REPO_WIN%"
set "REPO_WSL=%REPO_WSL:\=/%"
set "REPO_WSL=%REPO_WSL:C:=/mnt/c%"
set "REPO_WSL=%REPO_WSL:c:=/mnt/c%"

REM Detect which editor to use based on environment
REM Check TERM_PROGRAM (set by VS Code/Cursor integrated terminal)
set "EDITOR_CMD="
if "%TERM_PROGRAM%"=="vscode" (
    set "EDITOR_CMD=code"
) else if "%TERM_PROGRAM%"=="cursor" (
    set "EDITOR_CMD=cursor"
)

REM If not detected from TERM_PROGRAM, check VSCODE_PID or other env vars
if not defined EDITOR_CMD (
    if defined VSCODE_PID (
        REM Running inside VS Code terminal - check if it's actually Cursor
        if defined CURSOR_TRACE_ID (
            set "EDITOR_CMD=cursor"
        ) else (
            set "EDITOR_CMD=code"
        )
    )
)

REM Fallback: check which is available
if not defined EDITOR_CMD (
    where cursor >nul 2>&1
    if !errorlevel! equ 0 (
        set "EDITOR_CMD=cursor"
    ) else (
        where code >nul 2>&1
        if !errorlevel! equ 0 (
            set "EDITOR_CMD=code"
        )
    )
)

REM Run WSL script and capture output
set "FILE_TO_OPEN="
set "DIR_TO_CD="
for /f "tokens=*" %%i in ('wsl --exec bash -c "cd '%REPO_WSL%' && tools/acx %*"') do (
    set "LINE=%%i"
    REM Check if this line starts with CD:
    echo %%i | findstr /B "CD:" >nul
    if !errorlevel! equ 0 (
        set "DIR_TO_CD=%%i"
    ) else (
    REM Check if this line starts with OPEN:
    echo %%i | findstr /B "OPEN:" >nul
    if !errorlevel! equ 0 (
        set "FILE_TO_OPEN=%%i"
    ) else (
        echo %%i
    )
    )
)

REM If we got a dir path, convert and store it for PowerShell wrapper use
if defined DIR_TO_CD (
    set "WSL_DIR=!DIR_TO_CD:CD:=!"
    set "WIN_DIR=!WSL_DIR:/mnt/c/=C:\!"
    set "WIN_DIR=!WIN_DIR:/=\!"
    echo !WIN_DIR! > "%REPO_WIN%\.vscode\.acx_last_dir"
)

REM If we got a file path, convert and open it
if defined FILE_TO_OPEN (
    REM Remove "OPEN:" prefix and convert /mnt/c/ to C:\
    set "WSL_PATH=!FILE_TO_OPEN:OPEN:=!"
    set "WIN_PATH=!WSL_PATH:/mnt/c/=C:\!"
    set "WIN_PATH=!WIN_PATH:/=\!"

    echo Opening: !WIN_PATH!

    if defined EDITOR_CMD (
        !EDITOR_CMD! -r -g "!WIN_PATH!"
    ) else (
        echo No editor found. Please open !WIN_PATH! manually.
    )
)

endlocal
