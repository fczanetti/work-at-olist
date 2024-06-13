import pytest
from work_at_olist.base.models import Author, Book


@pytest.fixture
def author(db):
    """
    Creates and returns an author.
    """
    author = Author.objects.create(name='Author 01')
    return author


@pytest.fixture
def book(author, db):
    """
    Creates and returns a book.
    """
    book = Book.objects.create(name='Book 01', edition=1, publication_year=2024)
    book.authors.add(author)
    return book


@pytest.fixture
def books(db):
    """
    Creates and returns some books.
    """
    authors = [Author.objects.create(name=f'Author {i}') for i in range(10)]
    books = []
    for i, author in enumerate(authors):
        b = Book.objects.create(name=f'Book {i}', edition=1, publication_year=2024)
        b.authors.add(author)
        books.append(b)
    return books
