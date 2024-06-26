from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from work_at_olist.base.exceptions import ValidationError
from work_at_olist.base.models import Author, Book
from work_at_olist.base.schemas import BookIn


def validate_publication_year(year: int):
    """
    Raise ValidationError if a year is not between
    1 and 9999 (invalid).
    """
    if not 1 < year < 9999:
        raise ValidationError('Please, fill a valid publication year.')


def list_books(filters):
    books = Book.objects.all().distinct()

    publication_year = filters.publication_year
    if publication_year is not None:
        validate_publication_year(int(publication_year))

    return books


def create_book(payload_dict, response: HttpResponse):
    for author_id in payload_dict['authors']:
        get_object_or_404(Author, id=author_id)

    validate_publication_year(payload_dict['publication_year'])

    authors = payload_dict.pop('authors')
    book = Book.objects.create(**payload_dict)
    book.authors.add(*authors)
    response['Location'] = book.get_absolute_url()

    return 201, book


def update_book(book: Book, payload: BookIn):
    pub_year = payload.publication_year
    validate_publication_year(pub_year)

    book.name = payload.name
    book.edition = payload.edition
    book.publication_year = pub_year
    book.save()
    book.authors.add(*payload.authors)

    return book
