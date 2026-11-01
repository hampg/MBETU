"""Saját szerkesztésű bővítőanyag. A szócsaládok tudatosan megadottak,
nem általános ragozási szabállyal előállított mesterséges szóalakok.
"""
from collections import defaultdict, deque

JLY_GROUPS='''akadály|ly|akadályoz akadályozás akadálytalan akadálymentes akadálypálya akadályfutás
bagoly|ly|bagolyfióka gyöngybagoly macskabagoly fülesbagoly
bivaly|ly|bivalycsorda bivalyborjú bivalyerős
boly|ly|hangyaboly bolyhos bolyong bolyongás felbolydul
bolygó|ly|bolygórendszer bolygómozgás kisbolygó
boglya|ly|szénaboglya boglyas
csigolya|ly|csigolyák csigolyatörés csigolyaközi
csekély|ly|csekélység csekélyke
esély|ly|esélyes esélytelen esélyegyenlőség esélyegyenlőtlenség
fogoly|ly|fogolytábor hadifogoly hadifogolytábor fogolymadár
folyik|ly|folyó folyás folyton folytonos folytonosság folyóirat folyékony befolyás lefolyó vízfolyás folyópart folyószámla folyamatosság
furulya|ly|furulyás furulyázik furulyaszó furulyaművész
gally|ly|gallyaz gallyazás rőzsegally
gereblye|ly|gereblyéz gereblyézés gereblyefog
gólya|ly|gólyafészek gólyaláb gólyahír gólyatábor
hely|ly|helyiség helyesírás helyesírási helytelen helytelenít helyettes helyettesít helyez helyezés helyreállít helyszín helyrajz lakóhely munkahely búvóhely ülőhely állóhely játszóhely szülőhely
hólyag|ly|hólyagos vízhólyag hólyagpapír
ibolya|ly|ibolyakék ibolyaszín ibolyaillat
király|ly|királyi királynő királyság királylány királyné királyfi királyválasztás
komoly|ly|komolyság komolytalan komolytalanság
korcsolya|ly|korcsolyázik korcsolyázás korcsolyapálya korcsolyázó jégkorcsolya
kristály|ly|kristályos kristálytiszta kristálycukor kristályvíz
kölyök|ly|kölyökkutya kölyökmacska farkaskölyök
lyuk|ly|lyukad lyukadás lyukasztó lyukasztás kulcslyuk egérlyuk gomblyuk
mély|ly|mélység mélyít mélyül mélyedés mélyföld mélypont elmélyül
moly|ly|molylepke molyirtó molyrágta könyvmoly
mosoly|ly|mosolyogva mosolyodás mosolygós mosolytalan mosolygás elmosolyodik
osztály|ly|osztályoz osztályzat osztályfőnök osztálytárs osztályterem osztálykirándulás
pálya|ly|pályázat pályázik pályaudvar pályamű pályakezdő futópálya sportpálya sínpálya
pehely|ly|pehelykönnyű pehelypaplan hópehely tollpehely
persely|ly|perselypénz malacpersely perselyez
pocsolya|ly|pocsolyás pocsolyavíz
pólya|ly|pólyás bepólyál pólyázik
ragály|ly|ragályos
rejtély|ly|rejtélyes rejtélyesség
selyem|ly|selymes selyemkendő selyemhernyó selyemszál
sirály|ly|sirálycsapat sirályfióka
sólyom|ly|solymász solymászat vándorsólyom
súly|ly|súlytalan súlytalanság súlypont súlyemelő testsúly túlsúly súlyzó súlyzós súlymérés egyensúly
szabály|ly|szabálytalan szabálytalanság szabályzat szabályoz szabályozás játékszabály szabályszerű
személy|ly|személyes személyiség személytelen személyzet személyautó személyvonat személyazonosság
szeszély|ly|szeszélyes szeszélyesség
tartály|ly|víztartály üzemanyagtartály tartálykocsi
tengely|ly|tengelyes tengelykapcsoló keréktengely
ünnepély|ly|ünnepélyes ünnepélyesség ünnepélyesen
veszély|ly|veszélytelen veszélyeztet veszélyeztetés veszélyhelyzet életveszély vészhelyzet
vályú|ly|itatóvályú vályús
zsindely|ly|zsindelyes zsindelytető
baj|j|bajos bajnok bajnokság bajtárs bajtársi bajvívó
bejárat|j|átjáró kijáró lejárat feljáró átjárhatatlan
bója|j|jelzőbója bójázik
cserje|j|cserjés cserjésedik cserjeszint
díj|j|díjas díjaz díjazás díjtalan díjkiosztó ösztöndíj tandíj
éj|j|éjszaka éjszakai éjfél éjféli éjjelente éjjeli
faj|j|faji fajta fajgazdag állatfaj növényfaj
fej|j|fejes fejetlen fejléc fejsérülés fejdísz fejbőr fejtető fejfedő fejfájás fejlődés fejlődik
felejt|j|felejtés felejthetetlen elfelejt
haj|j|hajas hajszál hajviselet hajvágás hajmosás hajfonat hajcsat hajkefe hajnalodik hajnalban
hajó|j|hajós hajózik hajózás hajógyár hajóút vitorláshajó hajóskapitány
hajt|j|hajtás hajtó hajtogat hajtogatás hajtómű meghajtó
ifjú|j|ifjúság ifjúsági ifjúkor
ijed|j|ijedt ijedtség ijedős ijesztő ijesztget megijed
jég|j|jegesedés jéghegy jégkocka jégpálya jégcsap jégverés jégkrém jégvirág
jegy|j|jegyzetel jegyzék jegyző jegyzetfüzet jegygyűrű belépőjegy vonatjegy jegypénztár
jel|j|jelöl jelölés jelzés jelző jelleg jelkép jelképes jelenség jelentés jelenet jelölt jelmezbál
jó|j|jóság jóindulat jókedvű jókívánság jótékony jóváhagy
játék|j|játékos játékosság játékbolt játéktér játékszer játszótér játszótárs társasjáték
javít|j|javítás javító javítható kijavít megjavít
jár|j|járás járó járőr járdaszegély járókelő járvány járványos eljárás
jog|j|jogos jogtalan jogász jogi jogosítvány jogszabály jogorvoslat
jut|j|jutalék jutalmaz jutalmazás juttatás
juh|j|juhnyáj juhászat juhtej juhsajt
lejt|j|lejtés lejtős lejtmenet lejtőszög
majom|j|majomkenyérfa majomcsapat
máj|j|májas májkrém májbeteg
olaj|j|olajos olajoz olajozás olajfesték olajfa olajbogyó napraforgóolaj
pajzs|j|pajzsos pajzsmirigy pajzstetű
rajz|j|rajzos rajzolás rajzlap rajzfüzet rajzeszköz rajzfilm rajztanár
rejt|j|rejtés rejtett rejtek rejtekhely rejtőzik rejtőzködés
sajt|j|sajtos sajtkrém sajtkészítés sajtszelet
saját|j|sajátos sajátosság sajátság sajátkezűleg
sóhaj|j|sóhajt sóhajtás felsóhajt sóhajtozik
száj|j|szájas szájüreg szájpadlás szájszél szájharmonika szájvíz
szomj|j|szomj szomjas szomjúság szomjazás
tej|j|tejes tejeskávé tejtermék tejfölös tejbegríz tejpor tejfog tejhab
új|j|újít újítás újdonság újonnan újság újságíró újságos megújul
ujj|j|ujjatlan ujjlenyomat ujjbegy hüvelykujj kisujj
vaj|j|vajas vajaz vajkrém vajtartó
zaj|j|zajtalan zajszint zajong zajongás zajvédelem
'''

def extend_jly(banks,add):
    seen={r['solution'] for r in banks['jly']}
    for line in JLY_GROUPS.strip().splitlines():
        family,letter,ws=line.split('|')
        for w in ws.split():
            if '?' in w or letter not in w or w in seen:continue
            seen.add(w)
            add('jly',w.replace(letter,'…',1),letter,f'A helyes alak: {w}. A célhelyen {letter} betű jelöli a [j] hangot. A(z) {family} szócsaládjának írásképét érdemes együtt megjegyezni.',w,'A hiányzó j vagy ly betűt válaszd ki; a többi betű változatlan.',family)

