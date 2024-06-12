import json

import pytest
from django.urls import reverse
from http import HTTPStatus
from work_at_olist.base.models import Book


@pytest.fixture
def book_to_update(db, author):
    """
    Creates and returns a book to be updated.
    """
    book = Book.objects.create(name='Book to be Updated', edition=1, publication_year=2024)
    book.authors.add(author)
    return book


@pytest.fixture
def resp_book_update(book_to_update, client, author):
    """
    Creates a request updating a book and returns a response.
    """
    data = {'name': 'New Title',
            'edition': 1,
            'publication_year': 2024,
            'authors': [author.pk]}
    resp = client.put(reverse('base:book_update',
                              args=(book_to_update.pk,)), data,
                      content_type='application/json')
    return resp


def test_book_updated_status_code(resp_book_update):
    """
    Certifies that the status code from the updating
    response is correct.
    """
    assert resp_book_update.status_code == HTTPStatus.OK


def test_book_updated(resp_book_update):
    """
    Certifies that the book was updated.
    """
    assert Book.objects.filter(name='New Title').exists()
    assert not Book.objects.filter(name='Book to be Updated').exists()


def test_book_returned_after_update(resp_book_update, book_to_update):
    """
    Certifies the book is returned after updated.
    """
    book = Book.objects.get(id=book_to_update.pk)
    assert json.loads(resp_book_update.content) == book.to_dict()


def test_book_not_found(client, author):
    """
    Certifies that a 404 response is raised when
    trying to update a book that does not exist.
    """
    data = {'name': 'Title',
            'edition': 1,
            'publication_year': 2024,
            'authors': [author.pk]}
    resp = client.put(reverse('base:book_update',
                              args=(1234,)), data,
                      content_type='application/json')
    assert resp.status_code == HTTPStatus.NOT_FOUND
