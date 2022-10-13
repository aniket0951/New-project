from django.contrib import admin
from .models import BookOrder,Customer,BookReview,OrderDetail


class BookOrderAdmin(admin.ModelAdmin):
    list_display = ('order_id','customer_id','order_date','address','name','phone_no',
                                        'payment_method','order_total')


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_id','email','full_name','address','city','country','contact_no',
                        'password','register_date')


class BookReviewAdmin(admin.ModelAdmin):
    list_display = ('review_id','book_id','rating','headline','comments','review_time')


class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ('order_id','book_id','quantity','sub_total')

admin.site.register(BookOrder,BookOrderAdmin)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(BookReview,BookReviewAdmin)
admin.site.register(OrderDetail,OrderDetailAdmin)