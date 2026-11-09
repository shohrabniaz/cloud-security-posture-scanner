from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.scanner import scan

def test_finds_issues():
    res = scan(ROOT / "fixtures" / "cloud_inventory.json")
    assert res["critical"] >= 1
    assert res["finding_count"] >= 3

if __name__ == "__main__":
    test_finds_issues(); print("smoke_ok")
