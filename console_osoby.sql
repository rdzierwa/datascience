SELECT imię ||' '|| lower(nazwisko) as imie_nazwisko, wiek FROM osoby;

SELECT  nazwisko, length(nazwisko) as dlugosc_nazwiska from osoby;

SELECT  REPLACE(imię,'Michał','Michael') as imię, length(nazwisko) as dlugosc_nazwiska from osoby;

SELECT substr(nazwisko,1,2) as nazwisko from osoby;