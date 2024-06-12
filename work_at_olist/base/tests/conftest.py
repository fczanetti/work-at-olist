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
