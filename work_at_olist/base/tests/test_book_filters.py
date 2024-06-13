import json

from django.urls import reverse


def test_book_filter_by_name(client, books):
    """
    Certifies books can be filtered by name.
    """
    book = books[0]
    resp = client.get(reverse('base:books_list'), {'name': book.name})
    assert json.loads(resp.content)['books'] == [book.to_dict()]
