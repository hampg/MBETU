const assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm');
const core=require('../src/core.js');
const context=vm.createContext({});
vm.runInContext(fs.readFileSync('src/rules.js','utf8'),context);
vm.runInContext(fs.readFileSync('src/games.js','utf8'),context);
const games=JSON.parse(vm.runInContext('JSON.stringify(GAMES)',context));
assert.equal(games.length,6);
const html=fs.readFileSync('index.html','utf8');
const embedded=JSON.parse(html.match(/<script id="games-data" type="application\/json">(.*?)<\/script>/s)[1]);
let total=0;
for(const game of games.slice(1)){
 const rows=fs.readFileSync(game.bank,'utf8').split('\n').filter(l=>l&&!l.startsWith('#')).map((l,i)=>{
  const[word,answers,explanations,family,solution,context,options]=l.split('\t');const r={word,answers:JSON.parse(answers),explanations:JSON.parse(explanations),family,solution,context,id:`${game.id}-${String(i+1).padStart(3,'0')}`};if(Object.keys(JSON.parse(options)).length)r.options=JSON.parse(options);return r;
 });
 assert(rows.length>=50,game.id);total+=rows.length;
 assert.deepEqual(rows,embedded[game.id],`${game.id}: rebuild index.html after editing its TXT`);
 const ids=game.rules.map(r=>r.id);assert.equal(ids.length,new Set(ids).size);
 for(const r of rows){
  assert(r.context.trim().length>=5);assert(r.solution);assert(r.family);assert(r.answers.length);assert.deepEqual(Object.keys(r.explanations).sort(),[...r.answers].sort());
  for(const a of r.answers){assert(ids.includes(a));assert(r.explanations[a].length>30);assert(core.grade(r,a));}
  if(game.id==='jly'){assert.equal(r.word.split('…').length,2);assert.equal(r.word.replace('…',r.answers[0]),r.solution);}
  if(game.id==='hosszusag'){assert.equal(r.word.split('…').length,2);assert.equal(r.word.replace('…',r.options[r.answers[0]]),r.solution);assert.notEqual(r.options.short,r.options.long);}
  if(game.id==='hibakereso')assert.equal(r.word===r.solution,r.answers[0]==='correct');
  if(game.id==='egybeiras'){const clean=r.word.split(/\s*\+\s*/);assert.equal(clean.join(r.answers[0]==='one'?'':r.answers[0]==='apart'?' ':'-'),r.solution);}
 }
 for(const id of ids)assert(rows.some(r=>r.answers.includes(id)),`${game.id} missing ${id}`);
 for(const count of [1,7,20,rows.length,rows.length+10]){const deck=core.makeDeck(rows,ids,count);assert.equal(deck.length,Math.min(count,rows.length));assert.equal(new Set(deck.map(r=>r.id)).size,deck.length);}
 for(const id of ids){const deck=core.makeDeck(rows,[id],20);assert(deck.every(r=>r.answers.includes(id)));}
}
// Identical gap text can have distinct, meaningful contexts (hal/hall, tíz/tűz).
const duplicates=embedded.hosszusag.filter(r=>r.word==='ha…');assert(duplicates.length>=2);const deck=core.makeDeck(duplicates,['short','long'],duplicates.length);assert.equal(deck.length,duplicates.length);
assert(total>=600);assert(!html.includes('/*__'));
console.log(`PASS: 5 new games, ${total} contextual tasks, gap reconstruction, answer keys, distinct task IDs, per-game filtering and full-deck sampling.`);
