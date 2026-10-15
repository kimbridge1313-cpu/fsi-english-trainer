"""Lightweight static PWA checks (no browser dependencies)."""
from pathlib import Path
import json, struct

ROOT = Path(__file__).resolve().parents[1]
page = (ROOT / "index.html").read_text(encoding="utf-8")
sw = (ROOT / "sw.js").read_text(encoding="utf-8")
manifest = json.loads((ROOT / "manifest.webmanifest").read_text(encoding="utf-8"))
curriculum = json.loads((ROOT / "curriculum/index.json").read_text(encoding="utf-8"))
assert manifest["display"] == "standalone"
assert manifest["start_url"] == "/" and manifest["scope"] == "/"
assert 'rel="manifest"' in page and "serviceWorker.register('/sw.js'" in page
assert "ja-JP" in page and "data-track" in page
assert "CACHE_NAME" in sw and "caches.open" in sw
assert "lesson.file" in sw and "cache.addAll(paths)" in sw
assert len(curriculum["lessons"]) >= 10
assert not any(x["id"] == "ja-lesson-02-demonstratives-and-ownership" for x in curriculum["lessons"])
for icon in manifest["icons"] + [{"src": "/icons/apple-touch-icon.png", "sizes": "180x180"}]:
    path = ROOT / icon["src"].lstrip("/")
    data = path.read_bytes()
    assert data.startswith(b"\x89PNG\r\n\x1a\n"), path
    w, h = struct.unpack("!II", data[16:24])
    expected = int(icon["sizes"].split("x")[0])
    assert (w, h) == (expected, expected), (path, w, h)
    print(f"OK {path.relative_to(ROOT)} {w}×{h}")
for lesson in curriculum["lessons"]:
    assert (ROOT / lesson["file"]).is_file(), lesson
print(f"PWA static checks passed: {len(curriculum['lessons'])} lessons.")
