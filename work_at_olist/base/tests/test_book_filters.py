import json

from django.urls import reverse

from work_at_olist.base.models import Author


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


def test_book_filter_by_authors_id(client, books):
    """
    Certifies that books can be filtered by authors ID.
    One more author is added to book_1 in order to test that
    no duplicate results return. If, in the query that filters
    the authors in our view, we remove the '.distinct()', this
    test will fail because book_01 will return twice.
    """
    book_0 = books[0]
    book_1 = books[1]
    a0 = Author.objects.filter(id=book_0.authors.first().pk).first()
    a1 = Author.objects.filter(id=book_1.authors.first().pk).first()
    book_1.authors.add(a0)
    resp = client.get(reverse('base:books_list'), {'authors': [a0.pk, a1.pk]})
    assert json.loads(resp.content)['books'] == [book_0.to_dict(), book_1.to_dict()]


def test_book_filter_by_publication_year(client, books):
    """
    Certifies books can be filtered by publication year.
    """
    book = books[0]
    book.publication_year = 2010
    book.save()
    resp = client.get(reverse('base:books_list'), {'publication_year': 2010})
    assert json.loads(resp.content)['books'] == [book.to_dict()]
