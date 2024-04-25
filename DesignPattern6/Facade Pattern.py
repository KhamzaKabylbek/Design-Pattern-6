class LibraryFacade:
    def __init__(self):
        self.book_inventory = BookInventory()
        self.user_management = UserManagement()

    def borrow_book(self, user_id, book_title):
        if self.user_management.validate_user(user_id):
            if self.book_inventory.check_availability(book_title):
                self.book_inventory.borrow_book(book_title)
                self.user_management.record_borrow(user_id, book_title)
                print(f"Book '{book_title}' borrowed successfully by user {user_id}.")
            else:
                print(f"Book '{book_title}' is not available for borrowing.")
        else:
            print(f"User {user_id} is not valid.")

    def return_book(self, user_id, book_title):
        if self.user_management.validate_user(user_id):
            self.book_inventory.return_book(book_title)
            self.user_management.record_return(user_id, book_title)
            print(f"Book '{book_title}' returned successfully by user {user_id}.")
        else:
            print(f"User {user_id} is not valid.")

    def search_book(self, query):
        results = self.book_inventory.find_book(query)
        if results:
            print("Search results:")
            for book in results:
                print(book)
        else:
            print("No matching books found.")

    def check_availability(self, book_title):
        if self.book_inventory.check_availability(book_title):
            print(f"Book '{book_title}' is available.")
        else:
            print(f"Book '{book_title}' is not available.")

class BookInventory:
    def __init__(self):
        self.books = {}

    def find_book(self, query):
        return [book for book in self.books.values() if query.lower() in book.lower()]

    def check_availability(self, book_title):
        return book_title in self.books

    def borrow_book(self, book_title):
        del self.books[book_title]

    def return_book(self, book_title):
        self.books[book_title] = True

class UserManagement:
    def __init__(self):
        self.users = {}

    def validate_user(self, user_id):
        return user_id in self.users

    def record_borrow(self, user_id, book_title):
        pass

    def record_return(self, user_id, book_title):
        pass

def test_library_facade():
    library_facade = LibraryFacade()

    library_facade.borrow_book("user1", "Harry Potter")
    library_facade.borrow_book("user2", "Game of Thrones")
    library_facade.borrow_book("user1", "Python Programming")

    library_facade.return_book("user1", "Harry Potter")

    library_facade.search_book("Harry")
    library_facade.search_book("Python")
    library_facade.search_book("Lord of the Rings")

    library_facade.check_availability("Python")
    library_facade.check_availability("Lord of the Rings")

if __name__ == "__main__":
    test_library_facade()
