import json

import pytest
from http import HTTPStatus

from work_at_olist.base.models import Author
from work_at_olist.base.schemas import AuthorOut
from work_at_olist.django_assertions import assert_contains, assert_not_contains


@pytest.fixture
def authors(db):
    a = [f"Author {i}" for i in range(23)]
    list_authors = [Author.objects.create(name=name) for name in a]
    return list_authors


@pytest.fixture
def resp_authors_page(client, authors):
    """
    Creates a request to authors page and returns a response.
    """
    resp = client.get('/api/authors')
    return resp


@pytest.fixture
def resp_authors_page_2(client, authors):
    """
    Creates a request to authors page 2 and returns a response.
    """
    resp = client.get('/api/authors', {'page': 2})
    return resp


def test_status_code_authors_page(resp_authors_page):
    """
    Certifies that:
    - authors page is loaded successfully;
    - num_pages (number of pages) and curr_page (current page) are present.
    """
    assert resp_authors_page.status_code == HTTPStatus.OK
    assert json.loads(resp_authors_page.content)['num_pages'] == 3
    assert json.loads(resp_authors_page.content)['curr_page'] == 1


def test_authors_present_in_authors_page(resp_authors_page, authors):
    """
    Certifies that the authors are listed in authors page. This test
    considers that the user is accessing the first page.
    """
    for author in authors[:10]:
        author_out = AuthorOut.from_orm(author)
        assert_contains(resp_authors_page, json.dumps(author_out.dict()))


def test_correct_authors_shown_page_2(resp_authors_page_2, authors):
    """
    Certifies that:
    - authors 0 to 9 are not shown when requesting page 2;
    - authors from 10 to 19 are shown in page 2.
    """
    for author in authors[:10]:
        author_out = AuthorOut.from_orm(author)
        assert_not_contains(resp_authors_page_2, json.dumps(author_out.dict()))
    for author in authors[10:20]:
        author_out = AuthorOut.from_orm(author)
        assert_contains(resp_authors_page_2, json.dumps(author_out.dict()))


def test_filter_by_name(client, authors):
    """
    Certifies that the response is correct
    when filtering by name.
    """
    author = Author.objects.get(name='Author 5')
    author_out = AuthorOut.from_orm(author)
    resp = client.get('/api/authors', {'name': author.name})
    assert json.loads(resp.content)['items'] == [author_out.dict()]
