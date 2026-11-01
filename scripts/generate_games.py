"""Saját szerkesztésű feladatbankok az öt helyesírási játékhoz.
A változatok helyett önálló, ellenőrizhető példák; minden tételhez javítás jár.
"""
from pathlib import Path
import json,collections
ROOT=Path(__file__).resolve().parent.parent
banks={k:[] for k in ['alapelvek','egybeiras','jly','hosszusag','hibakereso']}
def add(game,word,answer,explanation,solution=None,context='',family=None,options=None):
    row=dict(word=word,answers=[answer],explanations={answer:explanation},family=family or solution or word,solution=solution or word,context=context)
    if options:row['options']=options
    row['id']=f'{game}-{len(banks[game])+1:03d}'
    banks[game].append(row)
# J / LY: a célbetűt rejtjük el, nem a teljes szóalakot.
jwords='ajak ajtó baj bajusz bejárat bója cserje csevej csukja díj ejt ejtőernyő éj éjjel faj fajta fej fejedelem fejel fejsze fejt felejt haj hajnal hajó hajt héja ifjú ijed ijedelem ijeszt jég jeges jegy jegyzet jel jelen jelmez jelvény jobb jog jó jókedv jósol játék játszik javít jármű jár járda jászol jövedelem július június juh juhász jutalom kajak karaj kijárat lejt lejtő majom máj majd majonéz muszáj óhaj olaj papagáj pajta pajzs raj rajt rajzol rejt rejtvény robaj rojt sajt sajnál saját sóhaj sújt száj szomjazik táj tajték talaj tej tejföl teljesít tolvaj tojáshéj tojás új újra ujjas ujj ujjong vaj vajon váj zaj zajos zörej zsivaj'.split()
jwords=[w for w in jwords if '?' not in w]
lywords='akadály bagoly bivaly boly bolygó boglya csigolya csekély erkély esély fogoly folyadék folyamat folyik folyosó furulya gally gereblye gólya hely helyes helyzet hólyag ibolya ilyen karvaly kastély kedély keselyű király királyfi komoly korcsolya kristály kölyök lyuk lyukas lyukaszt mély milyen moly mosoly mosolyog nyavalya osztály olykor olyan pálya pelyhes pehely persely pocsolya pólya ragály rejtély sekély selyem sirály sólyom súly súlyos szabály szabályos személy szeszély tartály tavaly tengely uszály ünnepély veszély veszélyes vályú zsindely zsöllye'.split()
contexts={'hely':'Azt mondjuk meg vele, hol állhat vagy ülhet valaki.','boly':'A hangyák lakóhelyének neve.','sújt':'Valakit csapással érint vagy büntet.','ujj':'A kéz egyik része.','új':'Nem régi, hanem most készült.','fejt':'A keresztrejtvényt oldja meg.','faj':'Élőlények rendszertani csoportja.'}
for group,letter in [(jwords,'j'),(lywords,'ly')]:
    for w in group:
        assert letter in w,(w,letter)
        display=w.replace(letter,'…',1)
        context=contexts.get(w,'A hiány helyére j vagy ly kerül. A többi betű változatlan.')
        add('jly',display,letter,f'A helyes alak: {w}. Ebben a szóban a [j] hangot {letter} betűvel jelöljük. A szócsalád írásképe segít a megjegyzésben.',w,context,w)
