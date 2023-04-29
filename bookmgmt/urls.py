from django.urls import path
from .views import add_book, book_list, edit_book, delete_book, book_search,home

urlpatterns = [
    path('', home, name='home'),
    path('add_book/', add_book, name='add_book'),
    path('book_list/', book_list, name='book_list'),
    path('edit_book/<int:book_id>/', edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', delete_book, name='delete_book'),
    path('book_search/', book_search, name='book_search'),
]
