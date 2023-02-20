@echo off

echo Installing Pillow library...

python -m pip install pillow

if %errorlevel% neq 0 (
  echo Error: Failed to install Pillow library.
  exit /b %errorlevel%
)

echo Installation complete.
