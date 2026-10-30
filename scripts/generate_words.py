"""Saját szerkesztésű szócsaládok: nem egy külső szótár másolata.
A generátor a szólistát készíti; a játék a words.txt pillanatképét használja.
"""
import json, collections
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
rows = {}
LETTERS = ['ddzs','ccs','ddz','ggy','lly','nny','ssz','tty','zzs','dzs','cs','dz','gy','ly','ny','sz','ty','zs']
def letters(s):
    out=[]
    while s:
        hit=next((x for x in LETTERS if s.startswith(x)),s[0]);out.append(hit);s=s[len(hit):]
    return out
VOWELS=set('aáeéiíoóöőuúüű')
def add(word, cat, reason, family=None, extra=None):
    assert word and '\t' not in reason
    if word in rows:
        r=rows[word]
        for c in [cat]+(extra or []):
            if c not in r['answers']: r['answers'].append(c); r['explanations'][c]=reason
        return
    answers=[cat]+[c for c in (extra or []) if c != cat]
    rows[word]=dict(word=word,answers=answers,explanations={c:reason for c in answers},family=family or word)
def group(s):return s.split()
# A magánhangzó-harmóniát és a tőváltozatokat csoportonként rögzítjük.
back=group('ablak asztal kalap kabát lap pap nap csap pad fal dal kar kard park udvar ház gáz láz váz ágy vágy lány arany talaj olaj haj zaj baj raj vaj sajt rajz pajzs lánc tánc piac palack ablakpárkány ajándék játék szándék nadrág világ virág ország újság szabadság igazság barátság bátorság jóság tanár diák barát család madár kosár pohár kanál tál szál szamár nyár határ táj szárazság árnyék nyak sarok sarkantyú sárkány patak alak utak helyett')
# Kizárólag köznevek: a fenti szerkesztési jelölők nem kerülnek az adatbázisba.
back=[x for x in back if x not in ['utak','helyett']]
front=group('kép gép szép nép tér vér bér szél tél kéz méz víz tűz rész ész pénz perc lemez keret sziget füzet üzenet élet épület emelet terület felület kerület méret érték emlék szék kerék vendég szeg cég jég rét kert étel ebéd kenyér egér tenyér levél fenék gyermek gyerek ember tenger hegy völgy könyv könny könnycsepp függöny törvény fény lény tény igény ösvény remény élmény regény növény vélemény esemény eredmény erkély veszély személy műhely rejtély esély engedély ünnep ének vers test festék ecset felelet történet szemüveg üveg szőnyeg bélyeg')
front=[x for x in front if x not in ['szép','könyv']] # v után nincs -v hasonulás; a szép melléknevet másutt használjuk.
rounded=group('kör tükör ökör gödör vödör bőr őr tőr csőr szőr köröm öröm könyök kölyök üst füst köd föld zöld gyümölcs kulcs gömb gomb csont pont bolt folt gond hang láng rang domb comb lomb dob klub film cím szín sín kén ón szén')
# A vegyes csoport minden eleméhez kézzel rögzített harmónia.
back2=group('kulcs gomb csont pont bolt folt gond hang láng rang domb comb lomb dob klub film cím sín ón')
rounded=[x for x in rounded if x not in back2]
# Ezek a vegyes hangrendűek a megszokott elülső ragot kapják.
front += group('film cím sín szín kén szén')
back2=[x for x in back2 if x not in ['film','cím','sín']]
# -val/-vel; a hosszú mássalhangzók írása az egyszerűsítő írásmódot követi.
for nouns,suf in [(back+back2,'al'),(front+rounded,'el')]:
    for n in nouns:
        gs=letters(n); last=gs[-1]
        if last in VOWELS or last=='v': continue
        if last in ['ddzs','ccs','ddz','ggy','lly','nny','ssz','tty','zzs'] or (len(gs)>1 and gs[-1]==gs[-2]): doubled=n
        elif len(last)>1: doubled=n[:-len(last)]+last[0]+last
        else: doubled=n+last
        extra=[]
        # A rag hasonulásával keletkező hosszú hang más mássalhangzó mellett rövidül.
        before=gs[-2] if len(gs)>1 else ''
        if before and before not in VOWELS and before!=last:extra=['shortening']
        reason=f'A(z) {n} + -v{suf} kapcsolatban a rag v-je a tő utolsó mássalhangzójához hasonul; ezt az írás is mutatja.'
        if extra:reason+=' A keletkező hosszú hang másik mássalhangzó mellett a kiejtésben rövidül is.'
        add(doubled+suf,'written',reason,n,extra)
