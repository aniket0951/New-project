from django.contrib import admin
from .models import LibrearyCard, BookAvaliable,StudentForm

# Register your models here.

class LibrearyCardAdmin(admin.ModelAdmin):
    list_display = ('name','address','standard','division','sr_no','phone_no')


class BookAvaliableAdmin(admin.ModelAdmin):
    list_display = ('first_year','second_year','third_year','MPSC','UPS','god','good_thought','spoken_english')


class StudentFormAdmin(admin.ModelAdmin):
    list_display = ('name','address','phone_no')

admin.site.register(LibrearyCard,LibrearyCardAdmin)
admin.site.register(BookAvaliable,BookAvaliableAdmin)
admin.site.register(StudentForm,StudentFormAdmin)