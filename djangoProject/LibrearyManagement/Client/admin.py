from django.contrib import admin
from .models import AuthorInform,IssueBook

# Register your models here.

class AuthorInformAdmin(admin.ModelAdmin):
    list_display = ('name','address1','address2','phone_no','book_no','book_publish',
                    'city','state','country','email')


class IssueBookAdmin(admin.ModelAdmin):
    list_display = ('subject','chapter')



admin.site.register(AuthorInform,AuthorInformAdmin)
admin.site.register(IssueBook,IssueBookAdmin)