# Zöngésség szerinti hasonulás: külön rögzített ragcsaládok.
voiceless_back=group('ablak kalap lap pap nap csap sajt park patak alak nyak sarok kabát diák barát piac lánc tánc palack csont pont bolt folt')
voiceless_front=group('kép gép nép rész ész perc szék kerék rét kert sziget füzet üzenet élet épület emelet terület felület kerület méret érték emlék ünnep test festék ecset felelet történet üst füst könyök kölyök gyümölcs')
voiced_back=group('ház gáz láz váz ágy vágy pad kard család világ virág ország újság szabadság igazság barátság bátorság jóság ajándék nadrág hang láng rang domb comb lomb dob klub')
# Az ajándék k-ra végződik, ezért az első csoportban a helye.
voiced_back.remove('ajándék');voiceless_back.append('ajándék')
voiced_front=group('kéz méz víz tűz pénz lemez vendég szeg cég jég hegy völgy üveg szemüveg szőnyeg bélyeg köd föld zöld gömb')
for nouns,suffixes in [(voiceless_back,['ban','ba','ból']),(voiceless_front,['ben','be','ből']),(voiced_back,['tól','hoz','ként']),(voiced_front,['től','hez','ként'])]:
    for n in nouns:
        for s in suffixes:
            if s=='hez' and n in ['köd','föld','zöld','gömb','tűz','völgy']:s='höz'
            add(n+s,'partial',f'A(z) {n} + -{s} határán az első zörejhang zöngéssége a következő mássalhangzóhoz igazodik. Ez zöngésség szerinti részleges hasonulás, az írás nem jelöli.',n)
# Képzés helye: az n b előtt m-ként hangzik. Kevésbé vitatható, átlátható toldalékhatárok.
for ns,suffs in [(group('szín kén szén fény lény tény igény remény élmény regény növény vélemény esemény eredmény törvény függöny'),['ben','be','ből']),(group('lány arany talaj'),[])]:
    for n in ns:
        if not n.endswith('n') or n.endswith('ny'):continue
        for s in suffs:add(n+s,'partial',f'A(z) {n} + -{s} kapcsolatban az n hangot a b előtt m-ként ejtjük: képzés helye szerinti részleges hasonulás történik.',n)
# Összeolvadás: valódi, egyenként összeállított igetövek, a megfelelő ragozással.
fusion_back=group('lát tanít mutat kutat arat altat adogatogat olvasgat hallgat válogat forgat mozgat simogat látogat támogat ápolgat hajt hajtogat javít igazít alakít alapít alapozgat azonosít bátorít borít csábít csalódít csillapít csinosít csoportosít díszít eláraszt fakít fáraszt fogyaszt folytat fordít fojt forralgat fújtat gazdagít gyógyít gyorsít gyullaszt halaszt hallat használhat hatástalanít hódít hord horgaszt hullat húzat húzogat irányít indít izgat kapcsolgat kavarít koptat kopogtat koronázgat kóstolgat kutat lapogat lapozgat lassít lazít másolgat mosogat nagyít nyit nyomtat oktat olvasgat oszt osztogat rajzolgat rakat ragaszt riaszt ringat ropogtat ruházgat sajnáltat sajátít sarkít simít sodorít sorolgat szabadít szagolgat szakít szállít szárít számít szaporít takarít tanúsít tart taszít tisztít továbbít tud tudat udvaroltat utasít utaztat vált változtat várat vasaltat virágoztat vitat vonat vontat zárat zsibbaszt')
# Nem közhasználatú vagy bizonytalan szerkesztési alakok eltávolítása.
fusion_back=[x for x in fusion_back if x not in ['adogatogat','kavarít','sodorít','csalódít','díszít','sajátít']]
for n in fusion_back:
    for s in ['ja','juk','játok','ják']:
        end=n[-1]; outcome={'t':'ty','d':'gy'}.get(end,'')
        assert outcome,n
        add(n+s,'fusion',f'A(z) {n} + -{s} határán a {end} és a j a kiejtésben {outcome} hanggá olvad össze. A hang hossza a környezettől függ; az írás megőrzi a szóelemeket.',n)