# szó | célbetű | rövid alak | hosszú alak | jelentés/támpont
LENGTH_EXTRA='''húszat|ú|u|ú|A húsz tárgyragos alakja: húszat számoltunk.
húszan|ú|u|ú|A húsz -an ragos alakja: húszan érkeztek.
tízet|í|i|í|A tíz tárgyragos alakja: tízet kérünk.
tízen|í|i|í|A tíz -en ragos alakja: tízen vannak.
áru|u|u|ú|Eladásra kínált termék, önálló főnév.
árú|ú|u|ú|Valamilyen árat jelentő melléknévi utótag, például kedvező árú.
irt|i|i|í|Kártevőket pusztít; nem az ír ige múlt ideje.
írt|í|i|í|Az ír ige múlt idejű alakja.
kor|o|o|ó|Életkor vagy történelmi időszak.
kór|ó|o|ó|Betegség, főnévként.
koros|o|o|ó|Idősebb életkorú emberre mondjuk.
kóros|ó|o|ó|Beteges, rendellenes állapotot jelöl.
öt|ö|ö|ő|A négyet követő számnév.
őt|ő|ö|ő|Az ő személyes névmás tárgyragos alakja.
tör|ö|ö|ő|Darabokra választ valamit.
tőr|ő|ö|ő|Rövid pengéjű szúrófegyver.
örül|ö|ö|ő|Boldogságot érez.
őrül|ő|ö|ő|Az őrül igét keressük, például megőrül valamitől.
örült|ö|ö|ő|Boldog volt; az örül múlt ideje.
őrült|ő|ö|ő|Tébolyult állapotú, vagy az őrül múlt ideje.
kör|ö|ö|ő|Kerek síkidom.
kőr|ő|ö|ő|A francia kártya piros szív alakú színének neve.
fő|ő|ö|ő|Forrásban levő ételre mondjuk: már készül a leves.
föl|ö|ö|ő|Felfelé jelentésű szóalak, nem a fő ige.
füzetek|ü|ü|ű|A füzet főnév többes száma.
fülek|ü|ü|ű|A fül főnév többes száma.
füles|ü|ü|ű|Füllel ellátott vagy fület viselő.
fülű|ű|ü|ű|Valamilyen füllel rendelkező: hosszú fülű.
füves|ü|ü|ű|Fűvel benőtt területre mondjuk.
füvet|ü|ü|ű|A fű tárgyragos alakja.
füvön|ü|ü|ű|A fű -ön ragos alakja.
fülbevaló|ü|ü|ű|Fülben viselt ékszer.
függ|gg|g|gg|Valami lóg, vagy valamitől függ.
függő|gg|g|gg|Függő helyzetű, illetve valamitől függő.
függőség|gg|g|gg|Valamitől való kóros vagy szoros függés.
függönyös|ü|ü|ű|Függönnyel ellátott.
füst|ü|ü|ű|Égéskor felszálló gáz és apró részecskék.
füstöl|ü|ü|ű|Füstöt bocsát ki.
fütyül|ü|ü|ű|Füttyöt ad, vagy dallamot fúj az ajkával.
füttyent|tty|ty|tty|Egy rövid füttyöt ad.
fürdik|ü|ü|ű|Vízben tisztálkodik vagy fürdőzik.
fürdő|ü|ü|ű|Fürdésre szolgáló helyiség vagy intézmény.
fürt|ü|ü|ű|Egy csomóba nőtt szőlőszemek.
fürtös|ü|ü|ű|Fürtökből álló vagy göndör hajú.
fűrész|ű|ü|ű|Fogazott vágószerszám.
fűrészel|ű|ü|ű|Fűrésszel dolgozik.
fűszer|ű|ü|ű|Az étel ízesítésére használt anyag.
fűszeres|ű|ü|ű|Fűszerrel ízesített.
fűt|ű|ü|ű|Meleget ad a helyiségnek.
fűtés|ű|ü|ű|A helyiség melegítése.
fűző|ű|ü|ű|Kötésre szolgáló zsinór vagy ruhadarab.
szűk|ű|ü|ű|Kevés helyet ad, nem tágas.
szűkít|ű|ü|ű|Keskenyebbé vagy kisebbé tesz.
szűkül|ű|ü|ű|Egyre keskenyebb lesz.
szűrő|ű|ü|ű|Szűrésre használt eszköz.
szűrés|ű|ü|ű|Folyadék vagy más anyag átszűrése.
szüret|ü|ü|ű|A szőlő betakarítása.
szüretel|ü|ü|ű|Szőlőt takarít be.
szükség|ü|ü|ű|Valami iránti igény vagy nélkülözhetetlenség.
szükséges|ü|ü|ű|Olyan, amire szükség van.
szükségtelen|ü|ü|ű|Olyan, amire nincs szükség.
szülő|ü|ü|ű|Az édesanya vagy az édesapa.
szülők|ü|ü|ű|Az édesanya és az édesapa együtt.
születés|ü|ü|ű|Világra jövetel.
sületlen|ü|ü|ű|Még nem sült meg; átvitt értelemben ostoba.
süt|ü|ü|ű|Sütőben ételt készít.
sütő|ü|ü|ű|Étel sütésére szolgáló készülék.
sütemény|ü|ü|ű|Sütéssel készült édes étel.
sűrít|ű|ü|ű|Sűrűbbé tesz.
sűrűség|ű|ü|ű|A sűrű állapot vagy fizikai mennyiség neve.
bűnös|ű|ü|ű|Bűnt elkövető személy.
büntet|ü|ü|ű|Vétségért hátrányt ró valakire.
büntetés|ü|ü|ű|A büntet ige főnévi származéka.
büszke|ü|ü|ű|Örömmel gondol saját vagy más eredményére.
bűvös|ű|ü|ű|Varázslatos.
bűvész|ű|ü|ű|Mutatványokkal szórakoztató előadó.
bűvölet|ű|ü|ű|Elragadtatott, varázslatos hatás.
bűz|ű|ü|ű|Nagyon kellemetlen szag.
hű|ű|ü|ű|Hűséges, ragaszkodó.
hűség|ű|ü|ű|Kitartó ragaszkodás.
hűt|ű|ü|ű|Hidegebbé tesz.
hűtő|ű|ü|ű|Élelmiszer hűtésére szolgáló készülék.
hűl|ű|ü|ű|Egyre hidegebb lesz.
hüledezik|ü|ü|ű|Hitetlenkedve álmélkodik.
hüvelyk|ü|ü|ű|Az egyik ujj neve vagy hosszmérték.
gyűjtemény|ű|ü|ű|Összegyűjtött tárgyak együttese.
gyűjtő|ű|ü|ű|Aki valamit gyűjt.
gyűjtés|ű|ü|ű|Dolgok összeszedése, összegyűjtése.
gyűr|ű|ü|ű|Összenyom, összegyűr valamit.
gyűrött|ű|ü|ű|Összegyűrt állapotú.
gyűrűs|ű|ü|ű|Gyűrűvel ellátott vagy gyűrű alakú.
gyűlölet|ű|ü|ű|Nagyon erős ellenszenv.
nyűg|ű|ü|ű|Terhes kötöttség vagy gond.
nyűgös|ű|ü|ű|Ingerlékeny, nehezen megnyugtatható.
nyüszít|ü|ü|ű|Vékony, panaszos hangot ad, például a kutya.
tűr|ű|ü|ű|Elvisel valamit.
tűrés|ű|ü|ű|Valaminek az elviselése.
türelem|ü|ü|ű|Nyugodt várakozás képessége.
türelmes|ü|ü|ű|Nyugodtan tud várni vagy elviselni valamit.
türelmetlen|ü|ü|ű|Nehezen viseli a várakozást.
tűnik|ű|ü|ű|Látszik valamilyennek, vagy eltűnik.
tündér|ü|ü|ű|Mesebeli lény.
tündököl|ü|ü|ű|Fényesen ragyog.
tűzoltó|ű|ü|ű|Tüzet oltó szakember.
tüzet|ü|ü|ű|A tűz tárgyragos alakja.
tüzes|ü|ü|ű|Tűzzel kapcsolatos vagy heves vérmérsékletű.
tüzek|ü|ü|ű|A tűz többes száma.
tűzben|ű|ü|ű|A tűz -ben ragos alakja.
tüzel|ü|ü|ű|Tüzet rak vagy fegyverből lövéseket ad le.
üzlet|ü|ü|ű|Bolt vagy üzleti megállapodás.
üzem|ü|ü|ű|Termelő munkahely vagy működés.
ügyes|ü|ü|ű|Jól és gyakorlottan végzi a feladatát.
ügy|ü|ü|ű|Elintézendő dolog vagy valamivel kapcsolatos kérdés.
ünnep|ü|ü|ű|Kiemelt, megemlékezésre szánt nap.
ünnepel|ü|ü|ű|Ünnepi eseményen vesz részt.
üreg|ü|ü|ű|Valaminek a belsejében lévő üres rész.
üres|ü|ü|ű|Nincs benne semmi.
üzenet|ü|ü|ű|Valakinek küldött rövid közlés.
űrhajó|ű|ü|ű|A világűrben közlekedő jármű.
űrlap|ű|ü|ű|Kitöltésre szolgáló nyomtatvány.
újság|ú|u|ú|Híreket közlő lap.
újságíró|ú|u|ú|Híreket és cikkeket ír foglalkozásszerűen.
újdonság|ú|u|ú|Valami új dolog.
újít|ú|u|ú|Új megoldást vezet be.
ujjatlan|u|u|ú|Nincs ruhaujja.
ujjlenyomat|u|u|ú|Az ujj bőrének lenyomata.
utca|u|u|ú|Házak között húzódó közterület.
utazik|u|u|ú|Más helyre megy közlekedési eszközzel.
utas|u|u|ú|Járművön utazó személy.
utak|u|u|ú|Az út többes száma.
utat|u|u|ú|Az út tárgyragos alakja.
úton|ú|u|ú|Az út -on ragos alakja.
úti|ú|u|ú|Úttal vagy utazással kapcsolatos melléknév.
útja|ú|u|ú|Az út harmadik személyű birtokos alakja.
urak|u|u|ú|Az úr többes száma.
urat|u|u|ú|Az úr tárgyragos alakja.
úr|ú|u|ú|Felnőtt férfi megszólítása.
úrnak|ú|u|ú|Az úr -nak ragos alakja.
rúd|ú|u|ú|Hosszú, egyenes tárgy.
rudak|u|u|ú|A rúd többes száma.
rudat|u|u|ú|A rúd tárgyragos alakja.
rúdja|ú|u|ú|A rúd birtokos alakja.
ludak|u|u|ú|A lúd többes száma.
ludat|u|u|ú|A lúd tárgyragos alakja.
lúdja|ú|u|ú|A lúd harmadik személyű birtokos alakja.
nyulak|u|u|ú|A nyúl többes száma.
nyulat|u|u|ú|A nyúl tárgyragos alakja.
nyúlós|ú|u|ú|Nyújtható, tapadós állagú.
nyújt|ú|u|ú|Hosszabbá tesz vagy odanyújt valamit.
nyújtás|ú|u|ú|Az izmok megnyújtása.
nyúlik|ú|u|ú|Hosszabbodik.
kutak|u|u|ú|A kút többes száma.
kutat|u|u|ú|Vizsgálódik; a kutat igét keressük.
kútban|ú|u|ú|A kút -ban ragos alakja.
kútja|ú|u|ú|A kút birtokos alakja.
bújócska|ú|u|ú|Elbújással játszott gyermekjáték.
bújtat|ú|u|ú|Elrejt valakit.
bujkál|u|u|ú|Rejtőzködve mozog.
bujdosó|u|u|ú|Bujdosó személyt jelentő szó.
búcsú|ú|u|ú|Elköszönés.
búcsúzik|ú|u|ú|Elköszön valakitől.
bús|ú|u|ú|Szomorú, bánatos.
búsul|ú|u|ú|Szomorkodik.
butul|u|u|ú|Egyre kevésbé értelmesen viselkedik.
buta|u|u|ú|Nem értelmes.
burgonya|u|u|ú|A krumpli másik neve.
bútor|ú|u|ú|Lakás berendezésére szolgáló tárgy.
bútoroz|ú|u|ú|Bútorokkal rendez be egy helyiséget.
futás|u|u|ú|Gyors léptekkel történő haladás.
futó|u|u|ú|Futó személy vagy futásra használt dolog.
futball|u|u|ú|A labdarúgás idegen eredetű neve.
futballista|ll|l|ll|Labdarúgó.
futballozik|ll|l|ll|Labdarúgást játszik.
furcsa|u|u|ú|Szokatlan.
furfang|u|u|ú|Ravasz ötlet vagy csel.
fúr|ú|u|ú|Lyukat készít fúróval.
fúró|ú|u|ú|Lyuk készítésére való szerszám.
fúj|ú|u|ú|Levegőt áramoltat.
fúvós|ú|u|ú|Levegő befújásával megszólaltatott hangszerre mondjuk.
fuvar|u|u|ú|Szállítási megbízás vagy út.
szúrás|ú|u|ú|Hegyes eszközzel okozott sérülés.
szúr|ú|u|ú|Hegyes tárgyat nyom valamibe.
szurkál|u|u|ú|Többször, apró mozdulatokkal szúr.
szurkol|u|u|ú|Egy csapat sikerét kívánja hangosan.
szurkoló|u|u|ú|Csapatot vagy versenyzőt támogató néző.
szúnyogháló|ú|u|ú|A szúnyogok ellen védő háló.
szúrópróba|ú|u|ú|Néhány kiválasztott tétel ellenőrzése.
szurokfekete|u|u|ú|Nagyon sötét, fekete színű.
ússzon|ssz|sz|ssz|Az úszik felszólító módú alakja.
uszoda|u|u|ú|Úszásra alkalmas medencékkel rendelkező létesítmény.
uszonya|u|u|ú|A hal egyik úszószervének birtokos alakja.
uszony|u|u|ú|A hal úszását segítő testrész.
úszó|ú|u|ú|Úszó ember vagy úszó tárgy.
úszás|ú|u|ú|Vízben történő haladás.
húsos|ú|u|ú|Húst tartalmazó.
húsleves|ú|u|ú|Húsból főzött leves.
huszonegy|u|u|ú|A húszat követő szám.
huszonöt|u|u|ú|A huszonnégyet követő szám.
huszár|u|u|ú|Lovas katona hagyományos megnevezése.
húsvét|ú|u|ú|Tavaszi ünnep.
húsvéti|ú|u|ú|Húsvéttal kapcsolatos.
húzás|ú|u|ú|A húz ige főnévi származéka.
húzó|ú|u|ú|Húzásra szolgáló eszköz vagy húzó személy.
hullám|ll|l|ll|A víz felszínének fel-le mozgó alakzata.
hullik|ll|l|ll|Lefelé esik, például a hó.
hulladék|ll|l|ll|Feleslegessé vált anyag.
hulla|ll|l|ll|Elpusztult élőlény teste.
hulló|ll|l|ll|Lefelé eső.
nyíl|í|i|í|Íjjal kilőtt hegyes eszköz.
nyilak|i|i|í|A nyíl többes száma.
nyilat|i|i|í|A nyíl tárgyragos alakja.
nyílik|í|i|í|Kinyílik, például az ajtó vagy a virág.
nyílás|í|i|í|Szabad átjáró egy felületen.
nyír|í|i|í|Ollóval rövidít vagy füvet vág.
nyírás|í|i|í|Haj vagy fű rövidre vágása.
nyílt|í|i|í|Nem zárt.
nyilatkozat|i|i|í|Hivatalos vagy nyilvános közlés.
hidak|i|i|í|A híd többes száma.
hidat|i|i|í|A híd tárgyragos alakja.
hídon|í|i|í|A híd -on ragos alakja.
hídja|í|i|í|A híd harmadik személyű birtokos alakja.
vizet|i|i|í|A víz tárgyragos alakja.
vizek|i|i|í|A víz többes száma.
vizes|i|i|í|Víztől nedves.
vízi|í|i|í|Vízzel kapcsolatos melléknév.
vízben|í|i|í|A víz -ben ragos alakja.
vízmű|í|i|í|Vízellátást biztosító létesítmény.
írás|í|i|í|Betűk és szövegek létrehozása.
író|í|i|í|Könyveket, műveket alkotó személy.
írat|í|i|í|Valakivel írásos feladatot végeztető ige.
irat|i|i|í|Írásos dokumentum, főnév.
iroda|i|i|í|Ügyintézésre szolgáló munkahely.
irodalom|i|i|í|Írott művek összessége vagy iskolai tantárgy.
ígéret|í|i|í|Vállalás arra, hogy valaki megtesz valamit.
ígér|í|i|í|Vállalja, hogy később megtesz valamit.
igaz|i|i|í|Nem hamis.
igazság|i|i|í|A valóságnak megfelelő állítás vagy méltányosság.
igazít|í|i|í|Megfelelő helyre, állapotba tesz.
igyekezik|i|i|í|Törekszik valamire.
ilyen|i|i|í|Ehhez hasonló, efféle.
izgalom|i|i|í|Felfokozott várakozás vagy nyugtalanság.
izom|i|i|í|A mozgást végző testszövet.
izzad|zz|z|zz|Verejtékezik.
izzó|zz|z|zz|Fényt adó vagy nagyon forró tárgy.
illik|ll|l|ll|Megfelelő, elvárt viselkedésre utal.
illem|ll|l|ll|A társas viselkedés szabályai.
illatos|ll|l|ll|Kellemes szagú.
illusztráció|ll|l|ll|Szöveget kísérő szemléltető kép.
ünnepi|nn|n|nn|Ünneppel kapcsolatos.
annyi|nny|ny|nny|Olyan sok, olyan mennyiségű.
ennyi|nny|ny|nny|Ilyen sok, ilyen mennyiségű.
mennyi|nny|ny|nny|Mennyiségre rákérdező szó.
könnyű|nny|ny|nny|Nem nehéz.
könnyes|nny|ny|nny|Könnyel teli, könnytől nedves.
könnyít|nny|ny|nny|Kevésbé nehézzé tesz.
meggyes|ggy|gy|ggy|Meggyet tartalmazó.
meggyleves|ggy|gy|ggy|Meggyből készített leves.
rosszabb|ssz|sz|ssz|A rossz középfoka; az sz hosszúságát figyeld.
rosszabb|bb|b|bb|A rossz középfoka; a fokjel b-jét figyeld.
jobb|bb|b|bb|A jó középfoka.
legjobb|bb|b|bb|A jó felsőfoka.
szebb|bb|b|bb|A szép középfoka.
nagyobb|bb|b|bb|A nagy középfoka.
kisebb|bb|b|bb|A kicsi középfoka; a fokjel b-jét figyeld.
kisebbek|s|s|ss|A kicsi középfokának többes alakja; az s-t figyeld.
magasabb|bb|b|bb|A magas középfoka.
alacsonyabb|bb|b|bb|Az alacsony középfoka.
erősebb|bb|b|bb|Az erős középfoka.
gyengébb|bb|b|bb|A gyenge középfoka.
kevesebb|bb|b|bb|A kevés középfoka.
több|bb|b|bb|A sok középfoka.
legkisebb|s|s|ss|A kicsi felsőfoka; az s-t figyeld.
leszek|sz|sz|ssz|A lesz ige egyes szám első személyű alakja.
lesznek|sz|sz|ssz|A lesz ige többes szám harmadik személyű alakja.
leszünk|sz|sz|ssz|A lesz ige többes szám első személyű alakja.
lassan|ss|s|ss|Lassú módon.
lassít|ss|s|ss|Csökkenti a sebességet.
lassul|ss|s|ss|Csökken a sebessége.
frissen|ss|s|ss|Friss állapotban.
frissít|ss|s|ss|Újabbá, frissebbé tesz.
frissül|ss|s|ss|Újabbá válik.
segít|í|i|í|Támogat valakit egy feladatban.
tanít|í|i|í|Tudást ad át.
javítás|í|i|í|Hiba kijavítása.
veszít|í|i|í|Elveszít valamit vagy alulmarad.
készít|í|i|í|Létrehoz, megalkot valamit.
szépít|í|i|í|Szebbé tesz.
épít|í|i|í|Épületet vagy szerkezetet hoz létre.
díszít|í|i|í|Díszekkel lát el.
szárít|í|i|í|Szárazzá tesz.
borít|í|i|í|Valamit valamire terít vagy lefed.
csípős|í|i|í|Erős, csípő ízű.
csiripel|i|i|í|A kismadár vékony hangon énekel.
csizma|i|i|í|Magas szárú lábbeli.
csinos|i|i|í|Tetszetős külsejű.
bíró|í|i|í|Ítéletet hozó jogász vagy sportmérkőzés vezetője.
bírál|í|i|í|Véleményezi, értékeli valaki munkáját.
bíróság|í|i|í|Igazságszolgáltatási intézmény.
bizalom|i|i|í|Valakinek a megbízhatóságába vetett hit.
biztos|i|i|í|Nem kétséges vagy megbízható.
bizony|i|i|í|Nyomatékosító szó.
bizonyít|í|i|í|Igazolja egy állítás helyességét; az utolsó i hangot figyeld.
kívánság|í|i|í|Valami iránti vágy.
kíváncsi|í|i|í|Szeretne többet megtudni valamiről.
színház|í|i|í|Színpadi előadások helye.
színes|í|i|í|Többféle színnel rendelkező.
színez|í|i|í|Színt ad valaminek.
színező|í|i|í|Kiszínezésre szolgáló rajzok gyűjteménye.
szívesen|í|i|í|Örömmel, készségesen.
sírás|í|i|í|Könnyezéssel járó hangadás.
sima|i|i|í|Nem érdes.
simul|i|i|í|Valamihez hozzálapul vagy simábbá válik.
sípol|í|i|í|Síp hangját adja.
síp|í|i|í|Fúvással megszólaltatható kis eszköz.
tizedik|i|i|í|A tíz sorszámnévi alakja.
tizenöt|i|i|í|A tizennégyet követő szám.
tizenhat|i|i|í|A tizenötöt követő szám.
titok|i|i|í|Mások elől elrejtett információ.
tisztít|í|i|í|Tisztává tesz; a szó végi magánhangzót figyeld.
viszont|i|i|í|Ellentétet vagy más nézőpontot bevezető szó.
vissza|ssz|sz|ssz|Az eredeti hely felé.
visszatér|ssz|sz|ssz|Újra az eredeti helyre megy.
visszhang|ssz|sz|ssz|Visszaverődő hang.
virrad|rr|r|rr|Kivilágosodik az ég.
varr|rr|r|rr|Tűvel és cérnával dolgozik.
varrás|rr|r|rr|Varrással készített öltéssor vagy maga a tevékenység.
forr|rr|r|rr|A folyadék forrásponton van.
forró|rr|r|rr|Nagyon meleg.
forrás|rr|r|rr|Víz felszínre törésének helye vagy a forr ige főnévi alakja.
orrú|rr|r|rr|Valamilyen orral rendelkező: hosszú orrú.
orrsövény|rr|r|rr|Az orrüreget elválasztó rész.
orrlyuk|rr|r|rr|Az orr egyik nyílása.
áll|ll|l|ll|Függőleges helyzetben van.
állít|ll|l|ll|Álló helyzetbe tesz, illetve kijelent valamit.
állapot|ll|l|ll|Valaminek a pillanatnyi helyzete, minősége.
állandó|ll|l|ll|Tartós, nem változó.
állvány|ll|l|ll|Valamit tartó szerkezet.
ellen|ll|l|ll|Valakivel vagy valamivel szemben.
ellenfél|ll|l|ll|A másik oldalon álló versenyző.
ellenőriz|ll|l|ll|Megvizsgálja valaminek a helyességét.
ellát|ll|l|ll|Biztosít valakinek valamit vagy elvégez egy feladatot.
kell|ll|l|ll|Szükségességet kifejező ige.
kellemes|ll|l|ll|Jó érzést keltő.
kellemetlen|ll|l|ll|Rossz érzést keltő.
kolléga|ll|l|ll|Munkatárs.
pillanat|ll|l|ll|Nagyon rövid idő.
pillangó|ll|l|ll|Színes szárnyú rovar.
pillant|ll|l|ll|Rövid ideig valahová néz.
cselló|ll|l|ll|Vonós hangszer.
szellő|ll|l|ll|Enyhe szél.
szellős|ll|l|ll|Jól átjárja a levegő.
szellem|ll|l|ll|Lélek vagy gondolkodó képesség.
szellemes|ll|l|ll|Ötletesen mulatságos.
'''

