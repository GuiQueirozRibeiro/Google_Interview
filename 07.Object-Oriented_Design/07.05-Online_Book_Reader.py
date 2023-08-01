'''
07.05 Online Book Reader: Design the data structures for an online book reader system.
'''

class OnlineReaderSystem:
    def __init__(self):
        self.userManager = UserManager()
        self.library = Library()
        self.display = Display()
        self.activeBook = None
        self.activeUser = None

    def getLibrary(self):
        return self.library

    def getUserManager(self):
        return self.userManager

    def getDisplay(self):
        return self.display

    def getActiveBook(self):
        return self.activeBook

    def setActiveBook(self, book):
        self.activeBook = book
        self.display.displayBook(book)

    def getActiveUser(self):
        return self.activeUser

    def setActiveUser(self, user):
        self.activeUser = user
        self.display.displayUser(user)


class Library:
    def __init__(self):
        self.books = {}

    def addBook(self, id, details, title):
        if id in self.books:
            return False
        book = Book(id, details, title)
        self.books[id] = book
        return True

    def remove(self, b):
        return self.remove(b.getId())

    def remove(self, id):
        if id in self.books:
            del self.books[id]
            return True
        return False

    def find(self, id):
        return self.books.get(id)


class UserManager:
    def __init__(self):
        self.users = {}

    def addUser(self, id, details, name):
        if id in self.users:
            return False
        user = User(id, details, name)
        self.users[id] = user
        return True

    def remove(self, u):
        return self.remove(u.getId())

    def remove(self, id):
        if id in self.users:
            del self.users[id]
            return True
        return False

    def find(self, id):
        return self.users.get(id)


class Display:
    def __init__(self):
        self.activeBook = None
        self.activeUser = None
        self.pageNumber = 0

    def displayUser(self, user):
        self.activeUser = user
        self.refreshUsername()

    def displayBook(self, book):
        self.pageNumber = 0
        self.activeBook = book

        self.refreshTitle()
        self.refreshDetails()
        self.refreshPage()

    def turnPageForward(self):
        self.pageNumber += 1
        print(f"Turning forward to page no {self.pageNumber} of book having title {self.activeBook.getTitle()}")
        self.refreshPage()

    def turnPageBackward(self):
        self.pageNumber -= 1
        print(f"Turning backward to page no {self.pageNumber} of book having title {self.activeBook.getTitle()}")
        self.refreshPage()

    def refreshUsername(self):
        print(f"User name {self.activeUser.getName()} is refreshed")

    def refreshTitle(self):
        print(f"Title of the book {self.activeBook.getTitle()} refreshed")

    def refreshDetails(self):
        print(f"Details of the book {self.activeBook.getTitle()} refreshed")

    def refreshPage(self):
        print(f"Page no {self.pageNumber} refreshed")


class Book:
    def __init__(self, id, details, title):
        self.bookId = id
        self.details = details
        self.title = title

    def getId(self):
        return self.bookId

    def setId(self, id):
        self.bookId = id

    def getDetails(self):
        return self.details

    def setDetails(self, details):
        self.details = details

    def getTitle(self):
        return self.title

    def setTitle(self, title):
        self.title = title


class User:
    def __init__(self, id, details, name):
        self.userId = id
        self.details = details
        self.name = name

    def renewMembership(self):
        pass

    def getId(self):
        return self.userId

    def setId(self, id):
        self.userId = id

    def getDetails(self):
        return self.details

    def setDetails(self, details):
        self.details = details

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name