for n in group('szeret félt ért épít szépít díszít segít készít egyesít értesít melegít hűt fűt süt üt vet vezet fest követ nevet említ erősít gyengít szelídít szédít teljesít teremt terít térít veszít ültet fizet keresztelget éget ébreszt csenget felejt fejt feleltet helyettesít illeszt kérdezget kerget lendít merít ment mereszt nehezít nézeget nevelget ölt önt pihentet pörget repít rendezget röpít sejt sejtet serkent sért siettet sürget szerezget szüntet tekerget terelget termeszt tervezget törölget tömörít tölt üdvözít üzemeltet zöldít'):
    if not n.endswith('t'):continue
    add(n+'jük','fusion',f'A(z) {n} + -jük határán a t és a j ty hanggá olvad össze. A helyesírás megtartja a t és a j betűjét.',n)
# A d-végű igék felszólító alakjai is összeolvadást tartalmaznak.
for ns,suffs in [(group('ad akad halad marad fogad tagad ragad szalad támad fárad szakad árad apad dagad izzad olvad szárad tapad hord old told áld'),['j','jak','jon','jatok','janak','junk']),(group('enged szenved ered eped téved mered ébred éled dermed dermed'),['j','jek','jen','jetek','jenek','jünk'])]:
    for n in ns:
        for s in suffs:add(n+s,'fusion',f'A(z) {n} + -{s} kapcsolatban a d és a j gy hanggá olvad össze a kiejtésben; írásban mindkét szóelemet megőrizzük.',n)
# Írásban jelöletlen teljes hasonulás: l/ny/gy + j.
unwritten_back=group('tanul alakul ápol áramol ábrázol árul bájol bámul bírál bonyolítgatol csatol csal csavarol csiszol csókol dalol darál dolgozol dacol dobol dörmögöl faragcsál foglal forral formál fújdogál gondol gyakorol gyalul gyalogol hajol hajszol halál hall halmozgatol használ hódol indul igazol javall kalapál kapál karcol kavarol kiabál kóstol korhol kotyogol markol másol mosolyogol mozgolódol okol orvosol párol parkol pazarol porol rabol rajzol randalírozol rombol rágcsál sajnál sétál sodol sorol spórol szaval szárnyal számol szól tárol talál tálal tanácsol tol tombol trappol ugrál utal utál vacsorál vakarol valósul vándorol varázsol vásárol válaszol vállal vádol zabolál zárol hanyagol')
unwritten_back=[n for n in unwritten_back if n not in ['zabolál','bonyolítgatol','bámul','csavarol','dolgozol','dörmögöl','halál','halmozgatol','javall','kavarol','kotyogol','mosolyogol','mozgolódol','randalírozol','sodol','vakarol']]
for n in unwritten_back:
    for s in (['j','jon','jatok','janak','junk'] if n in ['alakul','áramol','bájol','dacol','faragcsál','hajol','hódol','indul','szárnyal','tombol','trappol','ugrál','valósul','vándorol','vacsorál','fogy','fagy','vágy','huny'] else ['j','jon','jatok','janak','junk','ja','juk','játok','ják']):
        if s=='jen' and n.endswith('ül'):s='jön'
        add(n+s,'unwritten',f'A(z) {n} + -{s} kapcsolatban az l és a j találkozásakor a szokásos köznyelvi ejtésben hosszú j hallatszik. Ez írásban jelöletlen teljes hasonulás.',n)
