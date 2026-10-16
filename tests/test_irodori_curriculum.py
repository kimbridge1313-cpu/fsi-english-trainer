"""Irodori starter catalog and audio controls regression tests."""
from pathlib import Path
import json
r=Path(__file__).resolve().parents[1]
m=json.loads((r/'curriculum/index.json').read_text(encoding='utf8'))
en=[l for l in m['lessons'] if l['language_track']=='en']
ja=[l for l in m['lessons'] if l['language_track']=='ja']
assert len(en)==10 and len(ja)==18
assert sorted(l['lesson_number'] for l in ja)==list(range(1,19))
for l in ja:
 d=json.loads((r/l['file']).read_text(encoding='utf8'))
 assert d['language']=='ja-JP' and d['language_track']=='ja' and len(d['chunks'])>=5
 assert all(c['example_zh'] for c in d['chunks'])
 assert d['drills']['response']['rates']==[1,1,1]
 assert all(rd['rate']==1 and rd['pairs'] for rd in d['conversation']['rounds'])
assert all(l['status']=='review' for l in ja[3:])
html=(r/'index.html').read_text(encoding='utf8')
assert "meaning&&activeTrack!=='ja'?" in html
assert "c.example_zh&&activeTrack!=='ja'?" in html
assert "q.a_zh&&activeTrack!=='ja'?" in html
assert "activeTrack==='ja'&&q.cue_language==='zh-TW'" in html
assert "lesson.language=meta.language||obj.language" in html
assert 'utterance.rate=1.0;' in html
print('PASS: 10 English + 18 Japanese, JA-only playback controls, locale fallback and fixed speed')
