# Quick Start Guide

## Installation
```bash
git clone https://github.com/anerb/VSDevContainer.git
cd VSDevContainer
```

## Basic Usage

### 1. Preview Installation Commands
```powershell
python vsdevcontainer.py
```

### 2. Execute Installation Commands
```powershell
# Review output first, then:
python vsdevcontainer.py | Out-String | Invoke-Expression
```

### 3. Check Installed Tools
```powershell
python vsdevcontainer.py --check
```

## What Gets Installed?

By default, VSDevContainer manages:
- **Visual Studio 2022 Professional** (v17.8.0)
- **Git** (v2.43.0)
- **GitHub CLI** (v2.40.0)

## Customization

Edit `requirements.json` to add/remove tools or change versions.

## Safety

✅ The tool **never** runs commands automatically  
✅ All commands are output to stdout for review  
✅ You control when and what gets executed  

## Need Help?

- See `README.md` for detailed documentation
- See `IMPLEMENTATION.md` for technical details
- See `example-usage.ps1` for PowerShell examples
