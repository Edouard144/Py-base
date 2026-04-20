class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title
        self.is_borrowed = false

    def borrow_book(self):
        if not self.is_borrowed:
            self.is_borrowed = true
            print(f"The book named {self.title} was borrowed")
        else:
            print(f"The book has been borrowed") 
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = false
            print(f"The book has been returned well")
        else:
            print("The book was never rent brother")
