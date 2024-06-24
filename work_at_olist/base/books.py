from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from work_at_olist.base.models import Author, Book
from work_at_olist.base.schemas import BookIn


def create_book(payload_dict, response: HttpResponse):
    for author_id in payload_dict['authors']:
        get_object_or_404(Author, id=author_id)

    if not 1 < payload_dict['publication_year'] < 9999:
        return 400, {'message': 'Please, fill a valid year.'}

    authors = payload_dict.pop('authors')
    book = Book.objects.create(**payload_dict)
    book.authors.add(*authors)
    response['Location'] = book.get_absolute_url()

    return 201, book


def update_book(book: Book, payload: BookIn):
    book.name = payload.name
    book.edition = payload.edition
    book.publication_year = payload.publication_year
    book.save()
    book.authors.add(*payload.authors)
    return book
