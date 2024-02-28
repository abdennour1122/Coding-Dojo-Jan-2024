SELECT * FROM books_schema.books;
SET SQL_SAFE_UPDATES = 0;
INSERT INTO books(title,num_of_pages) 
VALUES('c sharp',200),
('java',200),
('python',200),
('php',200),
('ruby',222);

UPDATE books
SET title  = 'c#' 
WHERE book_id =11;

SELECT * FROM users
JOIN favorites On favorites.user_id=users.id
JOIN books On favorites.book_id=books.book_id
where books.book_id=5;
SELECT * FROM books_schema.favorites;
SET SQL_SAFE_UPDATES = 0;

insert into favorites (user_id,book_id)
values(1,1),
(1,2);
insert into favorites (user_id,book_id)
values(2,1),
(2,2),
(2,3);
insert into favorites (user_id,book_id)
values(3,1),
(3,2),
(3,3),
(3,4);
insert into favorites (user_id,book_id)
values(4,1),
(4,2),
(4,3),
(4,4),
(4,5);

SELECT * FROM users 
JOIN favorites On favorites.user_id=users.id
JOIN books On favorites.book_id=books.book_id
where books.book_id=3;

delete FROM favorites WHERE book_id=3 and user_id=1;

insert into favorites (user_id,book_id)
values(5,2);

SELECT * FROM favorites 
where user_id=3;

SELECT * FROM books_schema.users;

INSERT INTO users(name) 
VALUES('jane amsden'),
('emily dixon'),
('Theodore Dostoevsky'),favorites
('William Shapiro'),
('Lao Xiu');

UPDATE users
SET name = 'bill shapiro' 
WHERE id =4;




