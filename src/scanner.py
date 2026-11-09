from __future__ import annotations
import json
from pathlib import Path

def scan(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    findings = []
    for b in data.get("storage", []):
        if b.get("public"):
            findings.append({"resource": b.get("name"), "type": "storage", "issue": "public_bucket", "severity": "high"})
        if not b.get("encryption", True):
            findings.append({"resource": b.get("name"), "type": "storage", "issue": "unencrypted", "severity": "high"})
    for sg in data.get("security_groups", []):
        for rule in sg.get("ingress", []):
            if rule.get("cidr") in {"0.0.0.0/0", "::/0"} and int(rule.get("port", 0)) in {22, 3389, 3306, 5432}:
                findings.append({
                    "resource": sg.get("name"),
                    "type": "security_group",
                    "issue": f"open_admin_port_{rule.get('port')}",
                    "severity": "critical",
                })
    for db in data.get("databases", []):
        if db.get("public"):
            findings.append({"resource": db.get("name"), "type": "database", "issue": "public_database", "severity": "critical"})
        if not db.get("encryption", True):
            findings.append({"resource": db.get("name"), "type": "database", "issue": "unencrypted", "severity": "high"})
    return {
        "finding_count": len(findings),
        "critical": sum(1 for f in findings if f["severity"] == "critical"),
        "high": sum(1 for f in findings if f["severity"] == "high"),
        "findings": findings,
    }
