Set-Location (Split-Path -Parent $PSScriptRoot)
python -m src.cli scan --path .\fixtures\cloud_inventory.json
python tests\test_smoke.py
