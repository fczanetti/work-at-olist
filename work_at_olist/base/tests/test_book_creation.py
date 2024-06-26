import json

import pytest
from http import HTTPStatus

from work_at_olist.base.models import Book
from work_at_olist.base.schemas import BookOut


@pytest.fixture
def resp_book_creation(client, author):
    """
    Creates a book via POST request and
    returns a response.
    """
    data = {'name': 'Book 01',
            'edition': 1,
            'publication_year': 2023,
            'authors': [author.pk]}
    resp = client.post('/api/books/create', data, content_type='application/json')
    return resp


def test_book_creation_status_code(resp_book_creation):
    """
    Certifies that the response status code is 201,
    indicating book created successfully.
    """
    assert resp_book_creation.status_code == HTTPStatus.CREATED


def test_book_created(resp_book_creation, author):
    """
    Certifies a book was created and saved.
    """
    assert Book.objects.filter(name='Book 01').exists()


def test_book_returned_after_created(resp_book_creation):
    """
    Certifies the book is returned after its creation.
    """
    book = Book.objects.first()
    book_out = BookOut.from_orm(book)
    assert json.loads(resp_book_creation.content) == book_out.dict()


def test_book_location_informed_after_creation(resp_book_creation):
    """
    Certifies the location of the book is informed
    after creation.
    """
    book = Book.objects.first()
    assert resp_book_creation.headers['Location'] == book.get_absolute_url()


def test_book_creation_error_nonexistent_author_id(client, db):
    """
    Certifies that a 404 response is returned if the author ID does
    not exist in the database.
    """
    data = {'name': 'Book 01',
            'edition': 1,
            'publication_year': 2023,
            'authors': [150]}
    resp = client.post('/api/books/create', data, content_type='application/json')
    assert resp.status_code == HTTPStatus.NOT_FOUND


def test_book_creation_error_invalid_publication_year(client, db, author):
    """
    Certifies that a 400 response is returned when filled an
    invalid publication year.
    """
    data = {'name': 'Book 01',
            'edition': 1,
            'publication_year': 20233,
            'authors': [author.pk]}
    resp = client.post('/api/books/create', data, content_type='application/json')
    assert resp.status_code == HTTPStatus.BAD_REQUEST
    assert json.loads(resp.content) == {"message": "Please, fill a valid publication year."}
