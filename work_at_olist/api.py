from django.http import JsonResponse
from ninja import NinjaAPI

from work_at_olist.base.exceptions import ValidationError

api = NinjaAPI()

api.add_router('/', 'work_at_olist.base.api.router')


@api.exception_handler(ValidationError)
def validation_error_handler(request, exc):
    error = str(exc)
    return JsonResponse({"message": f"{error}"}, status=400)
