#!/usr/bin/env python3
"""
VSDevContainer - A tool to manage Windows development environment for Visual Studio 2022
Outputs PowerShell commands to enforce tool versions using scoop and winget.
"""

import json
import sys
import argparse
from pathlib import Path
from typing import Dict, List, Any


def load_requirements(requirements_file: str = "requirements.json") -> List[Dict[str, Any]]:
    """Load tool requirements from JSON file."""
    script_dir = Path(__file__).parent
    requirements_path = script_dir / requirements_file
    
    if not requirements_path.exists():
        print(f"Error: Requirements file not found: {requirements_path}", file=sys.stderr)
        sys.exit(1)
    
    try:
        with open(requirements_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in requirements file: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: Failed to read requirements file: {e}", file=sys.stderr)
        sys.exit(1)
    
    tools = data.get('tools', [])
    if not tools:
        print("Warning: No tools defined in requirements file", file=sys.stderr)
    
    return tools


def generate_scoop_commands(tool: Dict[str, Any]) -> List[str]:
    """Generate scoop installation commands for a tool."""
    commands = []
    scoop_info = tool.get('scoop', {})
    bucket = scoop_info.get('bucket')
    package = scoop_info.get('package')
    version = tool.get('version')
    
    if not package:
        return []
    
    # Add bucket if needed and not 'main'
    if bucket and bucket != 'main':
        commands.append(f"scoop bucket add {bucket}")
    
    # Install or update the package
    # Note: Scoop doesn't easily support version pinning in install command
    # Users would need to use 'scoop install package@version' for specific versions
    if version:
        commands.append(f"scoop install {package}@{version}")
    else:
        commands.append(f"scoop install {package}")
    
    return commands


def generate_winget_commands(tool: Dict[str, Any]) -> List[str]:
    """Generate winget installation commands for a tool."""
    commands = []
    winget_info = tool.get('winget', {})
    package_id = winget_info.get('id')
    version = tool.get('version')
    
    if not package_id:
        return []
    
    # Install with specific version if provided
    if version:
        commands.append(f"winget install --id {package_id} --version {version} --silent --accept-package-agreements --accept-source-agreements")
    else:
        commands.append(f"winget install --id {package_id} --silent --accept-package-agreements --accept-source-agreements")
    
    return commands


def generate_check_commands(tool: Dict[str, Any]) -> List[str]:
    """Generate commands to check if a tool is installed."""
    commands = []
    name = tool.get('name', 'Unknown')
    
    commands.append(f"# Checking {name}")
    
    # Check with scoop first (if available)
    if tool.get('scoop'):
        package = tool['scoop'].get('package')
        commands.append(f"scoop info {package} | Out-Null")
    
    # Alternative: Check with winget
    if tool.get('winget'):
        package_id = tool['winget'].get('id')
        commands.append(f"# Alternative: winget list --id {package_id} | Out-Null")
    
    return commands


def validate_tool(tool: Dict[str, Any]) -> bool:
    """Validate that a tool has required fields."""
    if not tool.get('name'):
        print(f"Warning: Tool missing 'name' field: {tool}", file=sys.stderr)
        return False
    
    if not tool.get('scoop') and not tool.get('winget'):
        print(f"Warning: Tool '{tool.get('name')}' has no installer configuration", file=sys.stderr)
        return False
    
    return True


def generate_installation_commands(tools: List[Dict[str, Any]], check_only: bool = False) -> None:
    """Generate and print PowerShell commands for all tools."""
    print("# VSDevContainer - Development Environment Setup")
    print("# Generated PowerShell commands to enforce tool versions")
    print("# Run these commands in PowerShell with administrator privileges")
    print()
    
    valid_tools = [tool for tool in tools if validate_tool(tool)]
    
    if not valid_tools:
        print("# No valid tools to process", file=sys.stderr)
        return
    
    for tool in valid_tools:
        name = tool.get('name', 'Unknown Tool')
        priority = tool.get('priority', 'scoop')
        
        print(f"# {name}")
        print(f"# Priority installer: {priority}")
        
        if check_only:
            check_cmds = generate_check_commands(tool)
            for cmd in check_cmds:
                print(cmd)
        else:
            # Generate commands based on priority
            if priority == 'scoop' and tool.get('scoop'):
                commands = generate_scoop_commands(tool)
                if commands:
                    print("# Using scoop:")
                    for cmd in commands:
                        print(cmd)
                # Also show winget alternative
                if tool.get('winget'):
                    winget_cmds = generate_winget_commands(tool)
                    if winget_cmds:
                        print("# Alternative using winget:")
                        for cmd in winget_cmds:
                            print(f"# {cmd}")
            else:
                # Use winget as primary
                commands = generate_winget_commands(tool)
                if commands:
                    print("# Using winget:")
                    for cmd in commands:
                        print(cmd)
                # Show scoop alternative
                if tool.get('scoop'):
                    scoop_cmds = generate_scoop_commands(tool)
                    if scoop_cmds:
                        print("# Alternative using scoop:")
                        for cmd in scoop_cmds:
                            print(f"# {cmd}")
        
        print()


def main():
    """Main entry point for the VSDevContainer tool."""
    parser = argparse.ArgumentParser(
        description='VSDevContainer - Manage Windows development environment for Visual Studio 2022',
        epilog='The tool outputs PowerShell commands to stdout. Pipe the output to PowerShell to execute.'
    )
    parser.add_argument(
        '--check',
        action='store_true',
        help='Generate commands to check installed tools instead of installation commands'
    )
    parser.add_argument(
        '--requirements',
        default='requirements.json',
        help='Path to requirements JSON file (default: requirements.json)'
    )
    
    args = parser.parse_args()
    
    try:
        tools = load_requirements(args.requirements)
        generate_installation_commands(tools, check_only=args.check)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
