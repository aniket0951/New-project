from rest_framework import serializers
from .views import LibrearyCard, BookAvaliable,StudentForm

class LibrearyCardSerializers(serializers.ModelSerializer):
    class Meta:
        model = LibrearyCard
        fields = '__all__'


class BookAvaliableSerializers(serializers.ModelSerializer):
    class Meta:
        model = BookAvaliable
        fields = '__all__'

class StudentFormSerializers(serializers.ModelSerializer):
    class Meta:
        model = StudentForm
        fields = '__all__' 