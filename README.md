# Monty-Hall-Problem-
BME Mathematics BSc 3. Semester Probability Programming excersises 2. Homework 
Ez a BME matematika bsc valószínűség számítás programozási feladatok című tárgy 2. házi feladata
A Monty Hall-paradoxon egy valószínűségi paradoxon, ami az Amerikai Egyesült Államokban futott Let's Make a Deal (Kössünk üzletet) című televíziós vetélkedő utolsó feladatán alapul, nevét a vetélkedő műsorvezetőjéről, Monty Hallról kapta. (A műsor magyar változatának címe Zsákbamacska volt, és Rózsa György vezette.)

A műsor végén a játékosnak mutatnak három csukott ajtót, amelyek közül kettő mögött egy-egy kecske van, a harmadik mögött viszont egy vadonatúj autó. A játékos nyereménye az, ami az általa kiválasztott ajtó mögött van. Azonban a választás meg van egy kicsit bonyolítva. Először a játékos csak rámutat az egyik ajtóra, de mielőtt valóban kinyitná, a műsorvezető a másik két ajtó közül kinyit egyet, amelyik mögött nem az autó van (a játékvezető tudja, melyik ajtó mögött mi van), majd megkérdezi a játékost, hogy akar-e módosítani a választásán. A játékos ezután vagy változtat, vagy nem, végül kinyílik az így kiválasztott ajtó, mögötte a nyereménnyel. A paradoxon nagy kérdése az, hogy érdemes-e változtatni, illetve hogy számít-e ez egyáltalán.

Három játéktaktika lehetséges e kérdés után:

Igen, megváltoztatom a döntést, megéri!
Nem változtatok (nem tudnám elviselni, hogy eldobtam a lehetőséget).
Mindegy hogy megváltoztatom vagy nem, 1/2-1/2 az esély, hogy melyik ajtó mögött van a nagy nyeremény.
Írjunk programot, mely szimulálja e három játékstratégiát, mindegyiket 1000-szer. A program

véletlen módon jelöljön ki egy ajtót, amely mögött az értékes ajándék van,
a játékos szerepében véletlenül válasszon egy ajtót (nem tudva az előző választásról),
a műsorvezető szerepében (véletlenszerűen) válasszon egy ajtót, mely különbözik a játékos által választottól és amely mögött nem az értékes jutalom van,
a játékos szerepében az első 1000-ben maradjon meg az eredeti döntése mellett, a második 1000 esetben változtassa meg döntését, a harmadik 1000 esetben 0.5 valószínűséggel változtasson eredeti döntésén, végül
eredményül írjuk ki a játékos nyerésének relatív gyakoriságát a három esetben a következő táblázat mintájára:

Marad a kiválasztott ajtó 0.245
Másik ajtót választ       0.567
Mindegy                   0.671
A feladat célja: a relatív gyakoriság szimuláción keresztül való megtapasztalása és a feltételes valószínűség fogalmának előkészítése egy paradoxonnak tűnő problémán keresztül.

Programozási cél: szimuláció programozása, véletlen szám generálása, ciklus írása.
A feltöltendő fájl neve montyhall.py legyen.
A feladat a példatárban 2.20 sorszámmal szerepel.
