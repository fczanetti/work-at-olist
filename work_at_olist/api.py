from ninja import NinjaAPI


api = NinjaAPI()

api.add_router('/authors', 'work_at_olist.base.api.router')
