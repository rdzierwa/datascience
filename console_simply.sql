SELECT COUNT(title) as total, Author_surname FROM simple_library_db
                                             GROUP BY Author_surname ORDER BY total DESC;
--Podaj łączną liczbę tytułów każdego autora--
SELECT COUNT(title) as total,Author_surname, Title FROM simple_library_db
                                                   GROUP BY Title ORDER BY Author_surname, total DESC;
SELECT lower(Author_name) as name, upper(Author_surname) as surname FROM simple_library_db

