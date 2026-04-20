class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
    def borrow(self, book):
        if not book.is_borrowed:
            book.borrow_book()
            self.borrowed_books.append(book) 
        else:
            print(f"The book is not available")

    def return_book(self, book):
        if book.is_borrowed:
            book.is_borrowed = false
            self.borrowed_books.remove(book)
        else:
            print("The book was never borrowed")
                          