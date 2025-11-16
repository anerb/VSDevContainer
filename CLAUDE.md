# CLAUDE.md - AI Assistant Guide for VSDevContainer

This document provides comprehensive guidance for AI assistants working with the VSDevContainer repository.

## Repository Overview

**Project Name**: VSDevContainer
**Purpose**: Pin and standardize the development environment for Visual Studio on Windows
**License**: MIT License (Copyright 2025 anerb)
**Current Status**: Initial setup phase

## Repository Structure

```
VSDevContainer/
├── .git/                 # Git version control
├── .gitignore           # Visual Studio comprehensive gitignore
├── LICENSE              # MIT License
├── README.md            # Project overview
└── CLAUDE.md            # This file - AI assistant guide
```

### Expected Future Structure

As the project develops, expect the following structure to emerge:

```
VSDevContainer/
├── .devcontainer/       # VS Code dev container configuration
│   ├── devcontainer.json
│   └── Dockerfile
├── src/                 # Source code
├── tests/              # Test suite
├── docs/               # Documentation
├── scripts/            # Build and automation scripts
├── .vs/                # Visual Studio settings (gitignored)
└── *.sln               # Visual Studio solution file(s)
```

## Technology Stack

Based on the .gitignore configuration, this project supports:

- **.NET/C# Development**: Primary focus with MSBuild, NuGet packages
- **C++ Development**: Visual C++ cache files and build artifacts
- **F# Support**: Ionide and Fody references
- **Node.js**: Node modules and related tooling
- **Python**: Python Tools for Visual Studio (PTVS)
- **Azure**: Azure publish settings and cloud development
- **Testing Frameworks**: MSTest, NUnit, xUnit support expected

## Development Workflows

### Git Branch Strategy

- **Main Branch**: Primary development branch (to be determined)
- **Feature Branches**: Use `claude/` prefix for AI-assisted development
- **Current Working Branch**: `claude/claude-md-mi24t7vsatendcjw-01NbcK94BxdarS14eLRUeHHy`

### Git Operations

**Pushing Changes**:
```bash
git push -u origin <branch-name>
```
- Branch names MUST start with 'claude/' and include session ID
- Retry up to 4 times with exponential backoff (2s, 4s, 8s, 16s) on network errors

**Fetching/Pulling**:
```bash
git fetch origin <branch-name>
git pull origin <branch-name>
```
- Retry up to 4 times with exponential backoff on failures

### Commit Conventions

Follow these guidelines for commits:

1. **Commit Message Format**:
   ```
   <type>: <short summary>

   <optional detailed description>
   ```

2. **Types**:
   - `feat`: New feature
   - `fix`: Bug fix
   - `docs`: Documentation changes
   - `refactor`: Code refactoring
   - `test`: Adding or updating tests
   - `build`: Build system changes
   - `ci`: CI/CD changes
   - `chore`: Maintenance tasks

3. **Use HEREDOC for multi-line messages**:
   ```bash
   git commit -m "$(cat <<'EOF'
   feat: Add development container configuration

   Includes Docker and devcontainer.json setup
   EOF
   )"
   ```

## Code Conventions

### .NET/C# Guidelines

- **Naming Conventions**:
  - PascalCase for classes, methods, properties, and public members
  - camelCase for private fields and local variables
  - Prefix private fields with underscore: `_privateField`

- **File Organization**:
  - One class per file
  - File name matches class name
  - Organize using namespaces matching folder structure

- **Documentation**:
  - Use XML documentation comments for public APIs
  - Include `<summary>`, `<param>`, and `<returns>` tags

### Project File Patterns

**Ignored Files** (from .gitignore):
- Build outputs: `bin/`, `obj/`, `out/`
- User-specific files: `*.user`, `*.suo`, `*.userosscache`
- Visual Studio cache: `.vs/`, `.vscode/`
- NuGet packages: `packages/` (except build/)
- Test results: `TestResult.xml`, `*.trx`
- Logs: `*.log`, `logs/`
- Environment files: `*.env`

**Tracked Files**:
- Source code: `*.cs`, `*.cpp`, `*.h`, `*.fs`
- Project files: `*.csproj`, `*.sln`, `*.vcxproj`
- Configuration: `*.config`, `appsettings.json`
- Documentation: `*.md`, `*.txt`
- Scripts: `*.ps1`, `*.sh`, `*.bat`

## Working with AI Assistants

### Before Starting Work

1. **Check current state**:
   ```bash
   git status
   git log --oneline -5
   ```

