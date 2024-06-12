import json
from http import HTTPStatus

import pytest
from django.urls import reverse

from work_at_olist.base.models import Author, Book
from work_at_olist.django_assertions import assert_contains


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


@pytest.fixture
def resp_books_page(books, client):
    """
    Creates a request to books page and returns a response.
    """
    resp = client.get(reverse('base:books'))
    return resp


def test_books_page_loaded_successfully(resp_books_page):
    """
    Certifies that books page is loaded successfully.
    """
    assert resp_books_page.status_code == HTTPStatus.OK


def test_books_present_books_page(resp_books_page, books):
    """
    Certifies that the books are present in books page.
    """
    for book in books:
        assert_contains(resp_books_page, json.dumps(book.to_dict()))
