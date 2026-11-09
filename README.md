# Cloud security posture scanner (export-driven)

**Author:** Md Shohrab Hossen Niaz

Analyse cloud resource exports (JSON) for common misconfigurations: public storage, open security groups, missing encryption flags.

```powershell
python -m src.cli scan --path .\fixtures\cloud_inventory.json
```
