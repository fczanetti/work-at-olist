from django.urls import path
from work_at_olist.base import views


app_name = 'base'
urlpatterns = [
    path('books', views.books_list, name='books_list'),
    path('books/<int:id>', views.book_read, name='book_read'),
    path('books/create', views.book_creation, name='book_creation'),
    path('books/update/<int:id>', views.book_update, name='book_update'),
    path('books/delete/<int:id>', views.book_delete, name='book_delete'),
]
