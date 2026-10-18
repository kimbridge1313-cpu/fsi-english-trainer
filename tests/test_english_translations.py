"""English chunk examples must have readable Traditional Chinese translations."""
from pathlib import Path
import json
root = Path(__file__).resolve().parents[1]
index = json.loads((root / "curriculum/index.json").read_text(encoding="utf-8"))
english = [x for x in index["lessons"] if x["language_track"] == "en"]
assert len(english) == 10
count = 0
for x in english:
    lesson = json.loads((root / x["file"]).read_text(encoding="utf-8"))
    for chunk in lesson["chunks"]:
        assert chunk["meaning"].strip() and chunk["usage"].strip()
        assert chunk["example_zh"].strip(), (x["id"], chunk["example"])
        count += 1
assert count == 61, count
page = (root / "index.html").read_text(encoding="utf-8")
assert "聽中文意思" not in page
assert "example-translation" in page
assert "聽中文例句" in page
print(f"PASS: {len(english)} English lessons, {count} translated examples")