def extend_length(banks,add):
    seen={(r['word'],r['solution'],r['answers'][0]) for r in banks['hosszusag']}
    priority=set('írat irat tizedik tizenöt huszonegy uszoda uszony bujkál bújócska türelem hüledezik vizet vízi vizes vízben hidat hídon utat úton úti urat rudat ludat nyulat füvet húszat húszan tízet tízen'.split())
    lines=sorted(LENGTH_EXTRA.strip().splitlines(),key=lambda line:line.split('|')[0] not in priority)
    for line in lines:
        w,target,short,long,ctx=line.split('|')
        if '?' in w:continue
        assert target in w,(w,target)
        answer='long' if target==long else 'short'
        gap=w.replace(target,'…',1);key=(gap,w,answer)
        if key in seen:continue
        seen.add(key)
        add('hosszusag',gap,answer,f'A helyes alak: {w}. A hiány helyén {target} áll, vagyis {"hosszú" if answer=="long" else "rövid"} hangot jelölünk. A megadott jelentést is vedd figyelembe.',w,ctx,w,{'short':short,'long':long})
        banks['hosszusag'][-1]['topic']='magánhangzó' if short in 'aeiouöü' else 'mássalhangzó'

# Külön megadott összetételek: a magyarázatok nem a hibás szóalakból következtetnek.
COMPOUNDS='''ablak+párkány|Az ablak alatti vízszintes perem.
ajtó+kilincs|Az ajtó kinyitására szolgáló fogantyú.
ház+tető|A házat felülről fedő szerkezet.
kert+kapu|A kert bejáratát lezáró kapu megnevezése.
konyha+asztal|A konyhában használt asztal fajtaneve.
író+asztal|Íráshoz, tanuláshoz való bútordarab neve.
ruha+szekrény|Ruhák tárolására szolgáló bútor.
könyv+polc|Könyvek tárolására való polc neve.
könyv+jelző|A könyvben az olvasás helyét jelölő eszköz.
könyv+borító|A könyv külső védőrésze.
füzet+borító|A füzet külső védőlapja.
rajz+füzet|Rajzolásra szolgáló füzetfajta.
rajz+lap|Rajzoláshoz használt papírlap neve.
rajz+szög|Rögzítésre szolgáló rövid szög széles fejjel.
író+szer|Íráshoz használt eszközök közös neve.
toll+tartó|Íróeszközök tárolására szolgáló tok.
ceruza+hegyező|A ceruza hegyének kialakítására használt eszköz.
tan+könyv|Egy tantárgy tanulására készített könyv.
munka+füzet|Kitölthető iskolai feladatokat tartalmazó füzet.
tan+terem|Iskolai tanításra használt helyiség.
torna+terem|Testnevelésre és sportolásra szolgáló terem.
iskola+udvar|Az iskola épületéhez tartozó udvar.
iskola+pad|Tanulók ülő- és munkabútora.
osztály+terem|Egy iskolai osztály tanterme.
osztály+társ|Ugyanabba az osztályba járó tanuló.
tanár+nő|Női tanár megnevezése.
tanító+nő|Alsó tagozatos női pedagógus megnevezése.
nap+ernyő|A napsugárzás ellen védő ernyő.
nap+szemüveg|Erős fény ellen védő szemüveg.
eső+kabát|Eső ellen védő ruhadarab neve.
eső+csepp|Az eső egyetlen apró vízrészecskéje.
eső+felhő|Esőt hozó felhő megnevezése.
hó+pehely|A hó egyetlen apró kristályos része.
hó+golyó|Hóból gyúrt gömb alakú játékszer.
hó+vihar|Erős széllel járó havazás.
jég+csap|Lecsepegő vízből kialakuló hegyes jégalakzat.
jég+kocka|Ital hűtésére használt kis jégdarab.
jég+krém|Fagyasztott édesség neve.
víz+part|A víz melletti szárazföldi sáv.
víz+csap|A víz folyását szabályozó szerelvény.
víz+vezeték|Víz szállítására szolgáló csőrendszer.
víz+tartály|Víz tárolására szolgáló tartály megnevezése.
víz+esés|Magasabb helyről lezúduló víz természeti képződménye.
víz+állás|A folyó vagy tó vízszintjének mérhető magassága.
víz+malom|Víz erejével hajtott malom neve.
szél+malom|Szél erejével működő malom.
szél+kerék|Széllel forgatott kerék vagy játék.
szél+vihar|Viharos erősségű szél eseménye.
ég+bolt|A fölöttünk látható ég összefoglaló neve.
csillag+kép|Az égen megkülönböztetett csillagcsoport neve.
csillag+fény|Csillagból érkező fény megnevezése.
világ+űr|Az égitestek közötti kozmikus tér neve.
űr+hajó|Világűrben közlekedő jármű.
űr+állomás|Hosszabb űrbeli tartózkodásra szolgáló létesítmény.
űr+kutatás|A világűr vizsgálatával foglalkozó tevékenység.
vas+kapu|Vasból készült kapu egyszerű anyagnévi megnevezése.
fa+kanál|Fából készült keverőkanál neve.
fa+doboz|Fából készült doboz egyszerű anyagnévi megnevezése.
fa+ház|Fából épített ház egyszerű anyagnévi megnevezése.
üveg+pohár|Üvegből készült pohár egyszerű anyagnévi megnevezése.
üveg+ajtó|Üvegből készült ajtó egyszerű anyagnévi megnevezése.
arany+gyűrű|Aranyból készült gyűrű egyszerű anyagnévi megnevezése.
ezüst+lánc|Ezüstből készült lánc egyszerű anyagnévi megnevezése.
vas+villa|Vasból készült villa vagy mezőgazdasági eszköz neve.
vas+lemez|Vasból készült lemez egyszerű anyagnévi megnevezése.
acél+cső|Acélból készült cső egyszerű anyagnévi megnevezése.
bőr+kabát|Bőrből készült kabát egyszerű anyagnévi megnevezése.
gyapjú+fonal|Gyapjúból készült fonal egyszerű anyagnévi megnevezése.
pamut+ruha|Pamutból készült ruha egyszerű anyagnévi megnevezése.
futó+pálya|Futásra kialakított sportpálya neve.
korcsolya+pálya|Korcsolyázásra kijelölt pálya neve.
úszó+medence|Úszásra épített medencefajta neve.
labda+rúgás|A futball sportág magyar neve.
kézi+labda|Egy csapatsport neve; nem tetszőleges kézben tartott labda.
kosár+labda|A kosárba dobással játszott sportág neve.
röplabda+pálya|A röplabdázásra kijelölt pálya neve.
sport+cipő|Sportoláshoz használt lábbeli.
sport+táska|Sportfelszerelés tárolására használt táska.
hátizsák+pánt|A hátizsák hordását segítő pánt megnevezése.
cipő+fűző|Cipő összekötésére használt zsinór.
cipő+kanál|A cipő felhúzását segítő eszköz.
szem+héj|A szemet takaró mozgó bőrredő.
szem+pilla|A szemhéj szélén nőtt szőrszál.
szem+öldök|A szem fölötti szőrzet megnevezése.
haj+szál|A haj egyetlen szála.
haj+kefe|Haj rendezésére használt kefe.
haj+vágás|A haj rövidítésének neve.
fog+kefe|Fogak tisztítására használt kefe.
fog+krém|Fogmosáshoz használt tisztítóanyag.
fog+mosás|A fogak tisztításának neve.
kéz+mosás|A kéz megtisztításának neve.
kéz+törlő|A kéz megtörlésére használt textília.
kéz+fogás|Kézzel adott üdvözlő mozdulat megnevezése.
láb+nyom|Láb által hagyott nyom.
ujj+lenyomat|Ujj bőrének mintázatát őrző lenyomat.
tej+föl|Savanyított tejtermék neve.
tej+hab|A tejből készített hab megnevezése.
tej+fog|Gyermekkorban kinövő, később kihulló fog neve.
tej+termék|Tejből előállított élelmiszerek összefoglaló neve.
sajt+krém|Kenhető, sajtos élelmiszer neve.
vaj+krém|Kenhető, vaj alapú élelmiszer neve.
hús+leves|Húsból főzött leves neve.
zöldség+leves|Zöldségekből főzött leves neve.
csont+leves|Csont felhasználásával főzött leves neve.
krumpli+leves|Burgonyából főzött leves neve.
gyümölcs+lé|Gyümölcsből készített ital neve.
alma+lé|Almából készített ital neve.
szőlő+lé|Szőlőből készített ital neve.
citrom+héj|A citrom külső burkának megnevezése.
tojás+héj|A tojás külső burka.
kenyér+héj|A kenyér külső, sült rétege.
kenyér+szelet|Egy szelet kenyér összetett főnévi neve.
cukor+répa|Egy cukorgyártásra termesztett növény neve.
paprika+mag|A paprika magjának megnevezése.
barack+mag|A barack magjának megnevezése.
virág+cserép|Virágültetésre szolgáló edény neve.
virág+föld|Virágültetéshez használt földkeverék neve.
virág+szál|Egy szál virág összetett főnévi megnevezése.
fű+szál|Egyetlen vékony fűlevél megnevezése.
fa+levél|A fa levele, összetett főnévként.
fa+ág|A fa egyik elágazó része.
fa+kéreg|A fa törzsét borító külső réteg.
fa+gyökér|A fa talajban lévő része.
madár+fészek|Madár által épített fészek megnevezése.
madár+etető|Madarak etetésére való kis építmény.
madár+hang|A madár által adott hang összetett főnévi neve.
hangya+boly|Hangyák lakóhelye.
méh+kas|Méhek tartására használt kas neve.
pók+háló|Pók által szőtt háló.
csiga+ház|A csiga meszes külső váza.
nyúl+ketrec|Nyúl tartására szolgáló ketrec neve.
állat+kert|Állatok bemutatására fenntartott intézmény.
állat+orvos|Állatokat gyógyító szakember.
mentő+autó|Betegek sürgős szállítására szolgáló jármű neve.
rendőr+autó|A rendőrség szolgálati autójának neve.
postás+táska|Postai küldemények hordására használt táska neve.
posta+láda|Levelek bedobására szolgáló láda.
levél+bélyeg|Postai díj megfizetését igazoló kis értékjegy.
levél+papír|Levelezésre szánt papír neve.
levél+boríték|Levél küldésére használt boríték megnevezése.
vonat+jegy|Vasúti utazásra jogosító jegy.
busz+megálló|Autóbuszok kijelölt megállóhelye.
vasút+állomás|Vonatok megállására és utasforgalomra szolgáló hely.
repülő+tér|Repülőgépek fel- és leszállására szolgáló létesítmény.
járda+szegély|A járda szélét határoló szegély.
út+kereszteződés|Utak találkozásának helye.
'''
ATTRIBUTES='''házi+feladat|Otthonra kiadott iskolai feladat állandósult jelzős megnevezése.
kék+ég|Az ég színét nevezzük meg, egyszerű minőségjelzős kapcsolatban.
zöld+mező|A mező színét nevezzük meg, nem állandósult elnevezést.
fehér+felhő|Egy felhő színét írjuk le.
fekete+cipő|Egy cipő színét nevezzük meg.
sárga+virág|Egy virág színét írjuk le.
barna+kabát|A kabát színére utalunk.
piros+ceruza|A ceruza színét nevezzük meg.
kerek+asztal|Az asztal alakját jellemezzük, nem rendezvényt nevezünk meg.
szögletes+doboz|A doboz alakját írjuk le.
nehéz+táska|A táska tömegét jellemezzük.
könnyű+feladat|A feladat nehézségi fokát nevezzük meg.
nehéz+kérdés|A kérdés nehézségi fokát jellemezzük.
hosszú+mondat|A mondat terjedelmét nevezzük meg.
rövid+szöveg|A szöveg terjedelmét jellemezzük.
érdekes+könyv|Egy könyv tartalmáról mondunk véleményt.
izgalmas+film|A filmet egyszerű minőségjelzővel jellemezzük.
csendes+utca|Az utca zajszintjét írjuk le.
hangos+zene|A zene hangerejét nevezzük meg.
mély+hang|A hang magasságát jellemezzük.
magas+fa|Egy fa magasságát nevezzük meg.
alacsony+kerítés|A kerítés magasságát jellemezzük.
széles+folyó|A folyó szélességét írjuk le.
keskeny+ösvény|Az ösvény szélességét nevezzük meg.
sima+felület|A felület tapintását jellemezzük.
érdes+papír|A papír tapintására utalunk.
meleg+tea|A tea hőmérsékletét nevezzük meg.
forró+leves|A leves hőmérsékletét jellemezzük.
hideg+szoba|A szoba hőmérsékletére utalunk.
édes+alma|Az alma ízét írjuk le.
savanyú+citrom|A citrom ízét jellemezzük.
érett+körte|A körte érettségét nevezzük meg.
nyers+répa|Egy répa elkészítettségi állapotát jellemezzük.
főtt+tojás|Elkészült ételt nevezünk meg jelzős kapcsolatban.
sült+krumpli|Egyszerű jelzős szókapcsolatban beszélünk az ételről.
hasznos+tanács|A tanács értékét jellemezzük.
pontos+válasz|A válasz helyességét, pontosságát nevezzük meg.
ügyes+gyerek|Egy gyereket egyszerű minőségjelzővel jellemzünk.
figyelmes+tanuló|A tanuló egyik tulajdonságát nevezzük meg.
barátságos+szomszéd|Egy szomszéd természetét írjuk le.
vidám+társaság|A társaság hangulatát jellemezzük.
szomorú+történet|A történet hangulatát írjuk le.
nyitott+ablak|Az ablak pillanatnyi állapotát nevezzük meg.
csukott+ajtó|Az ajtó állapotát írjuk le.
tiszta+ruha|A ruha tisztaságát jellemezzük.
sáros+cipő|A cipő pillanatnyi állapotát nevezzük meg.
'''
# előtag | jelen idejű igealak | főnévi igenév | mondatbeli tárgy
PREFIXES='''el|olvassa|olvasni|a történetet
meg|írja|írni|a levelet
ki|nyitja|nyitni|az ablakot
be|csukja|csukni|az ajtót
át|adja|adni|a csomagot
fel|veszi|venni|a kabátot
le|teszi|tenni|a táskát
össze|rakja|rakni|a játékot
szét|szedi|szedni|a szerkezetet
vissza|hozza|hozni|a könyvet
el|viszi|vinni|a dobozt
meg|keresi|keresni|a kulcsot
ki|találja|találni|a megoldást
meg|javítja|javítani|a kerékpárt
fel|rajzolja|rajzolni|az alakzatot
le|rajzolja|rajzolni|a házat
meg|oldja|oldani|a feladatot
meg|főzi|főzni|a levest
meg|süti|sütni|a kenyeret
fel|vágja|vágni|az almát
le|hámozza|hámozni|a krumplit
ki|takarítja|takarítani|a szobát
el|mosogatja|mosogatni|az edényeket
ki|mossa|mosni|a ruhákat
be|rendezi|rendezni|a lakást
át|rendezi|rendezni|a termet
fel|építi|építeni|a tornyot
le|bontja|bontani|a kerítést
el|meséli|mesélni|az élményét
meg|mutatja|mutatni|az eredményt
fel|hívja|hívni|a barátját
le|kapcsolja|kapcsolni|a lámpát
be|kapcsolja|kapcsolni|a számítógépet
fel|tölti|tölteni|a telefont
le|tölti|tölteni|a fájlt
ki|nyomtatja|nyomtatni|a lapot
el|menti|menteni|a szöveget
ki|választja|választani|a képet
össze|gyűjti|gyűjteni|a papírokat
szét|osztja|osztani|a lapokat
be|csomagolja|csomagolni|az ajándékot
ki|bontja|bontani|a csomagot
meg|köszöni|köszönni|a segítséget
meg|tanulja|tanulni|a verset
el|magyarázza|magyarázni|a szabályt
meg|vizsgálja|vizsgálni|a rajzot
ki|javítja|javítani|a hibát
le|másolja|másolni|a mondatot
ki|számolja|számolni|az összeget
össze|hasonlítja|hasonlítani|a két képet
'''
HYPHENS='''előre+hátra|Két ellentétes irányba történő mozgást foglalunk össze.
fel+le|A felfelé és lefelé irányt összefogó mellérendelő összetétel.
ki+be|A kifelé és befelé irányt összefogó kapcsolat.
innen+onnan|Többfelől, különböző helyekről érkező dolgokra utalunk.
itt+ott|Elszórtan, több különböző helyen.
onnan+innen|Két hely felől érkező mozgást összefogó mellérendelés.
égen+földön|Mindenütt keressük: állandósult mellérendelő kapcsolat.
tűzön+vízen|Minden nehézségen keresztül: állandósult kapcsolat.
csillog+villog|Erős, változó csillogást jelentő mellérendelő összetétel.
cseng+bong|Egyszerre csengő és bongó hangot jelölő összetétel.
izeg+mozog|Folyton mozgolódik: állandósult mellérendelő összetétel.
sürög+forog|Szorgosan tevékenykedik: mellérendelő összetétel.
irul+pirul|Zavarában elpirul: állandósult összetétel.
dúl+fúl|Nagyon mérgesen viselkedik: állandósult mellérendelés.
sír+rí|Keservesen sír: összefoglaló mellérendelő összetétel.
esik+kel|Ügyetlenül halad vagy nehézségekkel küzd.
fúr+farag|Két összekapcsolt barkácstevékenység összefoglaló neve.
jár+kel|Különböző helyeken mozog, járkál.
fűt+fát|Mindent ígér: az ígér fűt-fát állandósult kapcsolatának tárgyi része.
kézen+közön|Megmagyarázhatatlanul eltűnik: állandósult határozói összetétel.
szívvel+lélekkel|Teljes odaadással: állandósult mellérendelő kapcsolat.
testi+lelki|A testtel és a lélekkel egyaránt kapcsolatos, összefoglaló mellérendelés.
élő+haló|Valakiért rajongó személyre utaló állandósult mellérendelés.
'''

