from inspect import signature
from tabnanny import verbose
from venv import create
from django.db import models

# Create your models here.

class MyBaseModel(models.Model):
    id = models.AutoField(primary_key = True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)


class AddBook(MyBaseModel):
    book_name = models.CharField(max_length=100, blank=True)
    book_writer = models.CharField(max_length=100, blank=True)
    no_book = models.IntegerField()
    book_type = models.CharField(max_length=100)
    book_publish_year = models.IntegerField()

    class Meta:
        verbose_name = 'Add books'
        verbose_name_plural = 'Add Book'


class AddStudent(MyBaseModel):
    stud_name = models.CharField(max_length=100,blank=True)
    address = models.CharField(max_length=100)
    phone_no = models.IntegerField()
    signature = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Add Students'
        verbose_name_plural = 'Add Student'