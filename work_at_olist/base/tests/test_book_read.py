import json

import pytest
from http import HTTPStatus


@pytest.fixture
def resp_book_read_page(client, book):
    """
    Creates a request to read a book and
    returns a response.
    """
    resp = client.get(f'/api/books/{book.pk}')
    return resp


def test_status_code_book_read_page(resp_book_read_page):
    """
    Certifies that book read page is
    loaded successfully.
    """
    assert resp_book_read_page.status_code == HTTPStatus.OK


def test_book_is_present_on_page(resp_book_read_page, book):
    """
    Certifies that the book is shown on read page.
    """
    assert json.loads(resp_book_read_page.content) == book.to_dict()


def test_book_not_found_incorrect_id(client, db):
    """
    Certifies that a 404 response is returned
    if tried to read a book with invalid id.
    """
    resp = client.get('/api/books/1234')
    assert resp.status_code == HTTPStatus.NOT_FOUND
