from enum import auto
from tabnanny import verbose
from django.db import models
from AdminUser.models import MyBaseModel


class BookOrder(MyBaseModel):
    order_id = models.IntegerField()
    customer_id = models.IntegerField()
    order_date = models.DateTimeField(auto_now=True)
    address = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100, blank=True)
    phone_no = models.IntegerField()
    payment_method = models.CharField(max_length=100)
    order_total = models.IntegerField()

    class Meta:
        verbose_name = 'Book Orders'
        verbose_name_plural = 'Book Order'


class Customer(MyBaseModel):
    customer_id = models.IntegerField()
    email = models.CharField(max_length=100, blank=True)
    full_name = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    contact_no = models.IntegerField()
    password = models.IntegerField()
    register_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Customers'
        verbose_name_plural = 'Customer'

class BookReview(MyBaseModel):
    review_id = models.IntegerField()
    book_id = models.IntegerField()
    rating = models.CharField(max_length=50, blank=True)
    headline = models.CharField(max_length=50)
    comments = models.CharField(max_length=100)
    review_time = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Book Reviews'
        verbose_name_plural = 'Book Review'


class OrderDetail(MyBaseModel):
    order_id = models.IntegerField()
    book_id = models.IntegerField()
    quantity = models.CharField(max_length=100,blank=True)
    sub_total = models.IntegerField()

    class Meta:
        verbose_name = 'Order Details'
        verbose_name_plural = 'Order Detail'    


class UserProfile(MyBaseModel):
    user_name = models.CharField(max_length=100, blank=True)
    password = models.IntegerField()
    signature = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=50,blank=True)


class OnlineBook(MyBaseModel):
    book_name = models.CharField(max_length=100, blank=True)
    book_price = models.IntegerField()
    book_witer = models.CharField(max_length=100, blank=True)
    author_write_year = models.IntegerField()
    publish_date = models.DateTimeField(auto_now_add=True)
