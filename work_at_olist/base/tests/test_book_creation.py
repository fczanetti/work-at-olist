import json

import pytest
from django.urls import reverse
from http import HTTPStatus

from work_at_olist.base.models import Book


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
    resp = client.post(reverse('base:book_creation'), data, content_type='application/json')
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
    assert json.loads(resp_book_creation.content) == book.to_dict()
