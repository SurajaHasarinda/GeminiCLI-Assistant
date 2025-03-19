@echo off 
@REM `@echo off` is used to turn off the command echoing.
@REM If you want to see the commands being executed, remove `@echo off`.
@REM This script is used to call Python scripts from the command line
@REM Usage: ai <command> <args>

@REM Get the absolute path of the batch file directory
set DIR=%~dp0

if "%1"=="help" (
    python %DIR%\src\help.py
    exit /b
)

if "%1"=="autocommit" (
    python %DIR%\src\git_auto_commit.py
    exit /b
)

if "%1"=="findcmd" (
    python %DIR%\src\find_command.py %2
    exit /b
)

if "%1"=="sortfiles" (
    python %DIR%\src\sort_files.py
    exit /b
)

if "%1"=="test" (
    python %DIR%\src\test.py
    exit /b
)

echo Invalid command! Type "ai help" for a list of available commands.
