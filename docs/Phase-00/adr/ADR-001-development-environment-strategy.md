# ADR-001 — Development Environment Strategy

## Status

Accepted

## Date

2026-07-15

## Context

The project requires a stable and reproducible Python development environment for a long-term MLOps engineering roadmap.

The initial approach considered using a project-local virtual environment managed directly by UV. However, the development machine has an important infrastructure constraint:

- The C: drive is protected with Deep Freeze.
- Local virtual environments created on the frozen drive may be removed after system restart.
- Recreating the environment repeatedly would introduce unnecessary operational overhead.

The project also requires modern Python dependency management, reproducibility, and compatibility with production-oriented workflows.

## Decision

The project will use a hybrid environment strategy:

- Conda will provide the persistent Python runtime environment.
- UV will manage Python project dependencies.
- `pyproject.toml` will be the source of truth for dependencies.
- `uv.lock` will provide dependency reproducibility.

The project will not use `requirements.txt` as the primary dependency management mechanism.

## Consequences

Positive consequences:

- Persistent development environment across system restarts.
- Reproducible dependency installation.
- Modern Python packaging workflow.
- Compatibility with CI/CD and production engineering practices.
- Consistent workflow across AI Agent, Software Engineering, and MLOps projects.

Negative consequences:

- The project uses two tools with different responsibilities:
  - Conda for Python runtime management.
  - UV for dependency management.

This separation requires understanding the role of each tool.

## Alternatives Considered

### Alternative 1 — UV managed .venv

Advantages:
- Native UV workflow.
- Simple dependency management.

Rejected because:
- The local machine infrastructure constraint makes project-local environments unreliable.

### Alternative 2 — Traditional requirements.txt workflow

Advantages:
- Simple and familiar.

Rejected because:
- Less reproducible.
- Does not provide modern dependency locking.
- Not aligned with production Python engineering practices.

## Final Workflow

Initial setup:

1. Create Conda environment.
2. Activate environment.
3. Initialize UV project.
4. Add dependencies using:

```
uv add <package>
```

Development dependencies:

```
uv add --dev <package>
```

After restarting the computer:
- conda activate mlops_env
- uv pip install --group dev
- uv pip install -e .

Validation:
- pytest

The environment strategy will remain consistent throughout the roadmap unless explicitly revisited.