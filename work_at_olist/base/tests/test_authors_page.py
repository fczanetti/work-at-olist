import json

import pytest
from django.urls import reverse
from http import HTTPStatus

from work_at_olist.base.models import Author
from work_at_olist.django_assertions import assert_contains


@pytest.fixture
def authors(db):
    a = [f"Author {i}" for i in range(3)]
    list_authors = [Author.objects.create(name=name) for name in a]
    return list_authors


@pytest.fixture
def resp_authors_page(client, authors):
    """
    Creates a request to authors page and returns a response.
    """
    resp = client.get(reverse('base:authors'))
    return resp


def test_status_code_authors_page(resp_authors_page):
    """
    Certifies that authors page is loaded successfully.
    """
    assert resp_authors_page.status_code == HTTPStatus.OK


def test_authors_present_in_authors_page(resp_authors_page, authors):
    """
    Certifies that the authors are listed in authors page.
    """
    for author in authors:
        assert_contains(resp_authors_page, json.dumps(author.to_dict()))
