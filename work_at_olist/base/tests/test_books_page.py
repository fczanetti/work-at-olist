import json
from http import HTTPStatus

import pytest

from work_at_olist.base.schemas import BookOut
from work_at_olist.django_assertions import assert_contains, assert_not_contains


@pytest.fixture
def resp_books_page(books, client):
    """
    Creates a request to books page and returns a response.
    """
    resp = client.get('/api/books')
    return resp


@pytest.fixture
def resp_books_page_2(books, client):
    """
    Creates a request to books page 2 and returns a response.
    """
    resp = client.get('/api/books', {'page': 2, 'num_items': 3})
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
        book_out = BookOut.from_orm(book)
        assert_contains(resp_books_page, json.dumps(book_out.dict()))


def test_correct_books_shown_page_2(resp_books_page_2, books):
    """
    Certifies that the correct books are
    shown in page 2.
    """
    for book in books[3:6]:
        book_out = BookOut.from_orm(book)
        assert_contains(resp_books_page_2, json.dumps(book_out.dict()))
    for book in books[0:3]:
        book_out = BookOut.from_orm(book)
        assert_not_contains(resp_books_page_2, json.dumps(book_out.dict()))


def test_correct_number_of_pages_and_current_books_page(resp_books_page_2):
    """
    Certifies that the number of pages shown is correct
    and current page is also present.
    """
    assert json.loads(resp_books_page_2.content)['num_pages'] == 4
    assert json.loads(resp_books_page_2.content)['curr_page'] == 2
