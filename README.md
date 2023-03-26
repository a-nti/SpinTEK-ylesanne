## Spin TEK ülesande lahendus


### Rakenduse kasutamine:
1. Rakendust on soovitatav käivitada **Python 3** uusimate väljalasetega, kuid see ei pruugi olla vajalik

2. Käsurealt või muul eelistatud viisil palun installeerida <em>holidays</em> teek:
    <br><br>```$ pip install --upgrade holidays```<br><br>Täiendav info: https://pypi.org/project/holidays/
3. Fail või selle kataloog avada ja käivitada eelistatud IDEs, koodiredaktoris või käsureal käsklusega
<br><br>```$ python3 spinTEK_ylesanne.py```<br><br>
4. Sisesta aasta ja vajuta Enter klahvi. Tulemustega fail salvestatakse samasse kataloogi. Excelis võib olla vajalik lahtrite laiuse suurendamine.


### Ülesande kirjeldus:

Spin TEKis makstakse palka iga kuu kümnendal kuupäeval. Palka saab maksta ainult tööpäeval, seega kui 10. kuupäev langeb nädalavahetusele või riigipühale, siis makstakse palk välja sellele eelneval tööpäeval. 
Raamatupidaja soovib, et talle saadetaks meeldetuletus palga maksmise kohta kolm tööpäeva enne maksmise kuupäeva.

1. Ülesandeks on kirjutada käsurearakendus (CLI rakendus), mille sisendiks on aastaarv ja väljundiks 
    tabel, kus on valitud aasta iga kuu palgamaksmise kuupäev ja raamatupidajale meeldetuletuse saatmise 
    kuupäev (kokku 12 rida ning tabeli päis).


2. Rakendus peab väljundi kirjutama CSV-faili (näiteks "2023.csv").
