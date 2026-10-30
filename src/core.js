'use strict';
const GameCore=(()=>{
 const shuffle=(list,rng=Math.random)=>{const a=[...list];for(let i=a.length-1;i>0;i--){const j=Math.floor(rng()*(i+1));[a[i],a[j]]=[a[j],a[i]];}return a;};
 function makeDeck(words,ids,count,rng=Math.random){
  const pools=Object.fromEntries(ids.map(id=>[id,shuffle(words.filter(w=>w.answers.includes(id)),rng)]));
  const used=new Set(),familyLast=new Set(),result=[];
  // Körönként egy-egy kategória: a kis kategóriák sem vesznek el a nagy szócsaládok mellett.
  while(result.length<count){let changed=false;
   for(const id of shuffle(ids,rng)){
    const pool=pools[id];
    let index=pool.findIndex(w=>!used.has(w.word)&&!familyLast.has(w.family));
    if(index<0)index=pool.findIndex(w=>!used.has(w.word));
    if(index<0)continue;
    const [word]=pool.splice(index,1);result.push(word);used.add(word.word);familyLast.add(word.family);changed=true;
    if(familyLast.size>14)familyLast.delete(familyLast.values().next().value);
    if(result.length===count)break;
   }
   if(!changed)break;
  }return result;
 }
 const grade=(word,answer)=>word.answers.includes(answer);
 const summary=answers=>({total:answers.length,correct:answers.filter(a=>a.correct).length,percent:answers.length?Math.round(100*answers.filter(a=>a.correct).length/answers.length):0});
 return{shuffle,makeDeck,grade,summary};
})();
if(typeof module!=='undefined')module.exports=GameCore;