for n in group('beszél mesél felel énekel ítél remél cserél bérel él fél kérlel nevel emel kezel ölel érlel mérlegel neheztel perel reggelizel szemlél szelídül szépül épül ül örül repül hegedül fütyül merül készül fésül kerül becsül ünnepel nevetgél'):
    if n in ['reggelizel']:continue
    for s in (['j','jen','jetek','jenek','jünk'] if n in ['él','fél','remél','neheztel','szelídül','szépül','épül','ül','örül','merül','készül','nevetgél'] else ['j','jen','jetek','jenek','jünk','jük']):
        if s=='jen' and n.endswith('ül'):s='jön'
        add(n+s,'unwritten',f'A(z) {n} + -{s} kapcsolatban az l a j előtt a szokásos köznyelvi ejtésben j-vé válik, így hosszú j-t ejtünk; az írás ezt nem jelöli.',n)
for n in group('hagy fogy fagy vágy hány huny'):
    for s in (['j','jon','jatok','janak','junk'] if n in ['alakul','áramol','bájol','dacol','faragcsál','hajol','hódol','indul','szárnyal','tombol','trappol','ugrál','valósul','vándorol','vacsorál','fogy','fagy','vágy','huny'] else ['j','jon','jatok','janak','junk','ja','juk','játok','ják']):
        add(n+s,'unwritten',f'A(z) {n} + -{s} kapcsolatban a j a tővégi gy vagy ny hanghoz teljesen hasonul; a betűalak ezt nem követi.',n)
# Rövidülés: hosszú mássalhangzó rövid mellé kerül, zöngésségi változás nélkül.
for ns,suffs in [(group('toll orr váll állatállomány'),['ban','ba','ból','nak','ra','ról','nál','hoz']),(group('sakk makk csepp tett tettvágy'),[]),(group('csepp'),['ben','be','ből','nek','re','ről','nél']),(group('sakk makk'),['nak','ra','ról','nál','hoz']),(group('orr váll toll'),['tól'])]:
    for n in ns:
        for s in suffs:
            if n=='orr' and s.startswith('r'):s=s[1:]
            add(n+s,'shortening',f'A(z) {n} + -{s} alakban a hosszú mássalhangzó egy másik mássalhangzó mellett röviden hangzik. Az írásban megmarad a hosszúság jelölése.',n)
for n,suffs in [('áll',['tam','tál','tunk','tatok','tak','na','nék','nának','nánk','hat','hatnak','hatna']),('száll',['tam','tál','tunk','tatok','tak','na','nék','nának','nánk','hat','hatnak','hatna']),('varr',['tam','tál','tunk','tatok','tak','na','nék','nának','nánk','hat','hatnak','hatna']),('forr',['tam','tál','tunk','tatok','tak','na','nék','nának','nánk']),('hall',['hat','hatnak','hatna'])]:
    for s in suffs:
            if n=='orr' and s.startswith('r'):s=s[1:]
            add(n+s,'shortening',f'A(z) {n} + -{s} alakban a hosszú {n[-1]} hang a következő mássalhangzó mellett rövidül; a kettőzött betűt megtartjuk.',n)
# Kiesés: beszédtempótól függő, az AkH. szerint is lehetséges ejtésváltozat.
for p in ['', 'meg','el','ki','be','fel','le','át','vissza','újra']:
    for s in ['ta','tad','tam','tuk','tátok','ták']:
        n=p+'mond'+s
        add(n,'deletion',f'A(z) {n} szó ndt hangcsoportjában a d a folyamatos beszédben kieshet (ndt → nt). Gondos ejtésben meg is maradhat; a játék a lehetséges kiesést kéri felismerni.',p+'mond', ['partial'])
        rows[n]['explanations']['partial']='Az ndt csoportban kiesés nélkül a d a t előtt zöngétlenedhet. A kiesést és a zöngésség szerinti részleges hasonulást is elfogadjuk.'
