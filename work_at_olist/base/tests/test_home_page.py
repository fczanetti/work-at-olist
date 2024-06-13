import pytest
from django.urls import reverse
from http import HTTPStatus

from work_at_olist.django_assertions import assert_contains


@pytest.fixture
def resp_home_page(client):
    """
    Creates a request to home page and returns a response.
    """
    resp = client.get(reverse('base:home'))
    return resp


def test_status_code_home_page(resp_home_page):
    """
    Certifies home page is loaded successfully.
    """
    assert resp_home_page.status_code == HTTPStatus.OK


def test_page_title_is_present(resp_home_page):
    """
    Certifies that the title of the page is present.
    """
    assert_contains(resp_home_page, '<title>API - Books</title>')