# Rövid / hosszú: a betűpárt és a jelentést minden tételben rögzítjük.
length_rows='''híd|í|i|í|Építmény a folyó két partja között.
víz|í|i|í|Ezt isszuk, ha szomjasak vagyunk.
tűz|ű|ü|ű|Égés közben fényt és hőt ad.
fű|ű|ü|ű|Zöld növényzet a réten.
út|ú|u|ú|Ezen közlekedünk.
nyúl|ú|u|ú|Hosszú fülű állat.
lúd|ú|u|ú|A liba másik neve.
kút|ú|u|ú|Vizet lehet húzni belőle.
szív|í|i|í|A vért keringető szerv.
szín|í|i|í|Például piros vagy kék.
ír|í|i|í|Betűket vet a papírra.
íz|í|i|í|Az étel egyik érzékelhető tulajdonsága.
sír|í|i|í|Könnyezik.
tíz|í|i|í|A kilencet követő szám.
tízes|í|i|í|A tíz számnév -es képzős alakja.
húsz|ú|u|ú|A tizenkilencet követő szám.
húszas|ú|u|ú|A húsz számnév -as képzős alakja.
hús|ú|u|ú|Állati eredetű élelmiszer.
húz|ú|u|ú|Magához közelít valamit.
húg|ú|u|ú|Fiatalabb lánytestvér.
búza|ú|u|ú|Gabonaféle.
túró|ú|u|ú|Tejtermék.
szúnyog|ú|u|ú|Csípő rovar.
bújik|ú|u|ú|Elrejtőzik.
új|ú|u|ú|Nem régi.
úszik|ú|u|ú|Vízben halad.
kíván|í|i|í|Szeretne valamit.
kívül|í|i|í|Nem belül.
szíves|í|i|í|Kedves, készséges; a szívesen szó alapja.
bízik|í|i|í|Reméli, hogy valaki megbízható.
dicsér|i|i|í|Elismerően beszél valakiről.
nyit|i|i|í|Kinyitja az ajtót.
visz|i|i|í|Magával szállít valamit.
hiszen|i|i|í|Magyarázatot bevezető kötőszó.
tizenegy|i|i|í|A tízet követő szám.
huszadik|u|u|ú|A húsz sorszámnévi alakja.
ugrik|u|u|ú|Elrugaszkodik a földtől.
fut|u|u|ú|Gyors léptekkel halad.
furulya|u|u|ú|Fúvós hangszer.
ujj|u|u|ú|A kéz egyik része.
bunda|u|u|ú|Állat szőrzete vagy meleg ruhadarab.
szurok|u|u|ú|Sűrű, sötét, ragacsos anyag.
füzet|ü|ü|ű|Iskolai írószer, lapokkal.
fül|ü|ü|ű|Hallószerv.
függöny|ü|ü|ű|Az ablak elé akasztott textília.
tükör|ü|ü|ű|Megnézhetjük benne az arcunkat.
külön|ü|ü|ű|Nem együtt.
születik|ü|ü|ű|Világra jön.
szünet|ü|ü|ű|Rövid pihenő két tanóra között.
küzd|ü|ü|ű|Harcot vív vagy erőfeszítést tesz.
küld|ü|ü|ű|Eljuttat valamit valakihez.
fürge|ü|ü|ű|Gyors mozgású.
üdül|ü|ü|ű|Pihenéssel tölti a szabadságát.
sűrű|ű|ü|ű|Sok részből áll kis helyen; nem ritka.
gyűrű|ű|ü|ű|Ujjon viselt ékszer.
gyűjt|ű|ü|ű|Összeszed több dolgot.
fűz|ű|ü|ű|Például cipőbe cipőfűzőt vezet.
szűr|ű|ü|ű|Szitán vagy szűrőn átenged.
bűn|ű|ü|ű|Súlyos erkölcsi vétség.
űr|ű|ü|ű|A világűr szavunk önálló főnévi eleme.
együtt|tt|t|tt|Nem külön-külön.
fütty|tty|ty|tty|Az ajakkal keltett éles hang.
meggy|ggy|gy|ggy|Savanykás, piros gyümölcs.
könny|nny|ny|nny|Szemünkből kicsorduló folyadék.
gally|lly|ly|lly|Vékony faág.
rossz|ssz|sz|ssz|Nem jó.
hosszú|ssz|sz|ssz|Nagy a hossza.
asszony|ssz|sz|ssz|Felnőtt nő.
friss|ss|s|ss|Nem állott.
lassú|ss|s|ss|Nem gyors.
kisebb|s|s|ss|A kicsi középfoka; kiejtése megtévesztő lehet.
egyik|gy|gy|ggy|A több közül egy; kiejtése megtévesztő lehet.
utána|n|n|nn|Nem előtte, hanem őt követően.
lesz|sz|sz|ssz|A jövőre utaló igealak.
javít|v|v|vv|Kijavít egy hibát.
elem|l|l|ll|Egy szerkezet alkotórésze.
szalag|l|l|ll|Keskeny textilcsík.
állat|ll|l|ll|Élőlény, például a kutya.
állomás|ll|l|ll|Itt áll meg a vonat.
illat|ll|l|ll|Kellemes szag.
reggel|gg|g|gg|A nap eleje.
orr|rr|r|rr|A szaglás szerve.
toll|ll|l|ll|Írószer; tintával fog.
tol|l|l|ll|Nem húz, hanem maga előtt mozdít.
szál|l|l|ll|Egy vékony darab, például egy szál virág.
száll|ll|l|ll|A madár a levegőben halad.
hall|ll|l|ll|Érzékeli a hangot.
hal|l|l|ll|Vízben élő állat.
sakk|kk|k|kk|Táblás stratégiai játék.
csepp|pp|p|pp|Kis mennyiségű folyadék.
koppan|pp|p|pp|Rövid, kemény hangot ad.
csillag|ll|l|ll|Fénylő égitest.
csillog|ll|l|ll|Apró fényeket ver vissza.
csíp|í|i|í|Például a szúnyog teszi.
csík|í|i|í|Keskeny sáv.
csirke|i|i|í|Fiatal háziszárnyas.
csukló|u|u|ú|A kéz és az alkar közötti ízület.
szomorú|ú|u|ú|Bánatos.
keserű|ű|ü|ű|Nem édes, például a cukrozatlan kakaó íze.
savanyú|ú|u|ú|A citrom jellegzetes íze.
'''
for line in length_rows.strip().splitlines():
    w,target,short,long,ctx=line.split('|');a='long' if target==long else 'short';masked=w.replace(target,'…',1)
    add('hosszusag',masked,a,f'A helyes alak: {w}. A hiányzó betű itt {target}: {"hosszú" if a=="long" else "rövid"} hangot jelöl. A megadott jelentéshez ezt az írásképet használjuk.',w,ctx,w,{'short':short,'long':long})