2. **Verify branch**:
   - Ensure you're on the correct feature branch
   - Branch should start with `claude/`

3. **Understand context**:
   - Read relevant documentation
   - Check for related issues or PRs
   - Review recent commits

### During Development

1. **Use Todo Tracking**:
   - Break complex tasks into smaller steps
   - Track progress with TodoWrite tool
   - Mark tasks as in_progress/completed

2. **Code Quality**:
   - Follow established conventions
   - Add appropriate comments and documentation
   - Ensure no security vulnerabilities (XSS, SQL injection, etc.)
   - Validate input and sanitize output

3. **Testing**:
   - Write unit tests for new functionality
   - Ensure existing tests pass
   - Add integration tests where appropriate

### After Completing Work

1. **Review Changes**:
   ```bash
   git status
   git diff
   ```

2. **Commit Guidelines**:
   - Clear, descriptive commit messages
   - Logical grouping of changes
   - Reference related issues/tasks

3. **Push to Remote**:
   ```bash
   git push -u origin <branch-name>
   ```

## Build and Test

### Expected Build Commands

Once the project structure is established:

```bash
# Restore dependencies
dotnet restore

# Build the solution
dotnet build

# Run tests
dotnet test

# Build for release
dotnet build --configuration Release
```

### Pre-commit Checks

Before committing, ensure:
- [ ] Code compiles without errors
- [ ] All tests pass
- [ ] No new warnings introduced
- [ ] Code follows style guidelines
- [ ] Documentation updated if needed

## Environment Setup

### Development Container

The project aims to provide a fully pinned development environment. Expected setup:

1. **Docker**: Container runtime
2. **VS Code**: With Remote-Containers extension
3. **Visual Studio**: Windows development IDE
4. **.NET SDK**: Specific version to be pinned
5. **Build Tools**: MSBuild, NuGet

### Environment Variables

Store sensitive configuration in `.env` files (gitignored):
- API keys
- Connection strings
- Service credentials

## Common Tasks

### Adding a New Feature

1. Understand the requirement
2. Create todo list for implementation steps
3. Write tests first (TDD approach)
4. Implement the feature
5. Update documentation
6. Commit and push

### Fixing a Bug

1. Reproduce the bug
2. Write a failing test that demonstrates the bug
3. Fix the issue
4. Verify the test passes
5. Check for similar issues elsewhere
6. Commit with descriptive message

### Updating Documentation

1. Identify what needs documentation
2. Write clear, concise explanations
3. Include code examples where helpful
4. Update CLAUDE.md if workflow changes
5. Commit documentation separately

## Security Considerations

- Never commit secrets or credentials
- Use `.env` files for local secrets (gitignored)
- Validate all user input
- Sanitize output to prevent XSS
- Use parameterized queries to prevent SQL injection
- Keep dependencies updated
- Review security advisories for used packages

## File Reference Patterns

When referencing code locations, use: `file_path:line_number`

Example:
- Configuration is loaded in `src/config/AppConfig.cs:45`
- Main entry point at `src/Program.cs:12`

## Troubleshooting

### Common Issues

1. **Build failures**: Check NuGet package restoration
2. **Test failures**: Verify test dependencies and configuration
3. **Git push failures**: Ensure branch name follows conventions
4. **Missing dependencies**: Run `dotnet restore`

### Getting Help

- Check project documentation in `docs/`
- Review commit history for similar changes
- Consult Visual Studio output/error windows
- Check build logs in `MSBuild_Logs/`

## Project Evolution

This is a new project in its initial setup phase. As development progresses:

1. **Add concrete examples** of code patterns
2. **Document actual build processes** once established
3. **Update architecture** as structure emerges
4. **Add troubleshooting** for specific issues encountered
5. **Include performance** considerations
6. **Document deployment** procedures

## Questions to Clarify

As an AI assistant working on this project, consider asking:

1. What is the primary purpose of the development container?
2. Which Visual Studio version should be pinned?
3. What .NET SDK versions are required?
4. Are there specific NuGet packages that should always be included?
5. What testing framework should be used?
6. Are there CI/CD pipelines to integrate with?
7. What are the deployment targets?

## Additional Resources

- [Visual Studio Documentation](https://docs.microsoft.com/visualstudio/)
- [.NET Documentation](https://docs.microsoft.com/dotnet/)
- [Dev Containers Documentation](https://containers.dev/)
- [Git Best Practices](https://git-scm.com/book/en/v2)

---

**Last Updated**: 2025-11-16
**Status**: Initial version - repository in setup phase
**Maintainer**: AI assistants working with anerb
