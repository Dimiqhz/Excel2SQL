@echo off
echo Activating virtual environment...
call venv\Scripts\activate

echo Running the script...
python convert.py

echo Deactivating virtual environment...
deactivate

echo Script execution completed!
pause