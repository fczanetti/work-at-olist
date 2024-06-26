from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router, Query

from .books import create_book, update_book, list_books
from .models import Author, Book
from .schemas import AuthorOut, AuthorFilterSchema, BookOut, BookFilterSchema, BookIn, CustomPagination
from ninja.pagination import paginate
from django.http import HttpResponse

router = Router()


@router.get('/authors', response=List[AuthorOut])
@paginate(CustomPagination)
def authors(request, filters: AuthorFilterSchema = Query(...)):
    authors = Author.objects.all()
    authors = filters.filter(authors)

    return authors


@router.get('/books', response=List[BookOut])
@paginate(CustomPagination)
def books_list(request, filters: BookFilterSchema = Query(...)):
    books = list_books(filters)
    books = filters.filter(books)

    return books


@router.post('/books/create', response={201: BookOut})
def book_creation(request, payload: BookIn, response: HttpResponse):
    payload_dict = payload.dict()
    book = create_book(payload_dict, response)

    return book


@router.get('/books/{book_id}', response=BookOut)
def book_read(request, book_id: int):
    book = get_object_or_404(Book, id=book_id)

    return book


@router.put('/books/update/{book_id}', response=BookOut)
def book_update(request, book_id: int, payload: BookIn):
    book = get_object_or_404(Book, id=book_id)

    return update_book(book, payload)


@router.delete('/books/delete/{book_id}', response=BookOut)
def book_delete(request, book_id: int):
    book = get_object_or_404(Book, id=book_id)
    data = BookOut.from_orm(book).dict()
    book.delete()

    return data
