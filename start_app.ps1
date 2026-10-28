# AgriProcure AI - Windows launcher
$ErrorActionPreference = "Stop"
$RootPath = Split-Path -Parent $MyInvocation.MyCommand.Definition

if (-not (Test-Path (Join-Path $RootPath "package.json"))) {
    throw "package.json was not found in the repository root: $RootPath"
}

Write-Host "Starting AgriProcure AI backend..." -ForegroundColor Cyan
Start-Process -FilePath "cmd.exe" -ArgumentList "/k", "python run.py" -WorkingDirectory $RootPath

Start-Sleep -Seconds 3

Write-Host "Starting React/Vite frontend..." -ForegroundColor Cyan
Start-Process -FilePath "cmd.exe" -ArgumentList "/k", "npm run dev" -WorkingDirectory $RootPath

Start-Sleep -Seconds 3
Start-Process "http://localhost:5173"

Write-Host ""
Write-Host "Backend:  http://127.0.0.1:5000"
Write-Host "Frontend: http://localhost:5173"
Write-Host ""
Write-Host "First run prerequisites:"
Write-Host "  pip install -r requirements.txt"
Write-Host "  npm install"
