from math import ceil
from typing import List, Any

from django.conf import settings
from ninja import Schema
from ninja.pagination import PaginationBase


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
