from django.urls import path
from .views import book_order, order_book_,customer_info,customer_info_,book_review,book_review_ge,review,order_detail,order_detail_ge,user_profile,profile_,profile_del,online_book,book_online,book_

urlpatterns = [
    path('book_order',book_order),
    path('order_book_',order_book_),
    path('customer_info',customer_info),
    path('customer_info_',customer_info_),
    path('book_review',book_review),
    path('book_review_ge',book_review_ge),
    path('review',review),
    path('order_detail',order_detail),
    path('order_detail_ge',order_detail_ge),
    path('user_profile',user_profile),
    path('profile_',profile_),
    path('profile_del',profile_del),
    path('online_book',online_book),
    path('book_online',book_online),
    path('book_',book_),

]