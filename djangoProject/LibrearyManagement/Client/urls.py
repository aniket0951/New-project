from django.urls import path
from .views import author_inform, author_,author_inform_del,issue_book,issue_book_

urlpatterns = [
    path('author_inform',author_inform),
    path('author_',author_),
    path('author_inform_del',author_inform_del),
    path('issue_book',issue_book),
    path('issue_book_',issue_book_),

]