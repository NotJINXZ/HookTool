@echo off
setlocal enabledelayedexpansion

where pip >nul 2>nul
if %errorlevel% neq 0 (
    echo Error: pip is not installed. Please install Python and make sure pip is included in your PATH.
    exit /b 1
)

pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Error: Failed to install dependencies.
    exit /b 1
)

echo Dependencies installed successfully.
start start.bat
exit /b 0
