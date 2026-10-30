"""Build an offline-ready single HTML page from the editable source and TSV wordbank."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parent.parent

def read_words():
    rows=[]
    for line in (ROOT/'words.txt').read_text().splitlines():
        if not line or line.startswith('#'):continue
        word,answers,explanations,family=line.split('\t')
        rows.append(dict(word=word,answers=json.loads(answers),explanations=json.loads(explanations),family=family))
    return rows

def read_games():
    banks={}
    for game in ['alapelvek','egybeiras','jly','hosszusag','hibakereso']:
        rows=[]
        for line in (ROOT/'data'/f'{game}.txt').read_text().splitlines():
            if not line or line.startswith('#'):continue
            word,answers,explanations,family,solution,context,options=line.split('\t')
            row=dict(word=word,answers=json.loads(answers),explanations=json.loads(explanations),family=family,solution=solution,context=context,id=f'{game}-{len(rows)+1:03d}')
            if json.loads(options):row['options']=json.loads(options)
            rows.append(row)
        banks[game]=rows
    return banks

def build():
    page=(ROOT/'src/index.template.html').read_text()
    for marker,file in [('CSS','style.css'),('RULES','rules.js'),('GAMES','games.js'),('CORE','core.js'),('APP','app.js')]:
        page=page.replace('/*__'+marker+'__*/',(ROOT/'src'/file).read_text())
    data=json.dumps(read_words(),ensure_ascii=False,separators=(',',':')).replace('<','\\u003c')
    page=page.replace('/*__WORDS__*/',data)
    page=page.replace('/*__BANKS__*/',json.dumps(read_games(),ensure_ascii=False,separators=(',',':')).replace('<','\\u003c'))
    (ROOT/'index.html').write_text(page)
    print(f'index.html: {len(read_words())} words, {len(page.encode())} bytes; works offline')
if __name__=='__main__':build()