def extend_join(banks,add):
    seen={(r['word'],r['solution']) for r in banks['egybeiras']}
    def row(parts,a,ctx,reason,family=None,topic=None):
        ws=parts.split('+');sol=({'one':'','apart':' ','hyphen':'-'}[a]).join(ws);display=' + '.join(ws)
        if (display,sol) in seen:return
        seen.add((display,sol))
        add('egybeiras',display,a,f'A helyes alak: {sol}. {reason}',sol,ctx,family or sol)
        banks['egybeiras'][-1]['topic']=topic or ('igekötő' if family else 'összetétel' if a=='one' else 'jelzős' if a=='apart' else 'mellérendelő')
    for shade in ['sötét','világos','halvány']:
        for color in ['kék','zöld','sárga','lila']:
            row(shade+'+'+color,'one','Egyetlen szín árnyalatát nevezzük meg, nem két külön színt sorolunk fel.','Az egyszerű színnévhez kapcsolódó árnyalatjelölő melléknevet egybeírjuk a színnévvel.',topic='színárnyalat')
    for a,b in [('sötét','rózsaszín'),('világos','narancssárga'),('halvány','kékeszöld')]:
        row(a+'+'+b,'apart','Összetett színnév elé kerül külön árnyalatjelölő melléknév.','Az összetett színnév elé kerülő további árnyalatjelölőt különírjuk.',topic='színárnyalat')
    for a,b in [('bőr','pénztárca'),('fa','ruhásszekrény'),('arany','karikagyűrű'),('arany','nyaklánc'),('ezüst','karóra'),('acél','csőhálózat'),('műanyag','szék'),('műanyag','virágcserép'),('bőr','sportcipő'),('fa','íróasztal'),('üveg','ajtókilincs')]:
        if ' ' in b:continue
        row(a+'+'+b,'apart','Anyagnévi kapcsolat: az anyagnév vagy a jelzett szó már összetett szó.','Az anyagnévi kapcsolatot különírjuk, ha az anyagnév vagy az utótag önmagában összetett szó.',topic='összetett anyagnév')
    for parts in ['arany+gyűrű','bőr+kabát','fa+kanál','üveg+pohár','fa+doboz','vas+kapu']:
        row(parts,'one','Egyszerű anyagnév és egyszerű főnév kapcsolata; az anyagot nevezzük meg.','Az egyszerű anyagnevet az egyszerű főnévvel egybeírjuk.',topic='egyszerű anyagnév')
    for line in COMPOUNDS.strip().splitlines():
        parts,ctx=line.split('|')
        row(parts,'one',ctx,'A megadott fogalmat egybeírt összetett szó nevezi meg. Az egyszerű anyagnévi kapcsolatoknál az anyagnév és az egyszerű főnév is egy szóvá kapcsolódik.')
    for line in ATTRIBUTES.strip().splitlines():
        parts,ctx=line.split('|')
        row(parts,'apart',ctx,'Egyszerű minőségjelzős szókapcsolatban a jelző és a jelzett főnév külön szó marad.')
    for line in PREFIXES.strip().splitlines():
        pre,verb,inf,obj=line.split('|');family=pre+inf
        row(pre+'+'+verb,'one',f'Kijelentő mondat: Most ___ {obj}. Az igekötő a közvetlenül utána álló igéhez tartozik.','A saját igéje előtt közvetlenül álló igekötőt egybeírjuk az igével.',family)
        row(verb+'+'+pre,'apart',f'Tagadó mondat: Most nem ___ {obj}.','Az ige mögé kerülő igekötő külön szó marad.',family)
        row(pre+'+szeretné+'+inf,'apart',f'Szándékot kifejező mondat: Később ___ {obj}.','Az igekötő és a hozzá tartozó főnévi igenév közé a szeretné szó ékelődik; mindhárom elemet különírjuk.',family)
    for line in HYPHENS.strip().splitlines():
        parts,ctx=line.split('|')
        row(parts,'hyphen',ctx,'Az állandósult mellérendelő összetétel két tagját kötőjellel kapcsoljuk össze.')
    for verb in 'tudod látod hallod érted kéred jössz mész vársz segítesz szereted olvastad megtaláltad elhozod megoldod emlékszel elkészült sikerült elindul elkezdjük folytatjuk'.split():
        row(verb+'+e','hyphen','Függő eldöntendő kérdésben az ige után kérdőszócska áll: Azt kérdezte, ___ .','Az -e kérdőszócskát kötőjellel kapcsoljuk az előtte álló szóhoz.',verb,topic='kérdőszócska')
    for a,b in [('egy','két'),('két','három'),('három','négy'),('négy','öt'),('öt','hat'),('hat','hét'),('hét','nyolc'),('nyolc','tíz'),('tíz','tizenkét'),('húsz','harminc')]:
        row(a+'+'+b,'hyphen','Hozzávetőleges mennyiséget adunk meg, nem összeadást és nem pontos összetett számnevet.','A hozzávetőleges számkapcsolat tagjai közé kötőjelet írunk.',topic='közelítő számok')

