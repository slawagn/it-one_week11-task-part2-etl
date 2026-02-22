CREATE TABLE IF NOT EXISTS "books" (
	"book_id" INTEGER NOT NULL UNIQUE,
	PRIMARY KEY("book_id")
);

CREATE TABLE IF NOT EXISTS "authors" (
	"author_id" INTEGER NOT NULL UNIQUE,
	PRIMARY KEY("author_id")
);

CREATE TABLE IF NOT EXISTS "readers" (
	"reader_id" INTEGER NOT NULL UNIQUE,
	PRIMARY KEY("reader_id")
);

CREATE TABLE IF NOT EXISTS "loans" (
	"loan_id" INTEGER NOT NULL UNIQUE,
	PRIMARY KEY("loan_id")
);
CREATE TABLE IF NOT EXISTS "loan_books" (
	"loan_book_id" INTEGER NOT NULL UNIQUE,
	PRIMARY KEY("loan_book_id")
);

CREATE TABLE IF NOT EXISTS "book_readers" (
	"book_reader_id" INTEGER NOT NULL UNIQUE,
	PRIMARY KEY("book_reader_id")
);


INSERT INTO books (book_id)
VALUES (1);

INSERT INTO authors (author_id)
VALUES (2);

INSERT INTO readers (reader_id)
VALUES (3);

INSERT INTO loans (loan_id)
VALUES (4);

INSERT INTO loan_books (loan_book_id)
VALUES (5);

INSERT INTO book_readers (book_reader_id)
VALUES (6);