# Alapelvek: a megfigyelendő részletet megadjuk, nem állítunk kizárólagosságot egy teljes szóról.
principles={
'phonetic':('A tő önálló, köznyelvi alakjának hangjelölését figyeld.', 'Az önálló tő köznyelvi hangalakját tükröző betűket írjuk: a kiejtés szerinti írásmódot figyeljük.', 'alma asztal ceruza kapu kutya macska róka iskola táska óra hajó madár virág udvar kert patak papír ruha szoba lámpa'),
'analysis':('A kiejtés változása ellenére megőrzött szóelemeket figyeld.', 'Az írás megőrzi a szóelemek felismerhető alakját, bár az érintkező mássalhangzók a beszédben módosulhatnak: a szóelemzés elve érvényesül.', 'barátság látja adja anyja hagyjuk tanulja egészség község népdal színpad háztól kézhez ablakban jobbra otthon varrt mondta gondnak kertje partja'),
 'tradition':('A j hang jelölését vagy a régi családnévi írásképet figyeld.', 'A jelölt részlet hagyományos írásmódú: a mai kiejtés önmagában nem dönti el ezt a betűválasztást.', 'bagoly gólya király mosoly veszély súly hely mély osztály szabály folyik gally pehely sólyom harkály személy tavaly Széchenyi Kossuth Batthyány'),
 'simplify':('A hosszú többjegyű betű vagy a három azonos betű rövidített írását figyeld.', 'A kettőzött többjegyű betűnek csak az első jegyét ismételjük, illetve a toldalékoláskor találkozó három azonos betűt kettőre egyszerűsítjük: az egyszerűsítés elvét gyakoroljuk.', 'kulccsal jeggyel mésszel rosszal meggyel könnyel hosszabb loccsan meggy fütty könny asszony briddzsel eddzük tollal orra nagyobban hallak vádlottól füttyel')}
for a,(ctx,ex,ws) in principles.items():
    for w in ws.split():add('alapelvek',w,a,f'A megadott részletben: {ex}',w,ctx,w)
