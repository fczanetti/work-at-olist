from django.urls import path
from work_at_olist.base import views


app_name = 'base'
urlpatterns = [
    path('books/delete/<int:id>', views.book_delete, name='book_delete'),
]
