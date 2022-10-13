from rest_framework import serializers
from .models import AddBook, AddStudent

class AddBookSerializers(serializers.ModelSerializer):
    class Meta:
        model = AddBook
        fields = '__all__'

class AddStudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = AddStudent
        fields = '__all__'