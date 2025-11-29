import json
from pathlib import Path
from library_manager.book import Book

class LibraryInventory:
    def __init__(self, file_path="catalog.json"):
        self.file_path = Path(file_path)
        self.books = []
        self.load_data()

    def load_data(self):
        if self.file_path.exists():
            try:
                data = json.load(open(self.file_path))
                self.books = [Book(**item) for item in data]
            except:
                self.books = []
        else:
            self.books = []

    def save_data(self):
        with open(self.file_path, "w") as f:
            json.dump([b.to_dict() for b in self.books], f, indent=4)

    def add_book(self, title, author, isbn):
        b = Book(title, author, isbn)
        self.books.append(b)
        self.save_data()

    def search_by_isbn(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

    def search_by_title(self, title):
        return [b for b in self.books if title.lower() in b.title.lower()]

    def all_books(self):
        return self.books
