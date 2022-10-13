from rest_framework import serializers
from .models import BookOrder, Customer,BookReview,OrderDetail,UserProfile,OnlineBook

class BookOrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = BookOrder
        fields = '__all__'


class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class BookReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = BookReview
        fields = '__all__'


class OrderDetailSerializrs(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = '__all__'


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class OnlineBookSerializers(serializers.ModelSerializer):
    class Meta:
        model = OnlineBook
        fields = '__all__'
               