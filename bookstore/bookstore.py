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
import backend

win = Tk()

win.wm_title("BookStore")

# win.geometry('600x350')

# upper part labels


def create_label(label, row, column):
    return Label(text=label)\
        .grid(row=row, column=column, padx=1, pady=5)


title_label = create_label("Title: ", 0, 0)
author_label = create_label("Author: ", 0, 2)
year_label = create_label("Year: ", 1, 0)
ISBN_label = create_label("ISBN: ", 1, 2)

# upper part entries


def create_entry(row, column):
    entry_value = StringVar()
    entry = Entry(win, textvariable=entry_value)
    entry.grid(row=row, column=column, padx=5, pady=5)
    return entry, entry_value


title, title_value = create_entry(0, 1)
author, author_value = create_entry(0, 3)
year, year_value = create_entry(1, 1)
ISBN, ISBN_value = create_entry(1, 3)

# main part


def get_selected_row(event):
    global selected_tuple
    selected = list_books.curselection()
    if len(selected):
        index = list_books.curselection()[0]
        selected_tuple = list_books.get(index)
        title.delete(0, END)
        title.insert(END, selected_tuple[1])
        author.delete(0, END)
        author.insert(END, selected_tuple[2])
        year.delete(0, END)
        year.insert(END, selected_tuple[3])
        ISBN.delete(0, END)
        ISBN.insert(END, selected_tuple[4])


list_books = Listbox(win, height=12, width=35)
list_books.grid(row=2, column=0, rowspan=6, columnspan=2, padx=15, pady=15)

list_books.bind('<<ListboxSelect>>', get_selected_row)

list_books_scroolbar = Scrollbar(win)
list_books_scroolbar.grid(row=2, column=2, rowspan=6)

list_books.configure(yscrollcommand=list_books_scroolbar.set)
list_books_scroolbar.configure(command=list_books.yview)

# buttons


def create_button(label, row, column, command=lambda: print("Button")):
    return Button(win, text=label, command=command)\
        .grid(row=row, column=column, sticky=S+N+E+W, pady=2, padx=5)


def fill_books_list():
    list_books.delete(0, END)
    for row in backend.view():
        list_books.insert(END, row)


def search_entry():
    list_books.delete(0, END)
    for row in backend.search(
        title_value.get().strip(),
        author_value.get().strip(),
        year_value.get().strip(),
        ISBN_value.get().strip()
    ):
        list_books.insert(END, row)


def add_entry():
    title = title_value.get().strip()
    author = author_value.get().strip()
    year = year_value.get().strip()
    isbn = ISBN_value.get().strip()
    if title and author and year and isbn:
        backend.insert(
            title,
            author,
            year,
            isbn
        )
        list_books.delete(0, END)
        list_books.insert(END, (title_value.get().strip(),
                                author_value.get().strip(),
                                year_value.get().strip(),
                                ISBN_value.get().strip()))


def update_entry():
    title = title_value.get().strip()
    author = author_value.get().strip()
    year = year_value.get().strip()
    isbn = ISBN_value.get().strip()
    if title and author and year and isbn:
        backend.update(
            str(selected_tuple[0]),
            title,
            author,
            year,
            isbn
        )
    fill_books_list()


def delete_entry():
    backend.delete(str(selected_tuple[0]))
    fill_books_list()


create_button('View All', 2, 3, fill_books_list)
create_button('Search Entry', 3, 3, search_entry)
create_button('Add Entry', 4, 3, add_entry)
create_button('Update Selected', 5, 3, update_entry)
create_button('Delete Selected', 6, 3, delete_entry)
create_button('Close', 7, 3, win.destroy)

win.mainloop()
