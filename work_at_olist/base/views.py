import http
import json

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from work_at_olist.base.models import Book

DEFAULT_BOOKS_PER_PAGE = 10


def book_creation(request):
    data = json.load(request)

    authors = data.pop('authors')
    book = Book.objects.create(**data)
    book.authors.add(*authors)

    response = JsonResponse(book.to_dict(), status=http.HTTPStatus.CREATED)
    response['Location'] = book.get_absolute_url()

    return response


def books_list(request):
    books = Book.objects.all()

    page = request.GET.get('page', 1)
    items_per_page = request.GET.get('num_items', DEFAULT_BOOKS_PER_PAGE)
    name = request.GET.get('name')

    edition = request.GET.get('edition')
    authors = list(map(int, request.GET.getlist('authors')))
    publication_year = request.GET.get('publication_year')

    if name:
        books = books.filter(name__contains=name)

    if edition:
        books = books.filter(edition=edition)

    if authors:
        books = books.filter(authors__in=authors).distinct()

    if publication_year:
        books = books.filter(publication_year=publication_year)

    paginator = Paginator(
        [book.to_dict() for book in books],
        items_per_page
    )
    data = {'books': paginator.page(page).object_list,
            'num_pages': paginator.num_pages,
            'curr_page': int(page)}
    return JsonResponse(data, status=http.HTTPStatus.OK)


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
