from tabnanny import verbose
from django.db import models
from AdminUser.models import MyBaseModel
# Create your models here.

class BookRegister(MyBaseModel):
    full_name = models.CharField(max_length=100, blank=True)
    book_name = models.CharField(max_length=100, blank=True)
    standard = models.IntegerField()
    division = models.CharField(max_length=100, blank=True)
    book_writer = models.CharField(max_length=50,blank=True)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)

    def __str__(self):
        return self.book_name

    class Meta:
        verbose_name = 'Book Registers'
        verbose_name_plural = 'Book Register'


class BookLogin(MyBaseModel):
    user_name = models.CharField(max_length=100)
    password = models.IntegerField()
    email = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Book Logins'
        verbose_name_plural = 'Book Login'

class BookSearch(MyBaseModel):
    book_title = models.CharField(max_length=100)
    writer_name = models.CharField(max_length=100, blank=True)
    subject_name = models.CharField(max_length=100, blank=True)
    publish_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Book Searchs'
        verbose_name_plural = 'Book Search'


class LogoutBook(MyBaseModel):
    email = models.CharField(max_length=100, blank=True)
    password = models.IntegerField()

    def __str__(self):
        self.email