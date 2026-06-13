class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        from lib.author import Author

        if not isinstance(author, Author):
            raise Exception("author must be Author")

        self._author = author

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, book):
        from lib.book import Book

        if not isinstance(book, Book):
            raise Exception("book must be Book")

        self._book = book

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if not isinstance(date, str):
            raise Exception("date must be string")

        self._date = date

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, royalties):
        if not isinstance(royalties, int):
            raise Exception("royalties must be int")

        self._royalties = royalties

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]