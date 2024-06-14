import json

from django.urls import reverse


def test_book_filter_by_name(client, books):
    """
    Certifies books can be filtered by name.
    """
    book = books[0]
    resp = client.get(reverse('base:books_list'), {'name': book.name})
    assert json.loads(resp.content)['books'] == [book.to_dict()]


def test_book_filter_by_edition(client, books):
    """
    Certifies books can be filtered by edition.
    """
    book_1 = books[1]
    book_2 = books[2]
    book_1.edition = 5
    book_1.save()
    book_2.edition = 5
    book_2.save()
    resp = client.get(reverse('base:books_list'), {'edition': 5})
    assert json.loads(resp.content)['books'] == [book_1.to_dict(), book_2.to_dict()]