# Egybeírás: minden tétel konkrét jelentést/szerkezetet rögzít.
join_rows='''vas + út|one|vasút|A vonatok közlekedési pályája, egy fogalom neve.
napra + forgó|one|napraforgó|A sárga virágú olajnövényt nevezzük meg.
kéz + írás|one|kézírás|Valakinek a saját, kézzel írt betűformái.
könyv + tár|one|könyvtár|Könyvek kölcsönzésére és olvasására szolgáló intézmény.
iskola + táska|one|iskolatáska|Az iskolai felszerelés tárolására szolgáló táska neve.
víz + csepp|one|vízcsepp|Egy cseppnyi víz, összetett főnévként.
hó + ember|one|hóember|Hóból épített emberalak.
nap + fény|one|napfény|A Napból érkező fény összetett főnévi neve.
hold + fény|one|holdfény|A Hold felől érkező fény megnevezése.
kerék + pár|one|kerékpár|Kétkerekű jármű neve.
tűz + oltó|one|tűzoltó|A tüzet hivatásszerűen oltó személy foglalkozása.
fog + orvos|one|fogorvos|A fogakat gyógyító szakorvos neve.
szem + üveg|one|szemüveg|Látást javító, orron viselt eszköz neve.
házi + orvos|one|háziorvos|Az alapellátásban dolgozó orvos foglalkozási megnevezése.
piros + paprika|one|pirospaprika|Őrölt fűszer neve, nem egy friss paprika színét mondjuk meg.
gyors + vonat|one|gyorsvonat|A menetrendben szereplő vonattípus neve.
jelző + lámpa|one|jelzőlámpa|A közlekedést irányító készülék neve.
sok + szög|one|sokszög|Mértani alakzat szakkifejezése.
barát + füle|one|barátfüle|Lekváros tésztaétel neve.
négy + szög|one|négyszög|Négy oldalú síkidom neve.
el + olvas|one|elolvas|Az igekötő közvetlenül az ige előtt áll, ugyanahhoz az igéhez tartozik.
meg + ír|one|megír|Az igekötő közvetlenül az ige előtt áll.
ki + nyit|one|kinyit|Az igekötő közvetlenül az ige előtt áll.
be + lép|one|belép|Az igekötő közvetlenül az ige előtt áll.
át + kel|one|átkel|Az igekötő közvetlenül az ige előtt áll.
piros + alma|apart|piros alma|Egy alma színét nevezzük meg egyszerű minőségjelzővel.
magas + ház|apart|magas ház|Egy ház magasságát jellemezzük.
hideg + víz|apart|hideg víz|A víz hőmérsékletét jelöljük.
friss + kenyér|apart|friss kenyér|A kenyér frissességéről beszélünk.
üres + pohár|apart|üres pohár|Egy pohár állapotát nevezzük meg.
régi + könyv|apart|régi könyv|A könyv korára utalunk, egyszerű jelzős kapcsolatban.
öt + perc|apart|öt perc|Időtartamot mondunk meg számnévvel.
három + diák|apart|három diák|A diákok számát adjuk meg.
nyolc + óra|apart|nyolc óra|Időpontot vagy időtartamot nevezünk meg, nem összetett szót.
kéz + alatt|apart|kéz alatt|Névutós szókapcsolatot írunk.
fa + mellett|apart|fa mellett|Egy tárgy helyzetét fejezzük ki névutóval.
ház + előtt|apart|ház előtt|Névutós szókapcsolatot írunk.
olvassa + el|apart|olvassa el|Az igekötő az ige után áll.
írd + meg|apart|írd meg|Az igekötő az ige után áll.
nyisd + ki|apart|nyisd ki|Az igekötő az ige után áll.
el + fogja + olvasni|apart|el fogja olvasni|Az igekötő és a hozzá tartozó ige közé másik szó kerül.
meg + kell + írni|apart|meg kell írni|Az igekötő és az ige közé a kell szó kerül.
ki + szeretne + menni|apart|ki szeretne menni|Az igekötő és az ige közé másik szó kerül.
gyors + vonat|apart|gyors vonat|Egyszerű minőségjelzős szerkezetként csak a vonat sebességét jellemezzük.
sok + szög|apart|sok szög|Nagy mennyiségű fémszögről beszélünk, nem mértani alakzatról.
alig + alig|hyphen|alig-alig|Szóismétléssel azt fejezzük ki: csak nagyon nehezen.
néha + néha|hyphen|néha-néha|Ritkán ismétlődő eseményt fejezünk ki szóismétléssel.
messze + messze|hyphen|messze-messze|A nagy távolságot szóismétléssel hangsúlyozzuk.
egy + egy|hyphen|egy-egy|Néhány darabról, alkalmanként egyről beszélünk.
más + más|hyphen|más-más|Azt fejezzük ki: mindig más.
sok + sok|hyphen|sok-sok|A nagy mennyiséget szóismétléssel hangsúlyozzuk.
ki + ki|hyphen|ki-ki|Azt jelenti: mindenki a maga részéről.
süt + főz|hyphen|süt-főz|Összekapcsolt tevékenységeket jelentő mellérendelő összetétel.
jön + megy|hyphen|jön-megy|Két összekapcsolt mozgást jelentő mellérendelő összetétel.
ide + oda|hyphen|ide-oda|Két irányt összefogó mellérendelő összetétel.
oda + vissza|hyphen|oda-vissza|Két ellentétes irányt foglalunk egységbe.
apraja + nagyja|hyphen|apraja-nagyja|A közösség minden tagját összefoglaló összetétel.
kézzel + lábbal|hyphen|kézzel-lábbal|Az erőteljes tiltakozás módját megnevező állandósult kapcsolat.
örökkön + örökké|hyphen|örökkön-örökké|Állandósult szóismétlés, nyomatékos jelentéssel.
réges + régi|hyphen|réges-régi|Módosult alakú szóismétléssel a régi voltát hangsúlyozzuk.
éjjel + nappal|hyphen|éjjel-nappal|Megállás nélkül, minden napszakban: állandósult mellérendelő összetétel.
'''
for line in join_rows.strip().splitlines():
    word,a,sol,ctx=line.split('|')
    # Ugyanaz a betűsor eltérő kontextusban külön feladat. A deck kulcsa is egyedi.
    display=word
    ex={'one':'A megadott jelentésben összetett szót alkot, illetve az igekötő közvetlenül az igéhez kapcsolódik.','apart':'A megadott szerkezetet különírjuk.','hyphen':'Ezt a szóismétlést vagy mellérendelő összetételt kötőjellel írjuk.'}[a]
    add('egybeiras',display,a,f'A helyes alak ebben a jelentésben: {sol}. {ex}',sol,ctx,sol)
