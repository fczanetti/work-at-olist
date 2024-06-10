from django.core.paginator import Paginator
from django.http import JsonResponse

from work_at_olist.base.models import Author

DEFAULT_ITEMS_PER_PAGE = 10


def authors(request):
    authors = Author.objects.all()
    page = request.GET.get('page', 1)
    items_per_page = request.GET.get('num_items', DEFAULT_ITEMS_PER_PAGE)
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
