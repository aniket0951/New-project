from django.urls import path
from .views import book_register,book_register_,book_login,book_login_,search_book,book_search_ge,search_book_del,book_logout,logout_


urlpatterns = [
    path('book_register',book_register),
    path('book_register_',book_register_),
    path('book_login',book_login),
    path('book_login_',book_login_),
    path('search_book',search_book),
    path('book_search_ge',book_search_ge),
    path('search_book_del',search_book_del),
    path('book_logout',book_logout),
    path('logout_',logout_),

]