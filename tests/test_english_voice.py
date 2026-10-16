"""The English training track must always request an English voice."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
catalog = json.loads((root / "curriculum/index.json").read_text(encoding="utf-8"))
lessons = [x for x in catalog["lessons"] if x["language_track"] == "en"]
assert len(lessons) == 10
for meta in lessons:
    src = json.loads((root / meta["file"]).read_text(encoding="utf-8"))
    assert meta["language"] == "en-US", meta["id"]
    assert src["language"] == "en-US", meta["id"]
    assert src["language_track"] == "en", meta["id"]
    assert src["chunks"] and src["chunks"][0]["example"], meta["id"]

html = (root / "index.html").read_text(encoding="utf-8")
assert 'data-lang="${speechLanguage(language)}"' in html
assert "lesson.language=meta.language||obj.language" in html
assert "utterance.voice=matching;" in html
assert "if(!matching){" in html
assert "utterance.rate=1.0;" in html
print("PASS: all 10 English lessons explicitly require en-US and strict voice selection")
