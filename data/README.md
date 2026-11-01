# MBETŰ helyesírási feladatbankok

Öt saját szerkesztésű bank, összesen **2000 feladat**. A mássalhangzók eredeti, 2572 szóalakos bankja a gyökérben levő `words.txt` marad.

| Fájl | Játék | Feladat |
|---|---|---:|
| alapelvek.txt | Kiejtés, szóelemzés, hagyomány, egyszerűsítés | 250 |
| egybeiras.txt | Egybe, külön, kötőjellel | 350 |
| jly.txt | J vagy ly? | 400 |
| hosszusag.txt | Rövid vagy hosszú? | 350 |
| hibakereso.txt | Helyes vagy javítandó? | 650 |

UTF-8 TSV, a megjegyzéssorok `#` jellel kezdődnek. Oszlopok:

1. A kártyán látható alak; a `…` egyetlen hiányzó betű helyét jelzi.
2. Elfogadott kategóriák JSON-tömbje.
3. Kategóriánkénti magyarázat JSON-objektumként.
4. Szócsalád az egymást közvetlenül követő rokon feladatok ritkításához.
5. Teljes, helyes megoldás.
6. A jelentés, a mondattani szerkezet vagy a figyelendő jelenség.
7. A két betűváltozat JSON-objektuma; csak a hanghosszúsági játék használja.

A jelentés a feladat része. Például a `ha…` alakhoz a hal és a hall is szabályos megoldás lehetne; a meghatározás és az adott kategória teszi egyértelművé. Ezért a motor a feladatokat önálló azonosítóval kezeli, nem pusztán a kártya betűsorával.

Az alapelvek játékában a kérdésben megnevezett írásmódbeli részletet kell besorolni, nem a teljes szó valamennyi lehetséges alapelvét. Az egybeírásnál a jelentés és a szerkezet dönti el a választást. A hibakeresőben szereplő hibás íráskép szándékos: a helyes változat a megoldásmezőben található.

A TXT-fájlok az elsődleges források, a build ezeket ágyazza be az offline HTML-be. Kézi módosítás után:

```sh
python3 scripts/build.py
node tests/games.test.cjs
```

A `scripts/generate_games.py` újra előállítja a szerkesztői kiinduló állapotot; futtatása felülírja a kézi TXT-javításokat. A tesztek ellenőrzik a hiányok helyes visszaállítását, a pontozást és a feladatbankok szerkezetét, de nem helyettesítik a szakmai lektorálást.

## Bővítés és ellenőrzés – 2026. november 1.

A 664 eredeti tétel változatlanul megmaradt, 1336 új feladat került melléjük. A hibakeresőben 325 helyes és 325 javítandó alak szerepel. A feladatszám nem jelent ugyanennyi különböző szót: ugyanaz a szó eltérő játékban vagy más megfigyelési szemponttal is előfordulhat.

A bővítésben hangsúlyosak a tőbeli időtartam-váltakozások (víz–vizet, út–utat, tíz–tizedik), az igekötők helyzete, az egyszerű és összetett anyagnevek, a színárnyalatok és az -e kérdőszócska. Az alapelveknél mindig a feladatban kijelölt jelenséget kell figyelni.

A kiinduló szerkesztői választékot a `scripts/expanded_content.py` tartalmazza. A generátor a kategóriák, a témakörök és a szócsaládok között váltakozva válogat belőle, majd ellenőrizhető TXT-pillanatképet ír. A feladatbankok a felület módosítása nélkül tovább szerkeszthetők.

Az ellenőrzés kiterjed a hiányos alakok visszaállítására, a javítások egyezésére, az ismétlődő tételek kizárására, a teljes bankot bejáró tesztkörre és a kulcsfontosságú jelentésbeli ellentétekre. Kiegészítő magyar szótári szűrés és tartalmi átnézés is készült. A gépi szótár nem dönt a mondatbeli jelentésről, és ez nem független szaklektorálás.

## Forrás

[A magyar helyesírás szabályai, 12. kiadás](https://helyesiras.mta.hu/helyesiras/default/akh12): különösen 6–7., 18–27., 49–60., 85–104., 115–116., 119–120., 263. pont. A feladatok és a magyarázatok saját megfogalmazásúak; a szabályzat a szakmai alapjuk, nem a teljes bank tételenkénti forrása.
