@echo off
echo Checking PowerShell execution policy...
powershell -Command "if ((Get-ExecutionPolicy) -eq 'Restricted') { exit 1 } else { exit 0 }"
if %errorlevel% neq 0 (
    echo Execution policy is set to Restricted. Changing policy...
    powershell -Command "Set-ExecutionPolicy RemoteSigned -Scope CurrentUser"
    if %errorlevel% neq 0 (
        echo Failed to change execution policy. Please run this script as Administrator.
        pause
        exit /b
    )
)

echo Creating virtual environment...
python -m venv venv

echo Activating virtual environment...
call venv\Scripts\activate

echo Installing dependencies...
pip install --upgrade pip
pip install openpyxl pandas colorama

echo Setup completed!
pause