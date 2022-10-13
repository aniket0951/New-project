from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BookRegister,BookLogin,BookSearch,LogoutBook
from .serializers import BookRegisterSerializers,BookLoginSerializers,BookSearchSerializers,LogoutBookSerializers


@api_view(['POST'])
def book_register(request):
    full_name = request.data.get('full_name')
    book_name = request.data.get('book_name')
    standard = request.data.get('standard')
    division = request.data.get('division')
    book_writer = request.data.get('book_writer')
    address1 = request.data.get('address1')
    address2 = request.data.get('address2')

    if full_name and book_name:
        res = BookRegister.objects.create(full_name=full_name,book_name=book_name,
                        standard=standard,division=division,book_writer=book_writer,
                        address1=address1, address2=address2)
        serializers = BookRegisterSerializers(res)
        return Response(serializers.data)
    else:
        return Response('Please no book register !')

@api_view(['GET'])
def book_register_(request):
    ans = BookRegister.objects.all()
    data = BookRegisterSerializers(ans, many=True).data
    return Response(data)

@api_view(['POST'])
def book_login(request):
    user_name = request.data.get('user_name')
    password = request.data.get('password')
    email = request.data.get('email')

    if user_name:
        res = BookLogin.objects.create(user_name=user_name,password=password,email=email)
        serializers = BookLoginSerializers(res)
        return Response(serializers.data)
    else:
        return Response('No login !')

@api_view(['GET'])
def book_login_(request):
    ans = BookLogin.objects.all()
    data = BookLoginSerializers(ans, many=True).data
    return Response(data)


@api_view(['POST'])
def search_book(request):
    book_title = request.data.get('book_title')
    writer_name = request.data.get('writer_name')
    subject_name = request.data.get('subject_name')
    publish_date = request.data.get('publish_date')

    if book_title and writer_name:
        res = BookSearch.objects.create(book_title=book_title,writer_name=writer_name,
                            subject_name=subject_name,publish_date=publish_date)
        serializers = BookSearchSerializers(res)
        return Response(serializers.data)
    else:
        return Response('No search book !')

@api_view(['GET'])
def book_search_ge(request):
    ans = BookSearch.objects.all()
    data = BookSearchSerializers(ans, many=True).data
    return Response(data)

@api_view(['DELETE'])
def search_book_del(request):
    id = BookSearch.objects.filter(
    id=request.data.get('id')).delete()
    return Response('id delete sucessfull')

@api_view(['POST'])
def book_logout(request):
    email = request.data.get('email')
    password = request.data.get('password')

    if email:
        res = LogoutBook.objects.create(email=email,password=password)
        serializers = LogoutBookSerializers(res)
        return Response(serializers.data)
    else:
        return Response ('please no logout !')

@api_view(['GET'])
def logout_(request):
    ans = LogoutBook.objects.all()
    data = LogoutBookSerializers(ans, many=True).data
    return Response(data)
