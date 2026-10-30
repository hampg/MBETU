from build import read_words,ROOT
from collections import Counter
import json,re
words=read_words();ids={'partial','written','unwritten','fusion','shortening','deletion','none'}
assert len(words)>=2000
assert len({w['word'] for w in words})==len(words)
counts=Counter()
for w in words:
    assert re.fullmatch('[a-záéíóöőúüű]+',w['word']),w['word']
    assert w['answers'] and set(w['answers'])<=ids,w
    assert len(w['answers'])==len(set(w['answers'])),w
    assert set(w['answers'])==set(w['explanations']),w
    assert w['family'] and all(len(e)>30 for e in w['explanations'].values()),w
    counts.update(w['answers'])
for cat in ids:assert counts[cat]>=40,(cat,counts[cat])
index={w['word']:w for w in words}
anchors={'színpad':'partial','népdal':'partial','háztól':'partial','vízzel':'written','anyja':'unwritten','egészség':'unwritten','barátság':'fusion','látja':'fusion','jobbra':'shortening','otthon':'shortening','mondta':'deletion','gondnak':'deletion','alma':'none','toll':'none'}
for word,cat in anchors.items():assert cat in index[word]['answers'],word
for bad in ['játék}+','játékkalal','képban','ködhez','szándékkalal','fogyja','fagyja','alakulják']:
    assert bad not in index,bad
page=(ROOT/'index.html').read_text()
embedded=re.search(r'<script id="word-data" type="application/json">(.*?)</script>',page,re.S)
assert json.loads(embedded.group(1))==words,'Run build: embedded data is out of date'
assert '/*__' not in page
assert '<html lang="hu">' in page
print(f'PASS: {len(words)} unique, structured word forms; {len(set(w["family"] for w in words))} families; category counts {dict(counts)}; offline HTML matches source.')
