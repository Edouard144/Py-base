class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)

    def show_available_books(self):
        print("Available books:")
        for book in self.books:
            if not book.is_borrowed:
                print(f"- {book.title} by {book.author}")