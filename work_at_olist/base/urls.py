from django.urls import path
from work_at_olist.base import views


app_name = 'base'
urlpatterns = [
    path('authors', views.authors, name='authors'),
]
