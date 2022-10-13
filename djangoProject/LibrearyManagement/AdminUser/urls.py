from django.urls import path
from .views import book_add,book_add_, add_book_del,stud_add,add_libreary

urlpatterns = [
    path('book_add', book_add),
    path('book_add_',book_add_),
    path('add_book_del',add_book_del),
    path('stud_add',stud_add),
    path('add_libreary',add_libreary),

]