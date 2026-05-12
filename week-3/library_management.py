import uuid


class Book:
    def __init__(self, title, author, isbn, is_available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"


class Member:
    def __init__(self, name):
        self.name = name
        self.member_id = uuid.uuid4()
        self.borrowed_books = []

    def __str__(self):
        return f"Member Id: {self.member_id}, Name: {self.name}"


class Librarian:
    def __init__(self, name):
        self.name = name
        self.employee_id = uuid.uuid4()

    def __str__(self):
        return f"Employee Id: {self.employee_id}, Name: {self.name}"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = {}
        self.members = {}

    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError(f"{book} must be of type Book.")

        self.books[book.isbn] = book
        print(f"Book {book} is added to the library.")

    def remove_book(self, isbn):
        if isbn in self.books:
            del self.books[isbn]
            print(f"Book with the ISBN {isbn} is removed from the library.")
        else:
            raise ValueError(f"No book with ISBN {isbn} is in the library.")

    def register_member(self, member):
        if not isinstance(member, Member):
            raise TypeError(f"{member} must be of type Member.")

        if member.member_id not in self.members:
            self.members[member.member_id] = member
            print(f"{member} is registered to the library members.")
        else:
            raise ValueError(
                f"{member.name} with member id {member.member_id} is already a member of the library.")

    def borrow_book(self, member_id, isbn):
        if member_id not in self.members:
            raise ValueError(
                f"{member_id} is not registered in the library members.")

        if isbn not in self.books:
            raise ValueError(
                f"No book with the ISBN {isbn} is in the library.")

        member = self.members[member_id]
        book = self.books[isbn]

        if book in member.borrowed_books:
            raise ValueError(
                f"Member with member id {member_id} has already borrowed the book with ISBN {isbn}")

        if not book.is_available:
            raise ValueError(
                f"Book with ISBN {isbn} is not available to be borrowed.")

        book.is_available = False
        member.borrowed_books.append(book)

        print(
            f"Book with the ISBN {isbn} is borrowed by the member {member_id}.")

    def return_book(self, member_id, isbn):
        if member_id not in self.members:
            raise ValueError(
                f"{member_id} is not registered in the library members.")

        member = self.members[member_id]
        book = self.books[isbn]

        if book not in member.borrowed_books:
            raise ValueError(
                f"Book with the ISBN {isbn} is not borrowed by the member {member_id}")

        book.is_available = True

        for index, borrowed_book in enumerate(member.borrowed_books):
            if book.isbn == borrowed_book.isbn:
                del member.borrowed_books[index]
                break

        print(
            f"Book with the ISBN {isbn} is returned by the member {member_id}.")

    def search_books(self, query):
        result = []

        for book in self.books.values():
            if query.lower() in book.title.lower() or query.lower() in book.author.lower():
                result.append(book)

        return result

    def available_books(self):
        for book in self.books.values():
            if book.is_available:
                print(f"{book.title} by {book.author}")


class LibrarianAccess(Library):
    def __init__(self, name):
        self.librarians = {}
        super().__init__(name)

    def add_librarian(self, librarian):
        if not isinstance(librarian, Librarian):
            raise TypeError(
                f"{librarian} must be of type Librarian.")

        self.librarians[librarian.employee_id] = librarian
        print(f"{librarian} is added as a librarian to the library.")

    def remove_member(self, member_id):
        if member_id in self.members:
            for book in self.members[member_id].borrowed_books:
                super().return_book(member_id, book.isbn)
            del self.members[member_id]
        else:
            raise ValueError(
                f"{member_id} is not registered in the library members.")

    def generate_report(self):
        total_books = len(self.books)
        total_members = len(self.members)
        available_books = sum(
            1 for book in self.books.values() if book.is_available)
        borrowed_books = total_books - available_books

        print(f"Total books: {total_books}")
        print(f"Available books: {available_books}")
        print(f"Total members: {total_members}")
        print(f"Borrowed books: {borrowed_books}")


def main():
    book1 = Book("The Pragmatic Programmer", "David Thomas", "978-013957059")

    book2 = Book("Clean Code: A Handbook of Agile Software Craftsmanship",
                 "Robert C. Martin", "978-0132350884")

    book3 = Book("Introduction to Algorithms",
                 "Thomas H. Cormen", "978-0262046305")

    book4 = Book("Structure and Interpretation of Computer Programs",
                 "Harold Abelson", "978-0262510875")

    book5 = Book(
        "The Mythical Man-Month: Essays on Software Engineering", "Frederick P. Brooks Jr.", "978-0201835953")

    member1 = Member("Maqbool Baig")
    member2 = Member("Ali Khan")
    member3 = Member("Ayesha Ahmed")

    librarian1 = Librarian("Zahid Hussain")
    librarian2 = Librarian("Sana Malik")

    library = LibrarianAccess("Quaid-e-Azam Library")

    print("================================================================================")
    print("Books Addition Test")
    print("================================================================================\n")

    try:
        library.add_book(book1)
        library.add_book(book2)
        library.add_book(book3)
        library.add_book(book4)
        library.add_book(book5)
        library.add_book("Python Crash Course")
    except TypeError as e:
        print(e)

    print("\n================================================================================")
    print("Books Removal Test")
    print("================================================================================\n")

    try:
        library.remove_book(book5.isbn)
        library.remove_book("978-1718502703")
    except ValueError as e:
        print(e)

    print("\n================================================================================")
    print("Members Registration Test")
    print("================================================================================\n")

    try:
        library.register_member(member1)
        library.register_member(member2)
        library.register_member("Bilal Yousaf")
    except TypeError as e:
        print(e)

    try:
        library.register_member(member1)
    except ValueError as e:
        print(e)

    print("\n================================================================================")
    print("Books Borrow Test")
    print("================================================================================\n")

    try:
        library.borrow_book(member1.member_id, book1.isbn)
        library.borrow_book(member2.member_id, book2.isbn)
        library.borrow_book(member1.member_id, book3.isbn)
        library.borrow_book(member3.member_id, book4.isbn)
    except ValueError as e:
        print(e)

    try:
        library.borrow_book(member1.member_id, "978-1718502703")
    except ValueError as e:
        print(e)

    try:
        library.borrow_book(member1.member_id, book1.isbn)
    except ValueError as e:
        print(e)

    try:
        library.borrow_book(member2.member_id, book1.isbn)
    except ValueError as e:
        print(e)

    print("\n================================================================================")
    print("Book Return Test")
    print("================================================================================\n")

    try:
        library.return_book(member1.member_id, book3.isbn)
        library.return_book(member3.member_id, book3.isbn)
    except ValueError as e:
        print(e)

    try:
        library.return_book(member1.member_id, book2.isbn)
    except ValueError as e:
        print(e)

    print("\n================================================================================")
    print("Books Search Test")
    print("================================================================================\n")

    searched = library.search_books("program")

    if searched:
        for index, book in enumerate(searched, start=1):
            print(f"{index}. {book.title} by {book.author}")

    print("\n================================================================================")
    print("Available Books Test")
    print("================================================================================\n")
    library.available_books()

    print("\n================================================================================")
    print("Librarian Addition Test")
    print("================================================================================\n")

    try:
        library.add_librarian(librarian1)
        library.add_librarian(librarian2)
        library.add_librarian("Fatima Bibi")
    except TypeError as e:
        print(e)

    print("\n================================================================================")
    print("Remove Member Test")
    print("================================================================================\n")

    try:
        library.remove_member(member2.member_id)
        library.remove_member(member3.member_id)
    except ValueError as e:
        print(e)

    print("\n================================================================================")
    print("Library Report")
    print("================================================================================\n")
    library.generate_report()


if __name__ == "__main__":
    main()
