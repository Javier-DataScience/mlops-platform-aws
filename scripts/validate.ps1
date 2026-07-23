Write-Host ""
Write-Host "======================================="
Write-Host " MLOps Engineering Validation Pipeline "
Write-Host "======================================="
Write-Host ""

Write-Host "[1/5] Running Ruff checks..."
ruff check . --fix
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Write-Host "[2/5] Formatting code..."
ruff format .
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Write-Host "[3/5] Running MyPy..."
mypy .
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Write-Host "[4/5] Running Pytest..."
pytest
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Write-Host "[5/5] Running Pre-Commit..."
pre-commit run --all-files
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Write-Host ""
Write-Host "======================================="
Write-Host " Validation completed successfully."
Write-Host "======================================="