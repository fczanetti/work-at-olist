from django.http import JsonResponse

from work_at_olist.base.models import Author


def authors(request):
    authors = [author.to_dict() for author in Author.objects.all()]
    return JsonResponse({'authors': authors})
