from tabnanny import verbose
from django.db import models
from AdminUser.models import MyBaseModel

# Create your models here.

class AuthorInform(MyBaseModel):
    name = models.CharField(max_length=100)
    address1 = models.CharField(max_length=100, blank=True)
    address2 = models.CharField(max_length=100, blank=True)
    phone_no = models.IntegerField()
    book_no = models.IntegerField()
    book_publish = models.IntegerField()
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100,blank=True )

    class Meta:
        verbose_name = 'Author Informs'
        verbose_name_plural = 'Author Informations'


class IssueBook(MyBaseModel):
    subject = models.CharField(max_length=30, blank=True)
    chapter = models.IntegerField()

    class Meta:
        verbose_name = 'Issue Books'
        verbose_name_plural = 'Issue Book'