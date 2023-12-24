@echo off

where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Error: Python is not installed. Please install Python and make sure it's included in your PATH.
    exit /b 1
)

python uwt.py
if %errorlevel% neq 0 (
    echo.
    echo Error: An error occurred while running the UWT script.
    echo Please check the console output for details.
    echo.
    pause
    exit /b 1
)

echo.
echo.
echo Process exited successfully.
pause