ANALYSIS_WORDS='''látjuk mutatja kutatja hallgatja olvasgatja válogatja forgatja mozgatja tanítja bántja fordítja számítja tisztítja szárítja nyitja nyomtatja tartja adogatja szeretjük építjük szépítjük segítjük fűtjük hűtjük vetjük vezetjük követjük említjük tudja fogadja tagadja hordja oldja toldja áldja kenjük fonja bánja unja anyjuk anyjai hagyja hagyjátok hunyja hányja beszéljen énekeljen ítéljük emeljük kezeljük csókolja ápolja rajzolja szénpor szénbánya szénből színben színnyomat színpadi kézfej vízpart háztető háztartás fogkrém zsebkendő adhat szívtelen dobszó vasgolyó kerékből patakban parkból népben gépben méztől tűztől padtól gázcső'''.split()
PHONETIC_WORDS='''ablak ajtó erdő mező hegy völgy folyó tó tenger felhő csillag bolygó hold szél eső hó nyár tél ősz tavasz reggel este dél fiú lány anya apa baba néni bácsi ember gyerek tanár diák orvos kertész fodrász szakács sofőr pék virág levél gyökér ág törzs répa almafa uborka banán citrom narancs körte szilva barack dió mogyoró túró vaj kenyér zsemle leves kávé tea kakaó bögre pohár tányér kanál villa kés labda sapka sál nadrág kabát zokni cipő pad polc fal szék ágy szőnyeg füzet radír vonal motor roller busz autó hajó'''.split()
SIMPLIFY_WORDS='''meggyes meggyet meggyleves füttyent füttyös könnyű könnyes könnyít könnyed annyi ennyi mennyi hattyú petty pettyes pötty pöttyös pottyan loccsanás loccsant fröccsen fröccs buggyan meggyfa gallyak gallyas gallyaz gallyazás asszonyok asszonyi hosszúság hosszúkás rosszabb rosszaság rosszall mésszé kulccsá jeggyé könnyé eddzetek eddzél eddzünk eddzék játsszuk játsszátok játsszák játssz vadássz vadásszatok halássz halásszatok mássz másszatok másszon vessz vesszen ossz osszatok osszon alussza alusszák'''.split()

