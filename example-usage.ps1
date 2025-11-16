# Example PowerShell Script for VSDevContainer
# This script demonstrates how to use VSDevContainer output

Write-Host "VSDevContainer - Example Usage" -ForegroundColor Cyan
Write-Host "================================`n" -ForegroundColor Cyan

# Option 1: Review commands before executing
Write-Host "Option 1: Review commands first" -ForegroundColor Yellow
Write-Host "Run: python vsdevcontainer.py" -ForegroundColor Gray
Write-Host "Then copy and paste the commands you want to execute`n" -ForegroundColor Gray

# Option 2: Save to a file for later execution
Write-Host "Option 2: Save commands to a file" -ForegroundColor Yellow
Write-Host "Run: python vsdevcontainer.py > setup-commands.ps1" -ForegroundColor Gray
Write-Host "Then review and execute: .\setup-commands.ps1`n" -ForegroundColor Gray

# Option 3: Direct execution (use with caution)
Write-Host "Option 3: Direct execution" -ForegroundColor Yellow
Write-Host "Run: python vsdevcontainer.py | Out-String | Invoke-Expression" -ForegroundColor Gray
Write-Host "WARNING: This executes all commands immediately!`n" -ForegroundColor Red

# Option 4: Check what's already installed
Write-Host "Option 4: Check installed tools" -ForegroundColor Yellow
Write-Host "Run: python vsdevcontainer.py --check" -ForegroundColor Gray
Write-Host ""

Write-Host "Note: Most installation commands require Administrator privileges" -ForegroundColor Cyan
