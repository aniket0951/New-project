from django.contrib import admin
from .models import BookRegister,BookLogin,BookSearch

# Register your models here.

class BookRegisterAdmin(admin.ModelAdmin):
    list_display = ('full_name','book_name','standard','division','book_writer','address1','address2')
    list_filter = ('full_name', 'book_writer')

class BookLoginAdmin(admin.ModelAdmin):
    list_display = ('user_name','password','email')
    list_filter = ('user_name',)


class BookSearchAdmin(admin.ModelAdmin):
    list_display = ('book_title','writer_name','subject_name','publish_date')

admin.site.register(BookRegister,BookRegisterAdmin)
admin.site.register(BookLogin,BookLoginAdmin)
admin.site.register(BookSearch,BookSearchAdmin)