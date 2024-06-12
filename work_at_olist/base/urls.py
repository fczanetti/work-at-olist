from django.urls import path
from work_at_olist.base import views


app_name = 'base'
urlpatterns = [
    path('authors', views.authors, name='authors'),
    path('books', views.books_read, name='books'),
    path('books/create', views.book_creation, name='book_creation'),
    path('books/update/<int:id>', views.book_update, name='book_update'),
]
