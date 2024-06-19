from ninja import ModelSchema, FilterSchema
from pydantic import Field

from work_at_olist.base.models import Author, Book
from typing import Optional


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
