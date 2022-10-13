from django.urls import path
from .views import libreary_card, libreary_,book_Avaliable, available_book_,student_inform,student_,s_inform

urlpatterns = [
    path('libreary_card',libreary_card),
    path('libreary_',libreary_),
    path('book_Avaliable',book_Avaliable),
    path('available_book_',available_book_),
    path('student_inform',student_inform),
    path('student_',student_),
    path('s_inform',s_inform),

]
