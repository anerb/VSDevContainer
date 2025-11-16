# VSDevContainer

A Python tool to manage and enforce a stable Windows development environment for Visual Studio 2022. The tool outputs PowerShell commands to install and manage development tools using **scoop** (preferred) and **winget** package managers.

## Overview

VSDevContainer helps maintain consistent development environments by:
- Defining required tools and their versions in a configuration file
- Generating PowerShell commands to install/update tools
- Preferring scoop over winget for package management
- Never directly modifying your environment - only outputs commands

## Requirements

- Python 3.6 or higher
- Windows operating system
- PowerShell
- Scoop and/or Winget installed

## Installation

1. Clone this repository:
```bash
git clone https://github.com/anerb/VSDevContainer.git
cd VSDevContainer
```

2. Ensure you have Python 3 installed:
```powershell
python --version
```

## Usage

### Generate Installation Commands

Run the tool to generate PowerShell commands for installing/updating required tools:

```powershell
python vsdevcontainer.py
```

This will output PowerShell commands to stdout. To execute them, you can:

1. **Copy and paste** the commands into PowerShell (run as Administrator)
2. **Pipe directly to PowerShell**:
```powershell
python vsdevcontainer.py | Out-String | Invoke-Expression
```

### Check Installed Tools

To generate commands that check if tools are already installed:

```powershell
python vsdevcontainer.py --check
```

### Custom Requirements File

Specify a custom requirements file:

```powershell
python vsdevcontainer.py --requirements custom-requirements.json
```

## Configuration

Tool requirements are defined in `requirements.json`. Each tool specifies:

- **name**: Human-readable tool name
- **scoop**: Scoop package information (bucket and package name)
- **winget**: Winget package ID
- **version**: Target version to install
- **priority**: Preferred installer ('scoop' or 'winget')

Example:
```json
{
  "tools": [
    {
      "name": "Git",
      "scoop": {
        "bucket": "main",
        "package": "git"
      },
      "winget": {
        "id": "Git.Git"
      },
      "version": "2.43.0",
      "priority": "scoop"
    }
  ]
}
```

## Supported Tools

By default, VSDevContainer manages:
- Visual Studio 2022 Professional
- Git
- GitHub CLI (gh)

You can add more tools by editing `requirements.json`.

## How It Works

1. The tool reads `requirements.json` to determine required tools and versions
2. For each tool, it generates installation commands based on priority (scoop preferred)
3. Commands are output to stdout for manual review and execution
4. The tool never directly modifies your system - you control when commands are executed

## Package Manager Priority

VSDevContainer prefers **scoop** over **winget** because:
- Scoop is designed for developers and power users
- Better version management and updates
- No UAC prompts for most installations
- Cleaner uninstalls

However, both options are generated so you can choose based on your needs.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

See the LICENSE file for details.
