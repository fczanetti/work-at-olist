from django.urls import path
from work_at_olist.base import views


app_name = 'base'
urlpatterns = [
    path('authors', views.authors, name='authors'),
    path('books/create', views.book_creation, name='book_creation'),
]
