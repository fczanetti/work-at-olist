from typing import List, Any
from math import ceil

from ninja import Router, Schema, Query
from .models import Author
from .schemas import AuthorOut, AuthorFilterSchema
from ninja.pagination import paginate, PaginationBase
from django.conf import settings

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

    # items_attribute: str = "authors"

    def paginate_queryset(self, queryset, pagination: Input, **params):
        skip = (pagination.page - 1) * pagination.num_items
        return {
            'items': queryset[skip: skip + pagination.num_items],
            'num_pages': ceil(queryset.count() / pagination.num_items),
            'curr_page': pagination.page,
        }


@router.get('/', response=List[AuthorOut])
@paginate(CustomPagination)
def authors(request, filters: AuthorFilterSchema = Query(...)):
    authors = Author.objects.all()
    authors = filters.filter(authors)

    return authors
