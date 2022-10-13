from tabnanny import verbose
from django.db import models
from AdminUser.models import MyBaseModel


class LibrearyCard(MyBaseModel):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, blank=True)
    standard = models.IntegerField()
    division = models.CharField(max_length=100, blank=True)
    sr_no = models.IntegerField()
    phone_no = models.IntegerField()
    
    class Meta:
        verbose_name = 'Libreary cards'
        verbose_name_plural = 'Libreary Card'


class BookAvaliable(MyBaseModel):
    first_year = models.IntegerField()
    second_year = models.IntegerField()
    third_year = models.IntegerField()
    MPSC = models.IntegerField()
    UPS = models.IntegerField()
    god = models.IntegerField()
    good_thought = models.IntegerField()
    spoken_english = models.IntegerField()

    class Meta:
        verbose_name = 'Book avaliables'
        verbose_name_plural = 'Book Avaliable'

class StudentForm(MyBaseModel):
    name = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100)
    phone_no = models.IntegerField()

    class Meta:
        verbose_name = 'Student Forms'
        verbose_name_plural = 'Student Form'
