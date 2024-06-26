import pytest
from http import HTTPStatus
import json
from work_at_olist.base.models import Book


@pytest.fixture
def resp_book_removal(book, client):
    """
    Creates a request to remove a book
    and returns a response.
    """
    resp = client.delete(f'/api/books/delete/{book.pk}')
    return resp


def test_status_code_resp_book_removal(resp_book_removal):
    """
    Certifies that the status code is 200
    indicating success.
    """
    assert resp_book_removal.status_code == HTTPStatus.OK


def test_book_removed_successfully(resp_book_removal, book):
    """
    Certifies that the book was removed.
    """
    assert not Book.objects.filter(id=book.pk).exists()


def test_book_not_found_incorrect_id(client, db):
    """
    Certifies a 404 response is returned if tried
    to remove a book inserting non-existent id.
    """
    resp = client.delete('/api/books/delete/1234')
    assert resp.status_code == HTTPStatus.NOT_FOUND


def test_deleted_book_returned(resp_book_removal, book, author):
    """
    Certifies that the deleted book is returned
    after removed.
    """
    data = {'id': book.pk,
            'name': 'Book 01',
            'edition': book.edition,
            'publication_year': book.publication_year,
            'authors': [author.pk]}
    assert json.loads(resp_book_removal.content) == data
