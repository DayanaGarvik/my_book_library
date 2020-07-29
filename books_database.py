#################################################################################
# -----------------------------------BACKEND----------------------------------- #
#################################################################################

import sqlite3


# VARIABLES:
#         BookTitle = StringVar()
#         DateReleased = StringVar()
#         Author = StringVar()
#         Language = StringVar()
#         Pages = StringVar()
#         Status = StringVar()


def book_data():
    """Creates library database."""
    con = sqlite3.connect("my_library.db")
    c = con.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, \
              BookTitle text, DateReleased text, Author text, Language text, Pages text, Status text)")
    con.commit()
    con.close()


def add_book(BookTitle, DateReleased, Author, Language, Pages, Status):
    """Adds new book record to the database."""
    con = sqlite3.connect("my_library.db")
    c = con.cursor()
    c.execute("INSERT INTO books VALUES (NULL, ?, ?, ?, ?, ?, ?)",
              (BookTitle, DateReleased, Author, Language, Pages, Status))
    con.commit()
    con.close()


def view_data():
    """Displays all the library records in the Display window."""
    con = sqlite3.connect("my_library.db")
    c = con.cursor()
    c.execute("SELECT * FROM books")
    rows = c.fetchall()
    con.close()
    return rows


def delete_record(id):
    """Deletes specified book from the database."""
    con = sqlite3.connect("my_library.db")
    c = con.cursor()
    c.execute("DELETE FROM books WHERE id=?", (id,))
    con.commit()
    con.close()


def search_data(BookTitle="", DateReleased="", Author="", Language="", Pages="", Status=""):
    """Searches for books by the criteria entered in one or several
        entry fields.
    """
    con = sqlite3.connect("my_library.db")
    c = con.cursor()
    c.execute("SELECT * FROM books WHERE BookTitle=? OR DateReleased=? OR Author=? OR Language=? OR \
                Pages=? OR Status=?", (BookTitle, DateReleased, Author, Language, Pages, Status))
    rows = c.fetchall()
    con.close()
    return rows


#def update_data(id, BookTitle="", DateReleased="", Author="", Language="", Pages="", Status=""):
#   """Updates book record."""
#  con = sqlite3.connect("my_library.db")
# c = con.cursor()
#c.execute("UPDATE books SET BookTitle=?, DateReleased=?, Author=?, Language=?, Pages=?, Status=? WHERE id=?",
#         (BookTitle, DateReleased, Author, Language, Pages, Status, id))
#con.commit()
#con.close()


book_data()
