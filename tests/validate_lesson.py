import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
index = json.loads((root / 'curriculum/index.json').read_text(encoding='utf-8'))
assert index['lessons']

for meta in index['lessons']:
    lesson = json.loads((root / meta['file']).read_text(encoding='utf-8'))
    assert lesson['id'] == meta['id']
    assert len(lesson['chunks']) >= 5
    subs = lesson['drills']['substitution']
    assert '____' in subs['pattern']
    for item in subs['items']:
        assert item['cue'].strip() and item['answer'].strip()
        assert item['answer'] == subs['pattern'].replace('____', item['cue'])
    assert all(len(x['steps']) >= 3 for x in lesson['drills']['buildup']['items'])
    assert len(lesson['drills']['response']['rates']) == 3
    assert len(lesson['conversation']['rounds']) == 3
    for rd in lesson['conversation']['rounds']:
        assert rd['pairs'] and all(p['a'] and p['b'] for p in rd['pairs'])
print('PASS: lesson JSON structures and substitution strings')
