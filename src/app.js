'use strict';
(()=>{
const $=id=>document.getElementById(id);
const words=JSON.parse($('word-data').textContent), allRules=[...RULES,NONE], ids=allRules.map(r=>r.id);
const rule=id=>allRules.find(r=>r.id===id);
const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const fmt=n=>n.toLocaleString('hu-HU');
// Original geometric marks with lighter strokes and open negative space.
const iconPaths={
 partial:'<path d="M53 12A48 48 0 0 0 53 108M67 12A48 48 0 0 1 67 108" fill="none" stroke="currentColor" stroke-width="12"/><path d="M47 12H59V108H47Z"/>',
 written:'<path d="M44 22 10 60 44 98M76 22 110 60 76 98M14 60H106" fill="none" stroke="currentColor" stroke-width="12"/>',
 unwritten:'<path d="M12 24H104L92 36H12ZM12 54H104L92 66H12ZM12 84H104L92 96H12Z"/>',
 fusion:'<path d="M60 8V112M8 60H112M23 23 97 97M23 97 97 23" fill="none" stroke="currentColor" stroke-width="12"/>',
 shortening:'<path d="M5 60H87M58 26 92 60 58 94M108 18V102" fill="none" stroke="currentColor" stroke-width="12"/>',
 deletion:'<path d="M51 11H69V29H51ZM15 83H33V101H15ZM87 83H105V101H87Z"/><path d="M51 90H69V94H51Z" opacity=".28"/>'
};
const iconMarkup=id=>`<svg viewBox="0 0 120 124" fill="currentColor" xmlns="http://www.w3.org/2000/svg" focusable="false" aria-hidden="true">${iconPaths[id]}</svg>`;

let mode='practice', deck=[],position=0,answered=false,answers=[],practiceIds=[...ids],practiceCorrect=0,practiceTotal=0,streak=0,reviewAnswers=[],mistakePractice=false;
let drag=null,ghost=null;
function announce(text){$('route-notice').textContent=text;}
function choices(target){$(target).innerHTML=allRules.map(r=>`<label class="category-option"><input type="checkbox" value="${r.id}" checked> ${esc(r.name)}</label>`).join('');}
document.querySelector('.skip-link').addEventListener('click',e=>{e.preventDefault();$('main').focus();});
choices('practice-categories');choices('test-categories');
$('boxes').innerHTML=RULES.map((r,i)=>`<div class="box-wrap ${r.color}" data-rule="${r.id}"><div class="box-label"><button type="button" class="label-title" aria-describedby="tip-${r.id}" aria-label="${esc(r.name)}: magyarázat">${esc(r.name)}</button><span class="tooltip" role="tooltip" id="tip-${r.id}">${esc(r.tip)}</span><kbd aria-hidden="true">${i+1}</kbd></div><button type="button" class="drop-box" data-answer="${r.id}" aria-label="${i+1}. ${esc(r.name)}"><span class="box-no" aria-hidden="true">0${i+1}</span><span class="box-symbol" aria-hidden="true">${iconMarkup(r.id)}</span><span class="box-state"></span></button></div>`).join('');
$('help-toc').innerHTML=RULES.map((r,i)=>`<a href="#szabaly-${r.id}">0${i+1} ${esc(r.name)}</a>`).join('');
$('rules-content').innerHTML=RULES.map((r,i)=>`<article class="rule-article" id="szabaly-${r.id}"><span class="rule-index">0${i+1}</span><div><h2>${esc(r.name)}</h2><p class="rule-tip">${esc(r.tip)}</p><p>${esc(r.body)}</p><p>${esc(r.detail)}</p></div><div class="rule-examples"><p>ÍRJUK → EJTJÜK / ALAKÍTJUK</p>${r.examples.map(e=>`<div class="example-row"><div class="example-change"><span>${esc(e[0])}</span><span class="arrow">→</span><strong>${esc(e[1])}</strong></div><p>${esc(e[2])}</p></div>`).join('')}<p class="rule-source"><a href="https://helyesiras.mta.hu/helyesiras/default/akh12" target="_blank" rel="noopener noreferrer">Forrás: ${esc(r.source)} ↗</a></p></div></article>`).join('');
$('sources-list').innerHTML=SOURCES.map(s=>`<div class="source-link"><a href="${esc(s.url)}" target="_blank" rel="noopener noreferrer">${esc(s.title)} ↗</a><p>${esc(s.note)}</p></div>`).join('');
$('word-count').textContent=`${fmt(words.length)} SZÓALAK · 6 SZABÁLY`;
$('wordbank-detail').textContent=`A szóbank ${fmt(words.length)} különböző szóalakot tartalmaz, ${fmt(new Set(words.map(w=>w.family)).size)} szócsaládba rendezve. A szám ragozott alakokat is tartalmaz, nem ennyi külön szótövet jelent.`;
function selected(target){return Array.from($(target).querySelectorAll('input:checked'),e=>e.value);}
function available(selectedIds){return words.filter(w=>w.answers.some(c=>selectedIds.includes(c))).length;}
function updateAvailable(){const n=available(selected('test-categories'));$('available-count').textContent=`Ezekkel a beállításokkal ${fmt(n)} különböző szóalakból választhatsz (1–${fmt(n)} kérdés).`;$('question-count').max=n;}
$('test-categories').addEventListener('change',updateAvailable);updateAvailable();
function startPractice(pool=words){mode='practice';position=0;answered=false;deck=GameCore.makeDeck(pool,practiceIds,pool.length);if(!deck.length){practiceIds=[...ids];deck=GameCore.makeDeck(pool,practiceIds,pool.length);}renderWord();}
function renderWord(){
 cancelDrag();answered=false;
 const w=deck[position];if(!w)return;
 $('current-word').textContent=w.word;
 $('word-card').className='word-card';$('word-card').disabled=false;
 $('word-card').setAttribute('aria-label',`Aktuális szó: ${w.word}. Válassz egy dobozt vagy húzd bele a szót.`);
 $('feedback').hidden=true;$('feedback').textContent='';$('next').hidden=true;
 const isTest=mode==='test';
 $('scores').hidden=isTest;$('test-progress').hidden=!isTest;$('progress-track').hidden=!isTest;$('skip').hidden=isTest;
 $('mode-label').textContent=isTest?'TESZT FOLYAMATBAN':mistakePractice?'HIBÁS SZAVAK GYAKORLÁSA':'SZABAD GYAKORLÁS';
 $('game-eyebrow').textContent=isTest?'02 / MOST RAJTAD A SOR':'01 / A SZÓ A TIÉD';
 $('game-title').innerHTML=isTest?'Most hallgasd.<br><span>Most már tudod.</span>':'Hallgasd fejben.<br><span>Tedd a helyére.</span>';
 $('filter-toggle').hidden=isTest;$('multi-note').textContent=isTest?'A teszt közben nem mutatjuk a megoldást. Egy szóért egy pont jár; több elfogadott kategóriánál bármelyik helyes válasz jó.':'Több törvényt is felismertél? Ha a szó több kategóriába tartozik, bármelyik helyes dobozt elfogadjuk.';
 if(isTest){$('test-progress').textContent=`${position+1} / ${deck.length} szó`;$('progress-fill').style.width=`${position/deck.length*100}%`;$('practice-filters').hidden=true;}
 document.querySelectorAll('[data-answer]').forEach(b=>{b.disabled=false;b.classList.remove('correct-answer','wrong-answer','selected-answer','drag-over');const state=b.querySelector('.box-state');if(state)state.textContent='';if(b.classList.contains('drop-box')){const r=rule(b.dataset.answer);b.setAttribute('aria-label',`${ids.indexOf(r.id)+1}. ${r.name}`);}});
 $('none-answer').hidden=!isTest&&!practiceIds.includes('none');
 document.querySelectorAll('.box-wrap').forEach(wrap=>{const active=isTest||practiceIds.includes(wrap.dataset.rule);wrap.hidden=!active;});
 $('correct-count').textContent=practiceCorrect;$('streak-count').textContent=streak;
}
function submit(answer){
 if(answered||!deck[position]||$('game-view').hidden)return;
 if(mode==='practice'&&!practiceIds.includes(answer))return;
 answered=true;cancelDrag();const word=deck[position],correct=GameCore.grade(word,answer);
 const selectedButton=document.querySelector(`[data-answer="${answer}"]`);
 document.querySelectorAll('[data-answer]').forEach(b=>b.disabled=true);
 $('word-card').classList.add('locked');
 if(mode==='test'){
  answers.push({word,answer,correct});selectedButton.classList.add('selected-answer');
  const state=selectedButton.querySelector('.box-state');if(state)state.textContent='VÁLASZTOTTAD';
  $('feedback').className='feedback';$('feedback').innerHTML='<strong>Válasz rögzítve.</strong>A megoldást és a magyarázatot a teszt végén nézheted meg.';
 }else{
  practiceTotal++;if(correct){practiceCorrect++;streak++;}else streak=0;
  $('correct-count').textContent=practiceCorrect;$('streak-count').textContent=streak;
  $('word-card').classList.add(correct?'correct':'incorrect');selectedButton.classList.add(correct?'correct-answer':'wrong-answer');
  word.answers.forEach(id=>{const b=document.querySelector(`[data-answer="${id}"]`);if(!b)return;b.classList.add('correct-answer');const label=b.querySelector('.box-state');if(label)label.textContent='✓ HELYES';});
  const reason=word.explanations[correct?answer:word.answers[0]];
  $('feedback').className=`feedback ${correct?'good':'bad'}`;
  $('feedback').innerHTML=`<strong>${correct?'Ez az, jó helyre került!':'Ezt most tegyük a helyére.'}</strong>${esc(reason)}${word.answers.length>1?`<br>Elfogadott kategóriák: ${word.answers.map(c=>esc(rule(c).name)).join(' · ')}.`:''} <a href="#szabaly-${word.answers[0]==='none'?'none':word.answers[0]}">Miért? ↗</a>`;
 }
 $('feedback').hidden=false;$('skip').hidden=true;$('next').hidden=false;
 $('next').innerHTML=mode==='test'&&position===deck.length-1?'Mutasd az eredményt <span aria-hidden="true">↗</span>':'Következő szó <span aria-hidden="true">→</span>';
}
document.querySelectorAll('[data-answer]').forEach(b=>b.addEventListener('click',()=>submit(b.dataset.answer)));
$('next').addEventListener('click',()=>{
 if(!answered)return;
 if(mode==='test'&&position===deck.length-1){reviewAnswers=[...answers];showResults();return;}
 position++;if(position>=deck.length){if(mistakePractice){mistakePractice=false;startPractice();}else startPractice();}else renderWord();
 $('word-card').focus({preventScroll:true});
});
$('skip').addEventListener('click',()=>{position++;if(position>=deck.length)startPractice();else renderWord();});
$('filter-toggle').addEventListener('click',()=>{const open=$('practice-filters').hidden;$('practice-filters').hidden=!open;$('filter-toggle').setAttribute('aria-expanded',String(open));});
$('apply-filter').addEventListener('click',()=>{const next=selected('practice-categories');if(!next.length){$('filter-error').textContent='Válassz legalább egy kategóriát.';return;}practiceIds=next;mistakePractice=false;$('filter-error').textContent='';$('practice-filters').hidden=true;$('filter-toggle').setAttribute('aria-expanded','false');startPractice();});
$('test-form').addEventListener('submit',e=>{
 e.preventDefault();const cats=selected('test-categories'),count=Number($('question-count').value),max=available(cats);
 if(!cats.length){$('test-error').textContent='Válassz legalább egy kategóriát.';return;}
 if(!Number.isInteger(count)||count<1||count>max){$('test-error').textContent=`A kérdésszám 1 és ${max} közötti egész szám lehet.`;return;}
 $('test-error').textContent='';deck=GameCore.makeDeck(words,cats,count);position=0;answers=[];mode='test';mistakePractice=false;
 location.hash='teszt-folyamatban';route();renderWord();window.scrollTo({top:0,behavior:'instant'});announce(`${count} kérdéses teszt elindult.`);
});
document.querySelectorAll('[data-count]').forEach(b=>b.addEventListener('click',()=>{$('question-count').value=b.dataset.count;document.querySelectorAll('[data-count]').forEach(x=>x.classList.toggle('chosen',x===b));}));
$('question-count').addEventListener('input',()=>{document.querySelectorAll('[data-count]').forEach(b=>b.classList.toggle('chosen',b.dataset.count===$('question-count').value));});
function showResults(){
 const sum=GameCore.summary(reviewAnswers);$('result-percent').textContent=`${sum.percent}%`;$('result-fraction').textContent=`${sum.correct} / ${sum.total} helyes válasz`;
 $('result-caption').textContent=sum.percent===100?'Telitalálat! Minden szó a helyére került.':sum.percent>=70?'Sok minden megvan már. A bizonytalan szavakat még gyakoroljuk át.':'Minden körrel közelebb kerülsz. Nézzük meg a magyarázatokat, és próbáld újra!';
 $('retry-mistakes').hidden=sum.correct===sum.total;$('only-errors').checked=false;
 $('category-results').innerHTML=allRules.map(r=>{const matching=reviewAnswers.filter(a=>a.word.answers.includes(r.id));if(!matching.length)return '';return `<div class="category-result"><span>${esc(r.name)}</span><strong>${matching.filter(a=>a.correct).length} / ${matching.length}</strong></div>`;}).join('');
 renderReview();try{localStorage.setItem('mbetu-last-test',JSON.stringify({...sum,date:new Date().toISOString()}));}catch(_){}
 location.hash='eredmeny';route();window.scrollTo({top:0,behavior:'instant'});announce(`A teszt eredménye ${sum.percent} százalék, ${sum.correct} helyes válasz ${sum.total} szóból.`);
}
function renderReview(){
 const filtered=reviewAnswers.filter(a=>!$('only-errors').checked||!a.correct);
 $('answer-review').innerHTML=filtered.length?filtered.map(a=>{
 const index=reviewAnswers.indexOf(a)+1;
 return `<article class="review-item ${a.correct?'good':'bad'}"><div class="review-top"><h3>${esc(a.word.word)}</h3><span>${index}. SZÓ · ${a.correct?'✓ HELYES':'✕ JAVÍTANDÓ'}</span></div><p class="answer-label">A válaszod: <strong>${esc(rule(a.answer).name)}</strong></p><p>Elfogadott: <strong>${a.word.answers.map(c=>esc(rule(c).name)).join(' / ')}</strong></p>${a.word.answers.map(c=>`<p class="explanation">${esc(a.word.explanations[c])}</p>`).join('')}<a class="rule-link" href="#szabaly-${a.word.answers[0]}">Megnézem a szabályt ↗</a></article>`;
 }).join(''):'<p class="empty-review">Nincs hibás válasz. Minden szó a helyére került!</p>';
}
$('only-errors').addEventListener('change',renderReview);
$('retry-mistakes').addEventListener('click',()=>{const pool=reviewAnswers.filter(a=>!a.correct).map(a=>a.word);practiceIds=[...ids];document.querySelectorAll('#practice-categories input').forEach(c=>c.checked=true);mistakePractice=true;startPractice(pool);location.hash='gyakorlas';route();});
$('export-results').addEventListener('click',()=>{const s=GameCore.summary(reviewAnswers);const lines=[`MBETŰ – Teszteredmény: ${s.correct}/${s.total} (${s.percent}%)`,'',...reviewAnswers.flatMap((a,i)=>[`${i+1}. ${a.word.word} – ${a.correct?'HELYES':'HIBÁS'}`,`Válasz: ${rule(a.answer).name}`,`Elfogadott: ${a.word.answers.map(c=>rule(c).name).join(' / ')}`,...a.word.answers.map(c=>a.word.explanations[c]),''])];download('mbetu-eredmeny.txt',lines.join('\n'));});
function download(name,text){const url=URL.createObjectURL(new Blob(['\ufeff'+text],{type:'text/plain;charset=utf-8'})),a=document.createElement('a');a.href=url;a.download=name;document.body.append(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(url),1000);}
function route(){
 cancelDrag();let hash=decodeURIComponent(location.hash.slice(1))||'gyakorlas';let view='game-view',nav='gyakorlas';
 if(hash==='teszt'){view='test-view';nav='teszt';try{const s=JSON.parse(localStorage.getItem('mbetu-last-test'));if(s&&Number.isInteger(s.total)&&s.total>0&&Number.isInteger(s.correct)&&Number.isInteger(s.percent)){$('last-test').textContent=`Legutóbbi teszted ezen az eszközön: ${s.correct}/${s.total} helyes válasz (${s.percent}%).`;$('last-test').hidden=false;}}catch(_){}}
 else if(hash==='eredmeny'&&reviewAnswers.length){view='results-view';nav='teszt';}
 else if(hash==='sugo'||hash.startsWith('szabaly-')){view='help-view';nav='sugo';}
 else if(hash==='teszt-folyamatban'&&mode==='test'&&deck.length){nav='teszt';}
 else{if(mode!=='practice'){mistakePractice=false;startPractice();}hash='gyakorlas';}
 for(const id of ['game-view','test-view','results-view','help-view'])$(id).hidden=id!==view;
 document.querySelectorAll('[data-nav]').forEach(a=>{const active=a.dataset.nav===nav;a.classList.toggle('active',active);if(active)a.setAttribute('aria-current','page');else a.removeAttribute('aria-current');});
 if(hash.startsWith('szabaly-')){const target=hash==='szabaly-none'?document.querySelector('.help-extra'):$(hash);if(target)requestAnimationFrame(()=>target.scrollIntoView({behavior:'instant'}));}
 else window.scrollTo({top:0,behavior:'instant'});
 document.title=`MBETŰ — ${nav==='sugo'?'Szabálykönyv':nav==='teszt'?'Teszteld magad':'Hallgasd fejben. Tedd a helyére.'}`;
}
window.addEventListener('hashchange',route);
document.addEventListener('keydown',e=>{
 if(e.key==='Escape'){cancelDrag();document.querySelectorAll('.box-label').forEach(l=>l.classList.add('suppressed'));return;}
 if($('game-view').hidden||e.ctrlKey||e.altKey||e.metaKey||/INPUT|TEXTAREA|SELECT/.test(e.target.tagName))return;
 if(/^[1-7]$/.test(e.key)&&!answered){e.preventDefault();submit(ids[Number(e.key)-1]);}
 if(e.key==='Enter'&&answered&&e.target.tagName!=='BUTTON'&&e.target.tagName!=='A'){e.preventDefault();$('next').click();}
});
document.querySelectorAll('.label-title').forEach(b=>{b.addEventListener('mouseenter',()=>b.parentElement.classList.remove('suppressed'));b.addEventListener('focus',()=>b.parentElement.classList.remove('suppressed'));});
function cancelDrag(){
 if(ghost)ghost.remove();ghost=null;drag=null;
 $('word-card').classList.remove('drag-source');document.querySelectorAll('.drag-over').forEach(b=>b.classList.remove('drag-over'));
}
const card=$('word-card');
card.addEventListener('pointerdown',e=>{
 if(answered||e.button!==0)return;
 drag={x:e.clientX,y:e.clientY,id:e.pointerId,moved:false};card.setPointerCapture(e.pointerId);
});
card.addEventListener('pointermove',e=>{
 if(!drag||e.pointerId!==drag.id)return;
 if(!drag.moved&&Math.hypot(e.clientX-drag.x,e.clientY-drag.y)>7){drag.moved=true;ghost=document.createElement('div');ghost.className='drag-ghost';ghost.textContent=deck[position].word;ghost.setAttribute('aria-hidden','true');document.body.append(ghost);card.classList.add('drag-source');}
 if(!drag.moved)return;
 ghost.style.left=`${e.clientX}px`;ghost.style.top=`${e.clientY}px`;
 const target=document.elementFromPoint(e.clientX,e.clientY)?.closest('[data-answer]');document.querySelectorAll('[data-answer]').forEach(b=>b.classList.toggle('drag-over',b===target&&!b.disabled));
});
card.addEventListener('pointerup',e=>{
 if(!drag)return;const moved=drag.moved;const target=document.elementFromPoint(e.clientX,e.clientY)?.closest('[data-answer]');cancelDrag();
 if(card.hasPointerCapture(e.pointerId))card.releasePointerCapture(e.pointerId);
 if(moved&&target&&!target.disabled)submit(target.dataset.answer);
});
card.addEventListener('pointercancel',cancelDrag);card.addEventListener('lostpointercapture',cancelDrag);window.addEventListener('blur',cancelDrag);
startPractice();route();
})();
