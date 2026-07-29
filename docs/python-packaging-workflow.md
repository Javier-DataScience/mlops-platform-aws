# Python Project Initialization Workflow

## Purpose

Every Python project developed throughout this roadmap should follow a standardized initialization process.

The objective is to create projects that are:

- Reproducible.
- Properly packaged.
- Easily importable.
- Compatible with professional development tools.
- Maintainable throughout their lifecycle.

Following a consistent initialization workflow eliminates many common development issues and provides a solid engineering foundation for Software Engineering, MLOps, Machine Learning Engineering, AI Engineering, and LLM Engineering projects.

---

# Standard Project Structure

All projects should adopt the recommended **src layout**.

Example:

```
project_root/

├── docs/
├── scripts/
├── tests/
├── src/
│   └── my_project/
│       ├── __init__.py
│       ├── module_a.py
│       ├── module_b.py
│       └── ...
│
├── pyproject.toml
├── README.md
└── uv.lock
```

The `src` layout clearly separates project source code from configuration files, documentation, tests, and scripts while preventing accidental imports from the project root.

---

# Project Initialization Workflow

Whenever a new project is created, follow this sequence.

## Step 1 — Create and Activate the Environment

Create or activate the desired Conda environment.

Example:

```
conda activate my_environment
```

---

## Step 2 — Initialize the Project

Initialize the repository using UV.

Example:

```
uv init
```

This creates the initial project structure, including:

- pyproject.toml
- README.md
- .python-version

---

## Step 3 — Configure pyproject.toml

Before installing the project, configure `pyproject.toml` as an installable Python package.

The project metadata under the `[project]` section is **not sufficient** for Python to discover packages inside the `src` directory.

The project must explicitly define:

- The build system.
- Package discovery.
- Source directory mapping.

Example:

```toml
[build-system]
requires = ["setuptools>=61"]
build-backend = "setuptools.build_meta"

[tool.setuptools]
package-dir = {"" = "src"}

[tool.setuptools.packages.find]
where = ["src"]
```

Without these sections, Python may correctly install external dependencies while still failing to locate the project's own package.

---

# Why Package Discovery Is Required

When using a structure such as:

```
src/

└── my_project/
```

Python does not automatically recognize `my_project` as an importable package.

Typical symptoms include:

```
ModuleNotFoundError:
No module named 'my_project'
```

This occurs because Python knows where external libraries are installed but has no information indicating that the source code inside `src` should also be treated as an installable package.

Proper package discovery solves this problem.

---

# Step 4 — Synchronize Dependencies

Install project dependencies.

```
uv sync
```

This synchronizes the environment with the project's dependency definitions.

---

# Step 5 — Install the Project in Editable Mode

Install the current project.

```
uv pip install -e .
```

Editable installation creates a link between the active Python environment and the local source code.

Advantages include:

- Source code changes are immediately reflected.
- No reinstall is required after modifications.
- Imports behave exactly like installed third-party libraries.
- Development and testing remain synchronized.

---

# Step 6 — Verify the Installation

Verify that Python can import the package.

```
uv run python -c "import my_project; print(my_project.__file__)"
```

Expected result:

The command prints the package location.

Unexpected result:

```
ModuleNotFoundError
```

If this error appears, verify:

- pyproject.toml configuration.
- Package discovery.
- Editable installation.
- Active environment.

---

# Expected Import Style

After installation, modules should always be imported naturally.

Example:

```python
from my_project.training.trainer import ModelTrainer
```

Avoid:

- Modifying `sys.path`
- Relative import hacks
- IDE-specific workarounds
- Temporary path manipulation

Natural package imports are the standard used in professional Python projects.

---

# Engineering Checklist

Before beginning development, verify that:

- The project uses the `src` layout.
- `pyproject.toml` includes package discovery.
- The build system is configured.
- Dependencies have been synchronized.
- The project has been installed using:

```
uv pip install -e .
```

- Import verification succeeds.
- No `sys.path` modifications are required.

---

# Common Mistakes

Avoid the following:

- Forgetting to configure package discovery.
- Assuming the `[project]` section is enough.
- Importing modules by modifying `sys.path`.
- Installing dependencies but not installing the project itself.
- Using IDE-specific fixes instead of proper packaging.

---

# Rationale

Treating every project as a proper Python package provides a clean, reproducible, and maintainable engineering workflow.

Using the `src` layout, package discovery, editable installation, and import verification ensures that the project behaves like any professionally developed Python package.

This workflow should be adopted as the standard initialization procedure for every Software Engineering, MLOps, Machine Learning Engineering, AI Engineering, and LLM Engineering project developed throughout this roadmap.