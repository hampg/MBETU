const assert=require('node:assert/strict');
const fs=require('node:fs');
const core=require('../src/core.js');
const {RULES}=require('../src/rules.js');
const words=fs.readFileSync('words.txt','utf8').split('\n').filter(l=>l&&!l.startsWith('#')).map(l=>{const [word,answers,explanations,family]=l.split('\t');return{word,answers:JSON.parse(answers),explanations:JSON.parse(explanations),family};});
const ids=[...RULES.map(r=>r.id),'none'];
let seed=42;const rng=()=>((seed=(seed*1664525+1013904223)>>>0)/4294967296);
for(const size of [1,7,20,100,words.length,words.length+100]){
 const deck=core.makeDeck(words,ids,size,rng);
 assert.equal(deck.length,Math.min(size,words.length));assert.equal(new Set(deck.map(w=>w.word)).size,deck.length);
}
const small=core.makeDeck(words,ids,7,rng);
for(const id of ids)assert(small.some(w=>w.answers.includes(id)),`Missing ${id}`);
for(const id of ids){const deck=core.makeDeck(words,[id],25,rng);assert.equal(deck.length,25);assert(deck.every(w=>w.answers.includes(id)));}
for(const word of words){for(const id of ids)assert.equal(core.grade(word,id),word.answers.includes(id));}
const multi=words.find(w=>w.word==='kulccsal');assert(multi.answers.includes('written'));assert(multi.answers.includes('shortening'));
assert(core.grade(multi,'written'));assert(core.grade(multi,'shortening'));assert(!core.grade(multi,'none'));
assert.deepEqual(core.summary([{correct:true},{correct:false},{correct:true}]),{correct:2,total:3,percent:67});
assert.deepEqual(core.summary([]),{correct:0,total:0,percent:0});
assert.deepEqual(core.makeDeck(words,[],20),[]);
console.log(`PASS: balanced decks, unique questions, category filters, all ${words.length} word × answer combinations, multi-answer grading, scoring.`);
