# MBETŰ helyesírási feladatbankok

Öt saját szerkesztésű kezdő bank, összesen **664 feladat**. A mássalhangzók eredeti, 2572 szóalakos bankja a gyökérben levő `words.txt` marad.

| Fájl | Játék | Feladat |
|---|---|---:|
| alapelvek.txt | Kiejtés, szóelemzés, hagyomány, egyszerűsítés | 80 |
| egybeiras.txt | Egybe, külön, kötőjellel | 61 |
| jly.txt | J vagy ly? | 182 |
| hosszusag.txt | Rövid vagy hosszú? | 100 |
| hibakereso.txt | Helyes vagy javítandó? | 241 |

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

## Forrás

[A magyar helyesírás szabályai, 12. kiadás](https://helyesiras.mta.hu/helyesiras/default/akh12): különösen 6–7., 18–25., 49–60., 85–104., 120. pont. A feladatok és a magyarázatok saját megfogalmazásúak; a szabályzat a szakmai alapjuk, nem a teljes bank tételenkénti forrása.
