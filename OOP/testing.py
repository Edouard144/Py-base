# Create library
library = Library()

# Create books
book1 = Book("1984", "George Orwell")
book2 = Book("Atomic Habits", "James Clear")

# Add books
library.add_book(book1)
library.add_book(book2)

# Create user
user1 = User("Edouard")

library.add_user(user1)

# Use system
library.show_available_books()

user1.borrow(book1)
user1.borrow(book2)

library.show_available_books()

user1.return_book(book1)

library.show_available_books()