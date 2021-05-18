import sqlite3


def get_books(c):
    return c.execute('SELECT book_id, title, author FROM books')


def save_books(conn, t, a):
    c = conn.cursor()
    c.execute('INSERT INTO books(title, author) VALUES( ?, ?)', (t, a))
    conn.commit()


action = input('Co chcesz zrobić? [w]yświetl, [d]odaj: ')
if action == 'w':
    with sqlite3.connect('library.db') as connection:
        cursor = connection.cursor()
        for book in get_books(cursor):
            # print(book)
            book_id, title, author = book
            print(f'id: {book_id}, tytuł: \"{title}\", autor: \"{author}\"')
elif action == 'd':
    with sqlite3.connect('library.db') as connection:
        cursor = connection.cursor()
        title = input('Tytuł: ')
        author = input('Autor: ')
        save_books(connection, title, author)
else:
    print('Nie ma takiej opcji.')