# Nincs a hat kategória szerinti változás; a kettőzött betű önmagában sem bizonyíték.
for ns,suffs in [(group('körte mese zene kefe epe lecke béke teve medve lencse cseresznye dinnye'),['','ben','ből','hez','nek']),(group('lámpa táska iskola óra rózsa róka macska kutya konyha ruha párna tábla labda szoba utca posta tinta minta hajó autó rádió fotó olló folyó ajtó zászló dió holló gólya kályha pálya só búza kukorica paprika paradicsom uborka banán citrom narancs asztal kalap papír ceruza radír vonal függöny'),[])]:
    for n in ns:
        for s in suffs:
            base=n[:-1]+{'a':'á','e':'é'}[n[-1]] if s and n[-1] in 'ae' else n
            add(base+s,'none','Ebben az alakban a játékban tárgyalt hat kategória egyikére sincs példa. A magánhangzó változása vagy egy eleve hosszú mássalhangzó önmagában nem mássalhangzótörvény.',n)
for n in group('alma lámpa táska iskola óra rózsa róka macska kutya konyha ruha párna tábla labda szoba tinta minta hajó autó rádió fotó olló folyó ajtó zászló dió holló gólya kályha pálya só búza kukorica paprika paradicsom uborka banán citrom narancs asztal kalap papír ceruza radír vonal kapu falu faliújság mókus béka cápa sün oroszlán zebra elefánt pelikán liba kacsa pulyka fóka bálna medúza polip csiga lepke bogár rigó cinege varjú pók répa karalábé saláta karfiol zeller petrezselyem burgonya rizs tea kakaó kávé torta pogácsa pizza leves sajtos túró vaj kenyér tojás óvoda udvar folyosó terem fal pad polc kép térkép szék ágy matrac takaró lepedő párnahuzat cipő kabát nadrág ing sapka sál kesztyű öv óceán tó fű fa levél virág eső hó szél felhő nyár tél ősz tavasz reggel este éjjel dél ma holnap tegnap itt ott erre arra ilyen olyan valaki valami fiú baba apa anya néni bácsi unoka család rokon fivér nővér húg öcs ajak fül szem orr arc kar láb térd ujj köröm haj bőr toll állat szalag vas arany ezüst bronz réz acél üveg kerámia gumi műanyag telefon kamera mikrofon monitor motor kerék villamos vonat busz repülő bicikli roller létra daru hajós kapitány matróz tanár diák mérnök orvos bíró szakács fodrász pék zenész hegedű zongora gitár fuvola dob trombita furulya játék mese vers dal ének szó betű magánhangzó mondat olvasó olvasás tanulás futás úszás rajzolás festés séta mozi múzeum könyvtár színház vár palota torony templom bazilika udvarház malom tanya kert park erdő mező rét domb hegy völgy patak forrás nap hold csillag bolygó világűr'): 
    # A szó belseji zöngésségi kapcsolatokra nem mondunk automatikusan nemet.
    exclude=set(group('faliújság elefánt folyosó térkép párnahuzat kesztyű tegnap bronz műanyag magánhangzó könyvtár színház udvarház világűr öcs'))
    if n not in exclude and n not in ['erre','arra','éjjel','reggel']:add(n,'none','A szóban a játék hat mássalhangzó-változása közül egyik sem figyelhető meg. A hangokat a szokásos alakjukban ejtjük; az eleve hosszú hang nem hasonulás.',n)
for suffix in ['ban','ból','hoz','nak']:
    add('almá'+suffix,'none','Az alma tővégi a-ja a toldalék előtt megnyúlik, de ez magánhangzó-változás. A játék hat mássalhangzótörvényének egyike sem szerepel az alakban.','alma')
