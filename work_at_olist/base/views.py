import http
import json

from django.core.paginator import Paginator
from django.http import JsonResponse

from work_at_olist.base.models import Author, Book

DEFAULT_AUTHORS_PER_PAGE = 10
DEFAULT_BOOKS_PER_PAGE = 10


def authors(request):
    authors = Author.objects.all()
    page = request.GET.get('page', 1)
    items_per_page = request.GET.get('num_items', DEFAULT_AUTHORS_PER_PAGE)
    name = request.GET.get('name')
    if name:
        authors = authors.filter(name__contains=name)
    paginator = Paginator(
        [author.to_dict() for author in authors],
        items_per_page
    )
    data = {'authors': paginator.page(page).object_list,
            'num_pages': paginator.num_pages,
            'curr_page': int(page)}
    return JsonResponse(data)


def book_creation(request):
    data = json.load(request)
    authors = data.pop('authors')
    book = Book.objects.create(**data)
    book.authors.add(*authors)
    return JsonResponse(book.to_dict(), status=http.HTTPStatus.CREATED)


def books_read(request):
    books = Book.objects.all()
    page = request.GET.get('page', 1)
    items_per_page = request.GET.get('num_items', DEFAULT_BOOKS_PER_PAGE)
    paginator = Paginator(
        [book.to_dict() for book in books],
        items_per_page
    )
    data = {'books': paginator.page(page).object_list,
            'num_pages': paginator.num_pages,
            'curr_page': int(page)}
    return JsonResponse(data, status=http.HTTPStatus.OK)
