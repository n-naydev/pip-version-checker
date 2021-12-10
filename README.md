# pip-version-checker

A python package to check whether requied python package versions are outdated (there exist newer version in pypi)

# Usage

## As binary
pip_version_check

## As pre-commit hook
Add this in your .pre-commit-config.yaml
```yaml
  - repo: ../pip-version-checker
    rev: 615526dee4e0208d7478109eae1747ea7264a836
    hooks:
      - id: pip-version-check
        always_run: true
        verbose: true
        args: ['--filename', 'requirements.txt']
        stages: [push]
```
