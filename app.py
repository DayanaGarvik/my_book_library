##################################################################################
# -----------------------------------FRONTEND----------------------------------- #
##################################################################################

# Importing Libraries

from tkinter import *
import tkinter.messagebox

# Import book database file
import books_database


class Book:
    def __init__(self, root):
        self.root = root
        self.root.title("My Personal Library")
        self.root.geometry("1000x650+0+0")
        self.root.config(bg="RosyBrown3")

        # List of variables
        BookTitle = StringVar()
        DateReleased = StringVar()
        Author = StringVar()
        Language = StringVar()
        Pages = StringVar()
        Status = StringVar()


# -------------------------------------FUNCTIONS------------------------------------ #

        def add_data():
            """Adds books to the database when pressing the Add Button."""
            if len(BookTitle.get()) != 0:
                books_database.add_book(BookTitle.get(), DateReleased.get(), Author.get(), Language.get(),
                Pages.get(), Status.get())
                booklist.delete(0, END)
                booklist.insert(END, (BookTitle.get(), DateReleased.get(), Author.get(), Language.get(), Pages.get(),
                                      Status.get()))

        def display_data():
            """Shows all the book records in the Display window."""
            booklist.delete(0, END)
            for row in books_database.view_data():
                booklist.insert(END, row, str(""))

        def book_record(event):
            """Creates global variable for manipulating each book record."""
            global book_var
            searchBook = booklist.curselection()[0]
            book_var = booklist.get(searchBook)

            self.txtBookTitle.delete(0, END)
            self.txtBookTitle.insert(END, book_var[1])
            self.txtDateReleased.delete(0, END)
            self.txtDateReleased.insert(END, book_var[2])
            self.txtAuthor.delete(0, END)
            self.txtAuthor.insert(END, book_var[3])
            self.txtLanguage.delete(0, END)
            self.txtLanguage.insert(END, book_var[4])
            self.txtPages.delete(0, END)
            self.txtPages.insert(END, book_var[5])
            self.txtStatus.delete(0, END)
            self.txtStatus.insert(END, book_var[6])

        def search_data():
            """Searches for books by the criteria entered in one or several
            entry fields.
            """
            booklist.delete(0, END)
            for row in books_database.search_data(BookTitle.get(), DateReleased.get(), Author.get(), Language.get(),
                                                  Pages.get(), Status.get()):

                booklist.insert(END, row, str(""))

        def delete_data():
            """Deletes the chosen book record."""
            if len(BookTitle.get()) != 0:
                books_database.delete_record(book_var[0])
                clear_data()
                display_data()

        def clear_data():
            """Clears all entry fields simultaneously."""
            self.txtBookTitle.delete(0, END)
            self.txtDateReleased.delete(0, END)
            self.txtAuthor.delete(0, END)
            self.txtLanguage.delete(0, END)
            self.txtPages.delete(0, END)
            self.txtStatus.delete(0, END)

        def update():
            """Updates the book record by deleting the previous version and
            creating a new one with a new id-number.
            """
            if len(BookTitle.get()) != 0:
                books_database.delete_record(book_var[0])
            if len(BookTitle.get()) != 0:
                books_database.add_book(BookTitle.get(), DateReleased.get(), Author.get(), Language.get(),
                Pages.get(), Status.get())
                booklist.delete(0, END)
                booklist.insert(END, (BookTitle.get(), DateReleased.get(), Author.get(), Language.get(),
                Pages.get(), Status.get()))

        def exit_btn():
            """Asks user if she wants to close the exit the library,
            if pressed yes - closes the program.
            """
            exit_btn = tkinter.messagebox.askyesno("ALERT", message="Are you sure you want to exit the library?")
            if exit_btn > 0:
                root.destroy()
            return


