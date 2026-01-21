@echo off
setlocal enabledelayedexpansion

REM Get current directory and convert to WSL path
set "CUR_WIN=%CD%"
set "CUR_WSL=%CUR_WIN%"
set "CUR_WSL=%CUR_WSL:\=/%"
set "CUR_WSL=%CUR_WSL:C:=/mnt/c%"
set "CUR_WSL=%CUR_WSL:c:=/mnt/c%"

REM Setup PATH and run acc submit in WSL
wsl --exec bash -c "export PATH=\"\$HOME/.local/bin:\$PATH\"; export NVM_DIR=\"\$HOME/.nvm\"; [ -s \"\$NVM_DIR/nvm.sh\" ] && . \"\$NVM_DIR/nvm.sh\"; cd '%CUR_WSL%' && acc s"

endlocal
