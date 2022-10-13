from django.contrib import admin
from .models import AddBook, AddStudent

# Register your models here.

class AddBookAdmin(admin.ModelAdmin):
    list_display = ('book_name','book_writer','no_book','book_type','book_publish_year')
    list_filter = ('book_name','book_type')


class AddStudentAdmin(admin.ModelAdmin):
    list_display = ('stud_name','address','phone_no','signature')
    list_filter = ('stud_name','phone_no')

admin.site.register(AddBook,AddBookAdmin)
admin.site.register(AddStudent,AddStudentAdmin)