# ------------------------------------FRAMES---------------------------------------- #
        # Library layout
        MainFrame = Frame(self.root, bg="RosyBrown3")
        MainFrame.pack(anchor="center")


        # Frame for the title
        TitleFrame = Frame(MainFrame, width=100, padx=20, pady=8, bg="linen", relief=FLAT)
        TitleFrame.grid(row=0, column=1, sticky=N)

        self.lblTitle = Label(TitleFrame, font=('helvetica', 40, 'bold', 'italic'),
                              text="My Library", bg="linen", fg="IndianRed4")
        self.lblTitle.grid()

        # Frame for the Entry fields
        DataFrame = Frame(MainFrame, width=1000, height=500, bg="RosyBrown3", relief=RIDGE)
        DataFrame.grid(row=1, column=1, padx=20)

        DataFrameEntry = LabelFrame(DataFrame, width=400, height=500, bg="linen", relief=FLAT,
                                    font=('helvetica', 20), text="Enter Book Details\n", fg="IndianRed4")
        DataFrameEntry.grid(row=1, column=1, ipadx=30, ipady=5)

        # Frame for the Buttons
        ButtonFrame = Frame(DataFrame, width=120, height=500, bg="linen", relief=RIDGE)
        ButtonFrame.grid(row=1, column=2, ipadx=5, ipady=5, sticky=W+E)

        # Frame for the Display
        DataFrameDisplay = LabelFrame(DataFrame, width=400, height=500, bg="linen", relief=FLAT,
                                      font=('helvetica', 20), text="My Books\n", fg="IndianRed4")
        DataFrameDisplay.grid(row=2, column=1, ipady=5, columnspan=2)


# ----------------------------------------ENTRY FIELDS AND THEIR LABELS-------------------------------------- #

        # Variables:
        #         bookTitle = StringVar()
        #         dateReleased = StringVar()
        #         author = StringVar()
        #         language = StringVar()
        #         pages = StringVar()
        #         status = StringVar()

        # BOOK TITLE
        self.lblBookTitle = Label(DataFrameEntry, font=("helvetica", 18, "bold"), text="Book Title", padx=2, pady=2,
                                  bg="snow", fg="IndianRed4")
        self.lblBookTitle.grid(row=0, column=0, ipadx=5, sticky=W)
        self.txtBookTitle = Entry(DataFrameEntry, font=("helvetica", 18, "bold"), textvariable=BookTitle, width=20)
        self.txtBookTitle.grid(row=0, column=1, ipadx=5, sticky=W)

        # DATE OF RELEASE
        self.lblDateReleased = Label(DataFrameEntry, font=("helvetica", 18, "bold"), text="Year of Release", padx=2,
                                     pady=2, bg="snow", fg="IndianRed4")
        self.lblDateReleased.grid(row=1, column=0, ipadx=5, sticky=W)
        self.txtDateReleased = Entry(DataFrameEntry, font=("helvetica", 18, "bold"), textvariable=DateReleased, width=20)
        self.txtDateReleased.grid(row=1, column=1, ipadx=5, sticky=W)

        # AUTHOR
        self.lblAuthor = Label(DataFrameEntry, font=("helvetica", 18, "bold"), text="Author", padx=2, pady=2,
                               bg="snow", fg="IndianRed4")
        self.lblAuthor.grid(row=2, column=0, ipadx=5, sticky=W)
        self.txtAuthor = Entry(DataFrameEntry, font=("helvetica", 18, "bold"), textvariable=Author, width=20)
        self.txtAuthor.grid(row=2, column=1, ipadx=5, sticky=W)

        # LANGUAGE
        self.lblLanguage = Label(DataFrameEntry, font=("helvetica", 18, "bold"), text="Language", padx=2, pady=2,
                                 bg="snow", fg="IndianRed4")
        self.lblLanguage.grid(row=3, column=0, ipadx=5, sticky=W)
        self.txtLanguage = Entry(DataFrameEntry, font=("helvetica", 18, "bold"), textvariable=Language, width=20)
        self.txtLanguage.grid(row=3, column=1, ipadx=5, sticky=W)

        # PAGES
        self.lblPages = Label(DataFrameEntry, font=("helvetica", 18, "bold"), text="Number of Pages", padx=2, pady=2,
                              bg="snow", fg="IndianRed4")
        self.lblPages.grid(row=4, column=0, ipadx=5, sticky=W)
        self.txtPages = Entry(DataFrameEntry, font=("helvetica", 18, "bold"), textvariable=Pages, width=20)
        self.txtPages.grid(row=4, column=1, ipadx=5, sticky=W)

        # STATUS
        self.lblStatus = Label(DataFrameEntry, font=("helvetica", 18, "bold"), text="Status", padx=2, pady=2,
                               bg="snow", fg="IndianRed4")
        self.lblStatus.grid(row=5, column=0, ipadx=5, sticky=W)
        self.txtStatus = Entry(DataFrameEntry, font=("helvetica", 18, "bold"), textvariable=Status, width=20)
        self.txtStatus.grid(row=5, column=1, ipadx=5, sticky=W)


