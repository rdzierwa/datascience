SELECT author_id, COUNT(title) FROM titles GROUP BY author_id;

SELECT users.name, users.surname user_id, COUNT(book_id) as ile_ksiazek FROM borrowings
                                            JOIN users on users.ID = borrowings.user_id
                                            GROUP BY book_id;

--Chcemy policzyć książki napisane przez każdego autora, który ma ponad pięć książek Tabela Titles:

SELECT author_id, count(title) FROM titles GROUP BY author_id HAVING COUNT(title)>5;

SELECT authors.name||' '|| surname as autor, titles.title FROM authors
    JOIN titles ON authors.ID = titles.author_id
WHERE author_id = 3;

SELECT authors.name||' '|| surname as autor, titles.title FROM authors
    JOIN titles ON authors.ID = titles.author_id
WHERE substr(surname,1,1)=='S';

SELECT authors.name||' '|| surname as autor, titles.title FROM authors
    JOIN titles ON authors.ID = titles.author_id
WHERE surname like 'S%';