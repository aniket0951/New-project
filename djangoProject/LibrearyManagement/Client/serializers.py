from rest_framework import serializers
from .models import AuthorInform, IssueBook

class AuthorInformSerializers(serializers.ModelSerializer):
    class Meta:
        model = AuthorInform
        fields = '__all__'

class IssueBookSerializers(serializers.ModelSerializer):
    class Meta:
        model = IssueBook
        fields = '__all__'