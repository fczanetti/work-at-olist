import pytest
from django.urls import reverse
from http import HTTPStatus


@pytest.fixture
def resp_authors_page(client):
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
