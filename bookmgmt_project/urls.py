from django.contrib import admin
from django.urls import path, include
from bookmgmt.views import add_book, edit_book, delete_book, book_search,home,book_list

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('book_list/', book_list, name='book_list'),
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:book_id>/', edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', delete_book, name='delete_book'),
    path('book_search/', book_search, name='book_search'),
]