# Tankönyvi horgonyok, pontos egyedi magyarázattal.
for word,cat,reason in [
('barátság','fusion','A barát + -ság határán a t és az s hosszú cs-vé olvad össze: baráccság.'),
('egészség','unwritten','Az egész + -ség határán a sz és az s hosszú s-ként hangzik: egésség.'),
('község','unwritten','A köz + -ség határán a z és az s a szokásos ejtésben hosszú s-ként hangzik: kösség.'),
('színpad','partial','A szín + pad határán az n a p hatására m-ként hangzik: szímpad. Ez képzés helye szerinti részleges hasonulás.'),
('népdal','partial','A nép + dal határán a p a d hatására b-vé zöngésül: nébdal.'),
('háztól','partial','A ház + -tól határán a z a t hatására sz-szé zöngétlenedik: hásztól.'),
('anyja','unwritten','Az any- + -ja kapcsolatban a j az ny-hez teljesen hasonul: annya. Az írás megtartja a j-t.'),
('jobbra','shortening','A jobb + -ra alakban a hosszú b az r mellett rövidül: jobra.'),
('otthon','shortening','Az otthon szóban a hosszú t a h mellett rövidül: othon.'),
('mindnyájan','deletion','A mindnyájan ndny csoportjában a d a folyamatos beszédben kieshet: minnyájan.'),
('gondnak','deletion','A gond + -nak alakban a d a folyamatos beszédben kieshet: gonnak.'),
('röntgen','deletion','A röntgen szó ntg hangcsoportjából a t a folyamatos beszédben kieshet: röngen.'),
('erre','written','Az ez + -re kapcsolatban a z a rag r hangjához teljesen hasonul; a változást írásban is jelöljük.'),
('arra','written','Az az + -ra kapcsolatban a z a rag r hangjához teljesen hasonul; a változást írásban is jelöljük.'),
('éjjel','written','Az éj + -vel kapcsolatban a rag v-je a j-hez teljesen hasonul; ezt az írás is jelzi.'),
('vízzel','written','A víz + -vel rag v-je a z-hez teljesen hasonul; a hosszú z-t írásban is jelöljük: vízzel.')]:
    if word in rows:del rows[word]
    add(word,cat,reason)
# A nyelvészeti háttér szélesebb, a játék az iskolai hat kategóriát gyakoroltatja.
# Hibás/nem semleges jelentésű kombinációkat kézzel is kiszűrünk.
for w in list(rows):
    if any(x in w for x in ['állatállomány','tettvágy']):del rows[w]
# A tőben meglévő törvény a toldalékolt alakban is megmarad.
base_laws={'szárazság':('unwritten','A szárazság tövében a z és az s a szokásos ejtésben hosszú s-ként hangzik.'),'szabadság':('fusion','A szabadság tövében a d és az s cs-vé olvad össze.'),'igazság':('unwritten','Az igazság tövében a z és az s hosszú s-ként hangzik.'),'barátság':('fusion','A barátság tövében a t és az s hosszú cs-vé olvad össze.')}
for r in rows.values():
    if r['family'] in base_laws and r['word']!=r['family']:
        c,ex=base_laws[r['family']]
        if c not in r['answers']:r['answers'].append(c);r['explanations'][c]=ex
# TSV: JSON mezővel a több elfogadott besoroláshoz és a magyarázatokhoz.
lines=['# MBETŰ szóbank v1 – UTF-8, tabulátorral tagolt; saját szerkesztés', '# szó\telfogadott_kategóriák (JSON)\tmagyarázatok (JSON)\tszócsalád']
for w,r in sorted(rows.items()):
    lines.append('\t'.join([w,json.dumps(r['answers'],ensure_ascii=False),json.dumps(r['explanations'],ensure_ascii=False),r['family']]))
(ROOT/'words.txt').write_text('\n'.join(lines)+'\n')
counts=collections.Counter(c for r in rows.values() for c in r['answers'])
print(len(rows),dict(counts))
