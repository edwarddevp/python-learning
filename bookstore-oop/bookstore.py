"""
A program that stores this book information
Title, Author,
Year, ISBN

User can:
-View all records
-Search an entry
-ADD an entry
-Update an entry
-Delete an entry
-Close
"""
from tkinter import *
from tkinter import ttk
from backend import Database

database = Database("bookstore.db")


class Window(Tk):

    def __init__(self):
        super().__init__()
        self.wm_title("BookStore")
        self.renderLabels()
        self.renderEntries()
        self.renderListBox()
        self.rederButtons()

    def renderLabels(self):
        def create_label(label, row, column):
            return ttk.Label(text=label)\
                .grid(row=row, column=column, padx=1, pady=5)

        self.title_label = create_label("Title: ", 0, 0)
        self.author_label = create_label("Author: ", 0, 2)
        self.year_label = create_label("Year: ", 1, 0)
        self.ISBN_label = create_label("ISBN: ", 1, 2)

    # upper part entries

    def renderEntries(self):
        def create_entry(row, column):
            entry_value = StringVar()
            entry = ttk.Entry(self, textvariable=entry_value)
            entry.grid(row=row, column=column, padx=5, pady=5)
            return entry, entry_value

        self.title, self.title_value = create_entry(0, 1)
        self.author, self.author_value = create_entry(0, 3)
        self.year, self.year_value = create_entry(1, 1)
        self.ISBN, self.ISBN_value = create_entry(1, 3)

    # main part

    def renderListBox(self):
        def get_selected_row(event):
            selected = self.list_books.curselection()
            if len(selected):
                _extracted_from_get_selected_row_6()

        def _extracted_from_get_selected_row_6():
            index = self.list_books.curselection()[0]
            self.selected_tuple = self.list_books.get(index)
            self.title.delete(0, END)
            self.title.insert(END, self.selected_tuple[1])
            self.author.delete(0, END)
            self.author.insert(END, self.selected_tuple[2])
            self.year.delete(0, END)
            self.year.insert(END, self.selected_tuple[3])
            self.ISBN.delete(0, END)
            self.ISBN.insert(END, self.selected_tuple[4])

        self.list_books = Listbox(self, height=12, width=35)
        self.list_books.grid(row=2, column=0, rowspan=6,
                             columnspan=2, padx=15, pady=15)

        self.list_books.bind('<<ListboxSelect>>', get_selected_row)

        list_books_scroolbar = ttk.Scrollbar(self)
        list_books_scroolbar.grid(row=2, column=2, rowspan=6)

        self.list_books.configure(yscrollcommand=list_books_scroolbar.set)
        list_books_scroolbar.configure(command=self.list_books.yview)

    # buttons

    def rederButtons(self):
        def create_button(label, row, column, command=lambda: print("Button")):
            return ttk.Button(self, text=label, command=command)\
                .grid(row=row, column=column, sticky=S+N+E+W, pady=2, padx=5)

        def fill_books_list():
            self.list_books.delete(0, END)
            for row in database.view():
                self.list_books.insert(END, row)

        def search_entry():
            self.list_books.delete(0, END)
            for row in database.search(
                self.title_value.get().strip(),
                self.author_value.get().strip(),
                self.year_value.get().strip(),
                self.ISBN_value.get().strip()
            ):
                self.list_books.insert(END, row)

        def add_entry():
            title = self.title_value.get().strip()
            author = self.author_value.get().strip()
            year = self.year_value.get().strip()
            isbn = self.ISBN_value.get().strip()
            if title and author and year and isbn:
                database.insert(
                    title,
                    author,
                    year,
                    isbn
                )
                self.list_books.delete(0, END)
                self.list_books.insert(END, (title, author, year, isbn))

        def update_entry():
            title = self.title_value.get().strip()
            author = self.author_value.get().strip()
            year = self.year_value.get().strip()
            isbn = self.ISBN_value.get().strip()
            if title and author and year and isbn:
                database.update(
                    str(self.selected_tuple[0]),
                    title,
                    author,
                    year,
                    isbn
                )
            fill_books_list()

        def delete_entry():
            database.delete(str(self.selected_tuple[0]))
            fill_books_list()

        create_button('View All', 2, 3, fill_books_list)
        create_button('Search Entry', 3, 3, search_entry)
        create_button('Add Entry', 4, 3, add_entry)
        create_button('Update Selected', 5, 3, update_entry)
        create_button('Delete Selected', 6, 3, delete_entry)
        create_button('Close', 7, 3, self.destroy)


if __name__ == "__main__":
    app = Window()
    app.mainloop()
