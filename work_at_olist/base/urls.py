from django.urls import path
from work_at_olist.base import views


app_name = 'base'
urlpatterns = [
    path('books/<int:id>', views.book_read, name='book_read'),
    path('books/update/<int:id>', views.book_update, name='book_update'),
    path('books/delete/<int:id>', views.book_delete, name='book_delete'),
]
