do $$ begin assert (select count(*) from books) = 1, '1 book is expected';end;$$;
do $$ begin assert (select book_id from books limit 1) = 1, 'book with book_id of 1 is expected';end;$$;

do $$ begin assert (select count(*) from authors) = 1, '1 author is expected';end;$$;
do $$ begin assert (select author_id from authors limit 1) = 2, 'author with author_id of 2 is expected';end;$$;

do $$ begin assert (select count(*) from readers) = 1, '1 reader is expected';end;$$;
do $$ begin assert (select reader_id from readers limit 1) = 3, 'reader with reader_id of 3 is expected';end;$$;

do $$ begin assert (select count(*) from loans) = 1, '1 loan is expected';end;$$;
do $$ begin assert (select loan_id from loans limit 1) = 4, 'loan with loan_id of 4 is expected';end;$$;

do $$ begin assert (select count(*) from loan_books) = 1, '1 loan_book is expected';end;$$;
do $$ begin assert (select loan_book_id from loan_books limit 1) = 5, 'loan_book with loan_book_id of 5 is expected';end;$$;

do $$ begin assert (select count(*) from book_readers) = 1, '1 book_reader is expected';end;$$;
do $$ begin assert (select book_reader_id from book_readers limit 1) = 6, 'book_reader with book_reader_id of 6 is expected';end;$$;

SELECT 'ALL TESTS PASSED!' AS message
