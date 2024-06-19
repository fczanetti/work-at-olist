from ninja import NinjaAPI


api = NinjaAPI()

api.add_router('/', 'work_at_olist.base.api.router')
