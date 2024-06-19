from ninja import ModelSchema, FilterSchema
from pydantic import Field

from work_at_olist.base.models import Author
from typing import Optional


class AuthorOut(ModelSchema):
    class Meta:
        model = Author
        fields = ['id', 'name']


class AuthorFilterSchema(FilterSchema):
    name: Optional[str] = Field(None, json_schema_extra={'q': 'name__contains'})
