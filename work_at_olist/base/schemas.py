from math import ceil

from django.conf import settings
from ninja import ModelSchema, FilterSchema, Schema
from ninja.pagination import PaginationBase
from pydantic import Field

from work_at_olist.base.models import Author, Book
from typing import Optional, List, Any


class AuthorOut(ModelSchema):
    class Meta:
        model = Author
        fields = ['id', 'name']


class BookOut(ModelSchema):
    class Meta:
        model = Book
        fields = ['id', 'name', 'edition', 'publication_year', 'authors']


class BookIn(ModelSchema):
    class Meta:
        model = Book
        fields = ['name', 'edition', 'publication_year', 'authors']


class AuthorFilterSchema(FilterSchema):
    name: Optional[str] = Field(None, json_schema_extra={'q': 'name__contains'})


class BookFilterSchema(FilterSchema):
    name: Optional[str] = Field(None, json_schema_extra={'q': 'name__contains'})
    edition: Optional[int] = None
    authors: Optional[list[int]] = Field(None, json_schema_extra={'q': 'authors__in'})
    publication_year: Optional[int] = None


class CustomPagination(PaginationBase):
    class Input(Schema):
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