# Hibakereső: mindkét kategória valódi feladat, a javítás csak válasz után látszik.
for i,r in enumerate(banks['jly']):
    if i%2:continue
    sol=r['solution'];a=r['answers'][0]
    if sol in ['hely','boly','fejt','sújt','faj']:continue
    wrong=sol.replace(a,'ly' if a=='j' else 'j',1)
    for word,answer in [(sol,'correct'),(wrong,'fix')]:
        if any(x['word']==word for x in banks['hibakereso']):continue
        add('hibakereso',word,answer,f'{"Helyes" if answer=="correct" else "Javítandó"}: a megfelelő íráskép {sol}. A [j] hangot ebben a szóban {a} betű jelöli.',sol,r['context'],sol)
for i,r in enumerate(banks['hosszusag']):
    if i%3:continue
    correct=r['answers'][0];sol=r['solution'];right=r['options'][correct];other=r['options']['short' if correct=='long' else 'long'];wrong=sol.replace(right,other,1)
    for word,answer in [(sol,'correct'),(wrong,'fix')]:
        if any(x['word']==word for x in banks['hibakereso']):continue
        add('hibakereso',word,answer,f'A megadott jelentéshez tartozó helyes alak: {sol}. A célbetű {right}; a másik hosszúság ebben a feladatban nem megfelelő.',sol,r['context'],sol)
# Bővített, szerkesztett készlet és kiegyensúlyozott hibakereső.
from expanded_content import expand_all
expand_all(banks,add)
for game,rows in banks.items():
    lines=['# MBETŰ – '+game+'; UTF-8 TSV; saját szerkesztés', '# feladat\tválaszok_JSON\tmagyarázatok_JSON\tszócsalád\tmegoldás\tkontextus\tbetűválaszték_JSON']
    for r in rows:lines.append('\t'.join([r['word'],json.dumps(r['answers'],ensure_ascii=False),json.dumps(r['explanations'],ensure_ascii=False),r['family'],r['solution'],r['context'],json.dumps(r.get('options',{}),ensure_ascii=False)]))
    (ROOT/'data'/f'{game}.txt').write_text('\n'.join(lines)+'\n')
print({k:len(v) for k,v in banks.items()},'total',sum(map(len,banks.values())))
