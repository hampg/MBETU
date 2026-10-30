# MBETŰ

Hat magyar nyelvi játék: mássalhangzótörvények, helyesírási alapelvek, egybeírás, j/ly, hanghosszúság és hibakereső. Közös húzható szókártya, gyakorlás, teszt és részletes javítás. Az Alon Peres-portfólió nagy tipográfiája és geometrikus formái ihlették; saját felület, saját kód és saját szerkesztésű szóbank.

**Élő játék:** https://hampg.github.io/MBETU/

## Játékok és közvetlen címek

| Játék | Kezdő bank | Cím |
|---|---:|---|
| Mássalhangzótörvények | 2572 szóalak | `#gyakorlas/massalhangzok` |
| Helyesírási alapelvek | 80 feladat | `#gyakorlas/alapelvek` |
| Egybe, külön, kötőjellel | 61 feladat | `#gyakorlas/egybeiras` |
| J vagy ly? | 182 feladat | `#gyakorlas/jly` |
| Rövid vagy hosszú? | 100 feladat | `#gyakorlas/hosszusag` |
| Jó így? – Hibakereső | 241 feladat | `#gyakorlas/hibakereso` |

A felső **Játékok** menü a `#jatekok` játéktárat nyitja meg. A gyakorló nézetben gyors játékválasztó is van. A teszt és a súgó mindig a kiválasztott játékhoz tartozik; a tesztek helyi összesítése játékonként külön tárolódik. Az új játékok összesen 664 feladatot tartalmaznak, többféle feladatban ugyanaz a szó is szerepelhet. Az új bankok dokumentációja: [data/README.md](data/README.md).

## Használat

Nyisd meg az **index.html** fájlt bármelyik modern böngészőben. Egyetlen fájlban van minden, internetkapcsolat nélkül is működik. Nincs telepítés, külső betűtípus, CDN, mérőkód vagy szerveroldali adatkezelés. A szólista letöltési linkjéhez a mellette levő `words.txt`, illetve az új játékokhoz a `data/` alatti TXT-fájlok is szükségesek. Maga a játék ezek nélkül is működik, mert a bankok be vannak ágyazva.

- Húzd a szót egy dobozba, vagy kattints/érints meg egy dobozt. Billentyűzet: **1–6** a szabályok, **7** a „Nincs szabály”.
- A törvény nevére mutatva vagy billentyűzettel ráfókuszálva egymondatos súgó jelenik meg; Esc bezárja.
- Gyakorláskor azonnali visszajelzés és magyarázat jár; a következő szóhoz külön gomb vezet.
- A tesztben 1 és a kiválasztott részhalmaz mérete között állítható a kérdésszám. Nincs ismétlődés. A visszajelzés a végén jelenik meg; a hibás szavak külön újragyakorolhatók, az eredmény TXT-be menthető.
- A legutóbbi teszt összesített eredménye a böngésző helyi tárhelyén marad. Nevek és személyes adatok nem kerülnek tárolásra vagy továbbításra.

## A hat doboz

1. Részleges hasonulás – a zöngésség és a képzés helye szerinti változat közös dobozban.
2. Írásban jelölt teljes hasonulás.
3. Írásban jelöletlen teljes hasonulás.
4. Összeolvadás.
5. Mássalhangzó-rövidülés.
6. Mássalhangzó-kiesés.

Egy szó több kategóriába is tartozhat. Bármelyik jelölt helyes válasz egy pontot ér. Az eredmény kategóriánkénti bontása emiatt átfedhet: nem kell a sorokat összeadni. A kiesés beszédtempótól függő lehetőség, nem minden háromtagú mássalhangzócsoportból kötelezően eltűnő hang.

## Szóbank és bővítés

A `words.txt` UTF-8 kódolású, tabulátorral tagolt szövegfájl, soronként:

```
szóalak    ["kategória", "másik_kategória"]    {"kategória":"magyarázat", ...}    szócsalád
```

(A fenti ábrában a tabulátorokat szóközök helyettesítik.) A `#` kezdetű sorok megjegyzések. A kulcsok: `partial`, `written`, `unwritten`, `fusion`, `shortening`, `deletion`, `none`.

A **2572 szóalak 776 szócsaládból** készül; a pontos aktuális számok a Szabálykönyvben olvashatók. A szám ragozott alakokat is tartalmaz, nem 2572 külön szótövet. A szólista saját összeállítású, kézzel rögzített tő- és toldalékcsaládokból készül. Egyenkénti lexikográfusi ellenőrzése nem történt meg. A teszt a kategóriák között váltakozik, így a sok igeképzés nem szorítja ki a ritkább kiesési példákat; a közelmúlt szócsaládjait lehetőség szerint kerüli.

A `scripts/generate_words.py` a szerkesztői kiinduló lista generátora. A játék **nem futtatja**, a `words.txt` pillanatképét használja. A TXT közvetlenül javítható; utána újra kell építeni az HTML-t. A generátor ismételt futtatása felülírja a TXT kézi javításait.

```sh
python3 scripts/build.py
node tests/core.test.cjs
node tests/games.test.cjs
python3 scripts/check_words.py
python3 -m http.server 4173
```

Nincs npm-függőség. Node 18+ a tesztekhez, Python 3.9+ az építéshez. A `src/` tartalmazza az olvasható HTML-, CSS- és JS-forrásokat. A `src/core.js` játékmotor és a szóbank más oldalakhoz is használható. A GitHub Actions ellenőrzi a pontozást, az ismétlésmentességet, a szűrést, a több jó válasz elfogadását, az adatstruktúrát és az előállított HTML naprakészségét. A teszt az adatstruktúrát ellenőrzi, nem helyettesíti a nyelvészeti lektorálást.

## Források

- [A magyar helyesírás szabályai, 12. kiadás](https://helyesiras.mta.hu/helyesiras/default/akh12): 49–60., 79–83., 92–93. pont.
- [Helyes kisokos: a szóelemzés elve](https://www.helyesiras.mta.hu/helyesiras/blog/show/helyes-kisokos-szoelemzes-elve), MTA Nyelvtudományi Intézet.
- [Szigetvári Péter: Mássalhangzók egymás közt](https://www.nyest.hu/hirek/hasonulas), Nyelv és Tudomány, 2013. 09. 26.
- [Magyar nyelv 9.](https://www.nkp.hu/tankonyv/magyar_nyelv_9/), Nemzeti Köznevelési Portál.

A források a szabályleírásokhoz adnak hátteret, nem a teljes szólista tételenkénti minősítéséhez. A súgó saját megfogalmazású. A kiejtési példák magyar betűs segédletek, nem IPA-átírások.

## Közzététel

GitHub Pages: **Settings → Pages → Deploy from a branch → main / (root)**. A `.nojekyll` miatt a gyökérben levő HTML közvetlenül kiszolgálható. A kész `index.html` más statikus tárhelyre is feltölthető.

## Licenc

A saját kód és a saját szóbank MIT-licencű; lásd LICENSE. A hivatkozott külső forrásokra és a dizájnreferenciára a saját jogosultjaik feltételei vonatkoznak.
