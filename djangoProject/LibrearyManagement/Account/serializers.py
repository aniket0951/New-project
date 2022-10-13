from rest_framework import serializers
from .models import BookRegister,BookLogin, BookSearch,LogoutBook


class BookRegisterSerializers(serializers.ModelSerializer):
    class Meta:
        model = BookRegister
        fields = '__all__'


class BookLoginSerializers(serializers.ModelSerializer):
    class Meta:
        model = BookLogin
        fields = '__all__'


class BookSearchSerializers(serializers.ModelSerializer):
    class Meta:
        model = BookSearch
        fields = '__all__'


class LogoutBookSerializers(serializers.ModelSerializer):
    class Meta:
        model = LogoutBook
        fields = '__all__'