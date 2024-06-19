import http
import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from work_at_olist.base.models import Book


def book_update(request, id):
    book = get_object_or_404(Book, id=id)
    data = json.loads(request.body)

    authors = data.pop('authors')

    book.name = data['name']
    book.edition = data['edition']
    book.publication_year = data['publication_year']
    book.save()
    book.authors.add(*authors)

    return JsonResponse(book.to_dict(), status=http.HTTPStatus.OK)


def book_read(request, id):
    book = get_object_or_404(Book, id=id)
    return JsonResponse(book.to_dict(), status=http.HTTPStatus.OK)


def book_delete(request, id):
    book = get_object_or_404(Book, id=id)
    data = book.to_dict()
    book.delete()
    return JsonResponse(data, status=http.HTTPStatus.OK)
