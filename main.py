import tkinter as tk
from tkinter import messagebox
import json
from datetime import datetime

class LibraryManagementSystemGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")

        # Color styling
        self.root.configure(bg='#3498db')
        self.label_color = '#ffffff'
        self.button_color = '#2ecc71'
        self.entry_color = '#ecf0f1'

        # Increase window size
        self.root.geometry("400x400")

        self.library_name = "My Library"
        self.books = {}
        self.load_books()

        self.label = tk.Label(root, text=f"Welcome to {self.library_name}", bg='#3498db', fg=self.label_color, font=('Helvetica', 16))
        self.label.pack(pady=10)

        self.display_button = tk.Button(root, text="Display Books", command=self.display_books, bg=self.button_color, fg=self.label_color)
        self.display_button.pack(pady=5)

        self.add_button = tk.Button(root, text="Add Book", command=self.add_book, bg=self.button_color, fg=self.label_color)
        self.add_button.pack(pady=5)

        self.remove_button = tk.Button(root, text="Remove Book", command=self.remove_book, bg=self.button_color, fg=self.label_color)
        self.remove_button.pack(pady=5)

        self.checkout_button = tk.Button(root, text="Checkout Book", command=self.checkout_book, bg=self.button_color, fg=self.label_color)
        self.checkout_button.pack(pady=5)

        self.return_button = tk.Button(root, text="Return Book", command=self.return_book, bg=self.button_color, fg=self.label_color)
        self.return_button.pack(pady=5)

    def load_books(self):
        if tk.messagebox.askyesno("Load Books", "Load existing books data?"):
            try:
                with open("library_books.json", "r") as file:
                    self.books = json.load(file)
            except FileNotFoundError:
                tk.messagebox.showinfo("Info", "No existing data found.")

    def save_books(self):
        with open("library_books.json", "w") as file:
            json.dump(self.books, file, indent=2)

    def display_books(self):
        book_list = "\n".join([f"{book_id}: {info['title']} by {info['author']} ({info['available']} available)"
                               for book_id, info in self.books.items()])
        tk.messagebox.showinfo("Library Inventory", book_list)

    def add_book(self):
        add_book_window = tk.Toplevel(self.root)
        add_book_window.title("Add Book")

        # Color styling
        add_book_window.configure(bg='#3498db')

        title_label = tk.Label(add_book_window, text="Title:", bg='#3498db', fg=self.label_color)
        title_label.grid(row=0, column=0, padx=10, pady=10)

        title_entry = tk.Entry(add_book_window, bg=self.entry_color)
        title_entry.grid(row=0, column=1, padx=10, pady=10)

        author_label = tk.Label(add_book_window, text="Author:", bg='#3498db', fg=self.label_color)
        author_label.grid(row=1, column=0, padx=10, pady=10)

        author_entry = tk.Entry(add_book_window, bg=self.entry_color)
        author_entry.grid(row=1, column=1, padx=10, pady=10)

        quantity_label = tk.Label(add_book_window, text="Quantity:", bg='#3498db', fg=self.label_color)
        quantity_label.grid(row=2, column=0, padx=10, pady=10)

        quantity_entry = tk.Entry(add_book_window, bg=self.entry_color)
        quantity_entry.grid(row=2, column=1, padx=10, pady=10)

        def add_book_action():
            title = title_entry.get().strip()
            author = author_entry.get().strip()
            quantity_str = quantity_entry.get().strip()

            if title and author and quantity_str.isdigit():
                quantity = int(quantity_str)
                book_id = str(len(self.books) + 1)
                self.books[book_id] = {
                    "title": title,
                    "author": author,
                    "quantity": quantity,
                    "available": quantity,
                    "checked_out": {}
                }
                tk.messagebox.showinfo("Info", f"Book '{title}' added to the library.")
                self.save_books()
                add_book_window.destroy()
            else:
                tk.messagebox.showerror("Error", "Invalid input. Please enter valid information.")

        add_button = tk.Button(add_book_window, text="Add Book", command=add_book_action, bg=self.button_color, fg=self.label_color)
        add_button.grid(row=3, column=0, columnspan=2, pady=10)

    def remove_book(self):
        remove_book_window = tk.Toplevel(self.root)
        remove_book_window.title("Remove Book")

        # Color styling
        remove_book_window.configure(bg='#3498db')

        book_id_label = tk.Label(remove_book_window, text="Book ID:", bg='#3498db', fg=self.label_color)
        book_id_label.grid(row=0, column=0, padx=10, pady=10)

        book_id_entry = tk.Entry(remove_book_window, bg=self.entry_color)
        book_id_entry.grid(row=0, column=1, padx=10, pady=10)

        def remove_book_action():
            book_id = book_id_entry.get().strip()
            if book_id in self.books:
                del self.books[book_id]
                tk.messagebox.showinfo("Info", f"Book with ID {book_id} removed from the library.")
                self.save_books()
                remove_book_window.destroy()
            else:
                tk.messagebox.showerror("Error", f"Book with ID {book_id} not found.")

        remove_button = tk.Button(remove_book_window, text="Remove Book", command=remove_book_action, bg=self.button_color, fg=self.label_color)
        remove_button.grid(row=1, column=0, columnspan=2, pady=10)

    def checkout_book(self):
        checkout_book_window = tk.Toplevel(self.root)
        checkout_book_window.title("Checkout Book")

        # Color styling
        checkout_book_window.configure(bg='#3498db')

        book_id_label = tk.Label(checkout_book_window, text="Book ID:", bg='#3498db', fg=self.label_color)
        book_id_label.grid(row=0, column=0, padx=10, pady=10)

        book_id_entry = tk.Entry(checkout_book_window, bg=self.entry_color)
        book_id_entry.grid(row=0, column=1, padx=10, pady=10)

        user_name_label = tk.Label(checkout_book_window, text="User Name:", bg='#3498db', fg=self.label_color)
        user_name_label.grid(row=1, column=0, padx=10, pady=10)

        user_name_entry = tk.Entry(checkout_book_window, bg=self.entry_color)
        user_name_entry.grid(row=1, column=1, padx=10, pady=10)

        def checkout_book_action():
            book_id = book_id_entry.get().strip()
            user_name = user_name_entry.get().strip()

            if book_id in self.books and self.books[book_id]["available"] > 0:
                checkout_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.books[book_id]["checked_out"][user_name] = checkout_date
                self.books[book_id]["available"] -= 1
                tk.messagebox.showinfo("Info", f"Book with ID {book_id} checked out by {user_name}.")
                self.save_books()
                checkout_book_window.destroy()
            else:
                tk.messagebox.showerror("Error", f"Book with ID {book_id} is not available for checkout.")

        checkout_button = tk.Button(checkout_book_window, text="Checkout Book", command=checkout_book_action, bg=self.button_color, fg=self.label_color)
        checkout_button.grid(row=2, column=0, columnspan=2, pady=10)

    def return_book(self):
        return_book_window = tk.Toplevel(self.root)
        return_book_window.title("Return Book")

        # Color styling
        return_book_window.configure(bg='#3498db')

        book_id_label = tk.Label(return_book_window, text="Book ID:", bg='#3498db', fg=self.label_color)
        book_id_label.grid(row=0, column=0, padx=10, pady=10)

        book_id_entry = tk.Entry(return_book_window, bg=self.entry_color)
        book_id_entry.grid(row=0, column=1, padx=10, pady=10)

        user_name_label = tk.Label(return_book_window, text="User Name:", bg='#3498db', fg=self.label_color)
        user_name_label.grid(row=1, column=0, padx=10, pady=10)

        user_name_entry = tk.Entry(return_book_window, bg=self.entry_color)
        user_name_entry.grid(row=1, column=1, padx=10, pady=10)

        def return_book_action():
            book_id = book_id_entry.get().strip()
            user_name = user_name_entry.get().strip()

            if book_id in self.books and user_name in self.books[book_id]["checked_out"]:
                return_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                del self.books[book_id]["checked_out"][user_name]
                self.books[book_id]["available"] += 1
                tk.messagebox.showinfo("Info", f"Book with ID {book_id} returned by {user_name}.")
                self.save_books()
                return_book_window.destroy()
            else:
                tk.messagebox.showerror("Error", f"Book with ID {book_id} was not checked out by {user_name}.")

        return_button = tk.Button(return_book_window, text="Return Book", command=return_book_action, bg=self.button_color, fg=self.label_color)
        return_button.grid(row=2, column=0, columnspan=2, pady=10)

# Create the main window
root = tk.Tk()
app = LibraryManagementSystemGUI(root)

# Run the main loop
root.mainloop()
