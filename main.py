class Book:

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_issued = False

    def __str__(self):
        return f"{self.title} by {self.author}, ISBN: {self.isbn}, Issued: {self.is_issued}"


class Member:

    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def __str__(self):
        return f"Member: {self.name}, ID: {self.member_id}, Borrowed Books: {[book.title for book in self.borrowed_books]}"


class Library:

    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def register_member(self, member):
        self.members.append(member)
        print(
            f"Member '{member.name}' registered with ID: {member.member_id}.")

    def issue_book(self, isbn, member_id):
        book = next(
            (b for b in self.books if b.isbn == isbn and not b.is_issued),
            None)
        member = next((m for m in self.members if m.member_id == member_id),
                      None)

        if book and member:
            book.is_issued = True
            member.borrowed_books.append(book)
            print(f"Book '{book.title}' issued to member '{member.name}'.")
        else:
            print("Book not available or member not found.")

    def return_book(self, isbn, member_id):
        book = next((b for b in self.books if b.isbn == isbn and b.is_issued),
                    None)
        member = next((m for m in self.members if m.member_id == member_id),
                      None)

        if book and member and book in member.borrowed_books:
            book.is_issued = False
            member.borrowed_books.remove(book)
            print(f"Book '{book.title}' returned by member '{member.name}'.")
        else:
            print(
                "Book or member not found, or book not issued to this member.")


# Example usage
if __name__ == "__main__":
    # Create library
    library = Library()

    # Add books
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "1234567890")
    book2 = Book("1984", "George Orwell", "2345678901")
    book3 = Book("Harry Potter Part1", "J K Rowling", "007")
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    # Register members
    member1 = Member("Alice", 1)
    member2 = Member("Bob", 2)
    member3 = Member("Charlie",7)
    
    library.register_member(member1)
    library.register_member(member2)
    library.register_member(member3)

    # Issue books
    library.issue_book("1234567890", 1)
    library.issue_book("2345678901", 2)
    library.issue_book("007", 7)
    

    # Print status
    print(book1)
    print("\n")
    print(member1)
    print("\n")
    
    # Return books
    library.return_book("1234567890", 1)

    # Print status
    print(book1)
    print("\n")
    print(member1)

    print("\n")
    print(book3)
    

