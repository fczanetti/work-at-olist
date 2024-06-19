from typing import List, Any
from math import ceil

from ninja import Router, Schema, Query
from .models import Author, Book
from .schemas import AuthorOut, AuthorFilterSchema, BookOut, BookFilterSchema, BookIn
from ninja.pagination import paginate, PaginationBase
from django.conf import settings
from django.http import HttpResponse

router = Router()


class CustomPagination(PaginationBase):
    class Input(Schema):
        skip: int = 0
        page: int = 1
        num_items: int = settings.NINJA_PAGINATION_PER_PAGE

    class Output(Schema):
        items: List[Any]
        num_pages: int
        curr_page: int

    def paginate_queryset(self, queryset, pagination: Input, **params):
        skip = (pagination.page - 1) * pagination.num_items
        return {
            'items': queryset[skip: skip + pagination.num_items],
            'num_pages': ceil(queryset.count() / pagination.num_items),
            'curr_page': pagination.page,
        }


@router.get('/authors', response=List[AuthorOut])
@paginate(CustomPagination)
def authors(request, filters: AuthorFilterSchema = Query(...)):
    authors = Author.objects.all()
    authors = filters.filter(authors)

    return authors


@router.get('/books', response=List[BookOut])
@paginate(CustomPagination)
def books_list(request, filters: BookFilterSchema = Query(...)):
    books = Book.objects.all().distinct()
    books = filters.filter(books)

    return books


@router.post('/books/create', response={201: BookOut})
def book_creation(request, payload: BookIn, response: HttpResponse):
    payload_dict = payload.dict()
    authors = payload_dict.pop('authors')
    book = Book.objects.create(**payload_dict)
    book.authors.add(*authors)
    response['Location'] = book.get_absolute_url()
    return book
