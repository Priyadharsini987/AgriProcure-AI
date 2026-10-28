@echo off
setlocal
title AgriProcure AI

set "ROOT=%~dp0"
cd /d "%ROOT%"

echo ==========================================
echo        AGRIPROCURE AI - STARTUP
echo ==========================================

if not exist "%ROOT%package.json" (
    echo ERROR: package.json not found in %ROOT%
    pause
    exit /b 1
)

echo Starting Flask backend...
start "AgriProcure Backend" cmd /k "cd /d ""%ROOT%"" && python run.py"

timeout /t 3 /nobreak >nul

echo Starting React/Vite frontend...
start "AgriProcure Frontend" cmd /k "cd /d ""%ROOT%"" && npm run dev"

timeout /t 3 /nobreak >nul
start http://localhost:5173

echo.
echo Backend:  http://127.0.0.1:5000
echo Frontend: http://localhost:5173
echo.
echo If this is the first run, install dependencies first:
echo   pip install -r requirements.txt
echo   npm install
echo.
pause
