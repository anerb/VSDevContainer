#!/usr/bin/env python3
"""
Tests for VSDevContainer tool
Simple validation tests to ensure correct command generation
"""

import json
import sys
from pathlib import Path
from io import StringIO

# Add parent directory to path to import vsdevcontainer
sys.path.insert(0, str(Path(__file__).parent))

import vsdevcontainer


def test_load_requirements():
    """Test loading requirements from JSON file"""
    tools = vsdevcontainer.load_requirements()
    assert len(tools) > 0, "Should load at least one tool"
    assert all('name' in tool for tool in tools), "All tools should have a name"
    print("✓ test_load_requirements passed")


def test_generate_scoop_commands():
    """Test scoop command generation"""
    tool = {
        "name": "Git",
        "scoop": {
            "bucket": "main",
            "package": "git"
        },
        "version": "2.43.0"
    }
    commands = vsdevcontainer.generate_scoop_commands(tool)
    assert len(commands) > 0, "Should generate at least one command"
    assert any("scoop install" in cmd for cmd in commands), "Should contain install command"
    assert any("git@2.43.0" in cmd for cmd in commands), "Should include version"
    print("✓ test_generate_scoop_commands passed")


def test_generate_scoop_commands_with_bucket():
    """Test scoop command generation with non-main bucket"""
    tool = {
        "name": "Visual Studio 2022",
        "scoop": {
            "bucket": "versions",
            "package": "visualstudio2022professional"
        },
        "version": "17.8.0"
    }
    commands = vsdevcontainer.generate_scoop_commands(tool)
    assert len(commands) >= 2, "Should generate bucket add and install commands"
    assert any("scoop bucket add versions" in cmd for cmd in commands), "Should add bucket"
    assert any("scoop install" in cmd for cmd in commands), "Should contain install command"
    print("✓ test_generate_scoop_commands_with_bucket passed")


def test_generate_winget_commands():
    """Test winget command generation"""
    tool = {
        "name": "Git",
        "winget": {
            "id": "Git.Git"
        },
        "version": "2.43.0"
    }
    commands = vsdevcontainer.generate_winget_commands(tool)
    assert len(commands) > 0, "Should generate at least one command"
    assert any("winget install" in cmd for cmd in commands), "Should contain install command"
    assert any("Git.Git" in cmd for cmd in commands), "Should include package ID"
    assert any("2.43.0" in cmd for cmd in commands), "Should include version"
    print("✓ test_generate_winget_commands passed")


def test_generate_check_commands():
    """Test check command generation"""
    tool = {
        "name": "Git",
        "scoop": {
            "bucket": "main",
            "package": "git"
        },
        "winget": {
            "id": "Git.Git"
        }
    }
    commands = vsdevcontainer.generate_check_commands(tool)
    assert len(commands) > 0, "Should generate at least one command"
    assert any("scoop info" in cmd for cmd in commands), "Should contain scoop info command"
    print("✓ test_generate_check_commands passed")


def test_generate_installation_commands():
    """Test full installation command generation"""
    tools = [{
        "name": "Test Tool",
        "scoop": {
            "bucket": "main",
            "package": "test"
        },
        "version": "1.0.0",
        "priority": "scoop"
    }]
    
    # Capture stdout
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    
    try:
        vsdevcontainer.generate_installation_commands(tools)
        output = sys.stdout.getvalue()
        
        assert "Test Tool" in output, "Output should contain tool name"
        assert "scoop install" in output, "Output should contain scoop install command"
        assert "VSDevContainer" in output, "Output should contain header"
    finally:
        sys.stdout = old_stdout
    
    print("✓ test_generate_installation_commands passed")


def run_tests():
    """Run all tests"""
    print("Running VSDevContainer tests...\n")
    
    tests = [
        test_load_requirements,
        test_generate_scoop_commands,
        test_generate_scoop_commands_with_bucket,
        test_generate_winget_commands,
        test_generate_check_commands,
        test_generate_installation_commands
    ]
    
    failed = 0
    for test in tests:
        try:
            test()
        except AssertionError as e:
            print(f"✗ {test.__name__} failed: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ {test.__name__} error: {e}")
            failed += 1
    
    print(f"\nTests completed: {len(tests) - failed}/{len(tests)} passed")
    return failed == 0


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
