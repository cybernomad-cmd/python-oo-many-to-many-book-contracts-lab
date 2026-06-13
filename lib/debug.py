from lib.author import Author
from lib.book import Book
from lib.contract import Contract

author1 = Author("Leon")
author2 = Author("John")

book1 = Book("Python Basics")
book2 = Book("Advanced Python")

contract1 = author1.sign_contract(
    book1,
    "2026-06-13",
    5000
)

contract2 = author1.sign_contract(
    book2,
    "2026-06-13",
    3000
)

contract3 = author2.sign_contract(
    book1,
    "2026-06-14",
    2000
)

print(author1.books())
print(author1.total_royalties())
print(book1.authors())
print(Contract.contracts_by_date("2026-06-13"))