def extend_principles(banks,add):
    seen={r['solution'] for r in banks['alapelvek']}
    def row(w,a,ctx,why):
        if w in seen:return
        seen.add(w);add('alapelvek',w,a,why,w,ctx,w)
    for w in PHONETIC_WORDS:row(w,'phonetic','Az önálló szóalak köznyelvi hangjelölését figyeld, nem a szó történeti eredetét.',f'A(z) {w} megadott önálló alakjának betűzése a köznyelvi hangalakot tükrözi: itt a kiejtés szerinti írásmód a vizsgált szempont.')
    for w in ANALYSIS_WORDS:row(w,'analysis','A kiejtésben módosuló hangkapcsolat ellenére megőrzött szóelemeket figyeld.',f'A(z) {w} alakban az írás megőrzi a szóelemek eredeti betűit, noha az érintkező hangok az ejtésben módosulnak. Ez a szóelemzés elvének vizsgált esete.')
    for r in banks['jly']:
        if r['answers']==['ly']:row(r['solution'],'tradition','A [j] hang ly-nal történő jelölését figyeld.',f'A(z) {r["solution"]} célzott részletében ly jelöli a [j] hangot. Ezt a hagyományos szóképet a kiejtés önmagában nem határozza meg.')
    for w in SIMPLIFY_WORDS:
        if '?' in w:continue
        row(w,'simplify','A hosszú többjegyű mássalhangzó rövidített betűjelölését figyeld.',f'A(z) {w} alakban a hosszú többjegyű mássalhangzó írásakor az első betűjegyet ismételjük. A vizsgált részlet az egyszerűsítés elvéhez tartozik.')
    for w,root,suffix in [('jobban','jobb','ban'),('szebben','szebb','ben'),('többen','több','ben'),('nagyobban','nagyobb','ban'),('arra','az','ra')]:
        if w=='arra':continue # Ez jelölt hasonulás, nem három azonos betű egyszerűsítése.
        row(w,'simplify',f'A(z) {root} + -{suffix} határán találkozó három azonos betű egyszerűsítését figyeld.',f'A(z) {root} + -{suffix} szóelemek találkozásánál három azonos betű helyett kettőt írunk: {w}. Ez az egyszerűsítés elve.')