# -----------------------------------------LISTBOX AND SCROLLBAR-------------------------------------------#

        scrollbar = Scrollbar(DataFrameDisplay)
        scrollbar.grid(row=0, column=1)

        booklist = Listbox(DataFrameDisplay, width=80, height=15, font=("helvetica", 12, "bold"),
                           yscrollcommand=scrollbar.set)
        booklist.bind("<<ListboxSelect>>", book_record)
        booklist.grid(row=0, column=0, padx=8, pady=8)
        scrollbar.config(command=booklist.yview)


# -----------------------------------------------BUTTONS----------------------------------------------#

        # Add, Display, Search, Delete, Clear, Update, Exit

        # ADD
        self.btnAdd = Button(ButtonFrame, text="Add", font=("helvetica", 16, "bold"), height=1, width=10, bd=4,
                             bg="linen", fg="IndianRed4", command=add_data)
        self.btnAdd.grid(row=2, column=0, padx=(4, 4), pady=5)

        # DISPLAY
        self.btnDisplay = Button(ButtonFrame, text="Display", font=("helvetica", 16, "bold"), height=1, width=10, bd=4,
                                 bg="linen", fg="IndianRed4", command=display_data)
        self.btnDisplay.grid(row=3, column=0, padx=(4, 4), pady=8)

        # SEARCH
        self.btnSearch = Button(ButtonFrame, text="Search", font=("helvetica", 16, "bold"), height=1, width=10, bd=4,
                                bg="linen", fg="IndianRed4", command=search_data)
        self.btnSearch.grid(row=4, column=0, padx=(4, 4), pady=8)

        # DELETE
        self.btnDelete = Button(ButtonFrame, text="Delete Book", font=("helvetica", 16, "bold"), height=1, width=10,
                                bd=4, bg="linen", fg="IndianRed4", command=delete_data)
        self.btnDelete.grid(row=5, column=0, padx=(4, 4), pady=8)

        # CLEAR
        self.btnClear = Button(ButtonFrame, text="Clear Fields", font=("helvetica", 16, "bold"), height=1, width=10,
                               bd=4, bg="linen", fg="IndianRed4", command=clear_data)
        self.btnClear.grid(row=6, column=0, padx=(4, 4), pady=8)

        # UPDATE
        self.btnUpdate = Button(ButtonFrame, text="Update", font=("helvetica", 16, "bold"), height=1, width=10, bd=4,
                                bg="linen", fg="IndianRed4", command=update)
        self.btnUpdate.grid(row=7, column=0, padx=(4, 4), pady=8)

        # EXIT
        self.btnExit = Button(ButtonFrame, text="Exit Library", font=("helvetica", 16, "bold"), height=1, width=10,
                              bd=4, bg="linen", fg="IndianRed4", command=exit_btn)
        self.btnExit.grid(row=8, column=0, padx=(4, 4))


if __name__ == '__main__':
    root = Tk()
    applications = Book(root)
    root.mainloop()
