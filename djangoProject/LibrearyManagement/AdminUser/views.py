from django.shortcuts import render
from .models import AddBook, AddStudent
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import AddBookSerializers, AddStudentSerializers


# Create your views here.
@api_view(['POST'])
def book_add(request):
    book_name = request.data.get('book_name')
    book_writer = request.data.get('book_writer')
    no_book = request.data.get('no_book')
    book_type = request.data.get('book_type')
    book_publish_year = request.data.get('book_publish_year')

    if book_name:
        res = AddBook.objects.create(book_name=book_name,book_writer=book_writer,no_book=no_book,
                                        book_type=book_type,book_publish_year=book_publish_year)
        serializers = AddBookSerializers(res)
        return Response(serializers.data)
    else:
        return Response('Please no add book !')

@api_view(['GET'])
def book_add_(request):
    ans = AddBook.objects.all()
    data = AddBookSerializers(ans, many=True).data
    return Response(data)

@api_view(['DELETE'])
def add_book_del(request):
    id = AddBook.objects.filter(id=request.data.get('id')).delete()
    return Response('add book id successfull')

@api_view(['POST'])
def stud_add(request):
    stud_name = request.data.get('stud_name')
    address = request.data.get('address')
    phone_no = request.data.get('phone_no')
    signature = request.data.get('signature')

    if stud_name:
        res = AddStudent.objects.create(stud_name=stud_name,address=address,phone_no=phone_no,signature=signature)
        serializers = AddStudentSerializers(res)
        return Response(serializers.data)
    else:
        return Response('Please no student add !')

@api_view(['GET'])
def add_libreary(request):
    ans = AddStudent.objects.all()
    data = AddStudentSerializers(ans, many=True).data
    return Response(data)