def limit_bank(rows,target,preserve=0):
    """Stabil válogatás kategória, témakör és szócsalád szerinti körforgással."""
    if len(rows)<target:raise ValueError(f'Kevés feladat: {len(rows)} / {target}')
    head=rows[:preserve];pools=defaultdict(lambda:defaultdict(lambda:defaultdict(deque)))
    for r in rows[preserve:]:pools[r['answers'][0]][r.get('topic','alap')][r['family']].append(r)
    out=list(head)
    while len(out)<target:
        changed=False
        for topics in pools.values():
            while topics:
                topic=next(iter(topics));families=topics.pop(topic)
                if not families:continue
                family=next(iter(families));queue=families.pop(family)
                out.append(queue.popleft());changed=True
                if queue:families[family]=queue
                if families:topics[topic]=families
                break
            if len(out)==target:return out
        if not changed:break
    return out

TARGETS={'alapelvek':250,'egybeiras':350,'jly':400,'hosszusag':350,'hibakereso':650}

def expand_all(banks,add):
    old={k:len(v) for k,v in banks.items()}
    previous_errors=list(banks['hibakereso'])
    extend_jly(banks,add)
    extend_length(banks,add)
    extend_join(banks,add)
    extend_principles(banks,add)
    print('Szerkesztői választék:',{k:len(v) for k,v in banks.items()})
    for key in ['jly','hosszusag','egybeiras','alapelvek']:
        banks[key]=limit_bank(banks[key],TARGETS[key],old[key])
    # A hibakereső nem egyetlen betűtípus túlsúlya: 100 j/ly, 110 hanghosszúság,
    # 115 szókapcsolat egy helyes és egy valóban javítandó változattal.
    banks['hibakereso']=list(previous_errors);used_solutions=set()
    existing={(r['word'],r['solution']) for r in previous_errors}
    quotas={'jly':100,'hosszusag':110,'egybeiras':115}
    for source,quota in quotas.items():
        candidates=[]
        for r in banks[source]:
            if r['solution'] in used_solutions:continue
            if source=='jly' and r['solution'] in ['hely','boly','sújt']:continue
            if not any(x['solution']==r['solution'] for x in candidates):candidates.append(r)
        chosen=limit_bank(candidates,quota)
        for r in chosen:
            sol=r['solution'];used_solutions.add(sol)
            if source=='jly':
                letter=r['answers'][0];wrong=r['word'].replace('…','ly' if letter=='j' else 'j')
                reason=f'A célhelyen {letter} betű jelöli a [j] hangot.'
            elif source=='hosszusag':
                answer=r['answers'][0];right=r['options'][answer];other=r['options']['long' if answer=='short' else 'short']
                wrong=r['word'].replace('…',other);reason=f'A célhelyen {right} áll, nem {other}. A hanghosszúságot a helyes szóalak szerint jelöljük.'
            else:
                a=r['answers'][0];parts=r['word'].split(' + ')
                wrong=(' '.join(parts) if a=='one' else ''.join(parts))
                reason={'one':'Ebben a jelentésben egybeírjuk az elemeket.','apart':'Ebben a szerkezetben a különírás szükséges.','hyphen':'Ebben a szerkezetben kötőjel kapcsolja össze az elemeket.'}[a]
            assert wrong!=sol,(source,sol)
            for word,answer in [(sol,'correct'),(wrong,'fix')]:
                if (word,sol) in existing:continue
                existing.add((word,sol))
                add('hibakereso',word,answer,f'A megadott jelentésben a helyes alak: {sol}. {reason}',sol,r['context'],r['family'])
    banks['hibakereso']=limit_bank(banks['hibakereso'],TARGETS['hibakereso'],len(previous_errors))
    assert {k:len(v) for k,v in banks.items()}==TARGETS
