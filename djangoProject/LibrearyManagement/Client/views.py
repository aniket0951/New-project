from re import sub
from django.shortcuts import render
from .models import AuthorInform,IssueBook
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import  IssueBookSerializers


@api_view(['POST'])
def author_inform(request):
    name = request.data.get('name')
    address1 = request.data.get('address1')
    address2 = request.data.get('address2')
    phone_no = request.data.get('phone_no')
    book_no = request.data.get('book_no')
    book_publish = request.data.get('book_publish')
    city = request.data.get('city')
    state = request.data.get('state')
    country = request.data.get('country')
    email = request.data.get('email')

    if name and address1:
        res = AuthorInform.objects.create(name=name,address1=address1,address2=address2,
                        phone_no=phone_no,book_no=book_no,book_publish=book_publish,city=city,
                        state=state,country=country,email=email)
        serializers = AuthorInformSerializers(res)
        return Response(serializers.data)
    else:
        return Response('please no match informations !')

@api_view(['GET'])
def author_(request):
    ans = AuthorInform.objects.all()
    data = AuthorInformSerializers(ans, many=True).data
    return Response(data)

@api_view(['DELETE'])
def author_inform_del(request):
    id = AuthorInform.objects.filter(id=request.data.get('id')).delete()
    return Response('Yes successfull')


@api_view(['POST'])
def issue_book(request):
    subject = request.data.get('subject')
    chapter = request.data.get('chapter')

    if subject:
        ans = IssueBook.objects.create(subject=subject,chapter=chapter)
        serializers= IssueBookSerializers(ans)
        return Response(serializers.data)
    else:
        return Response('no dout book !')


@api_view(['GET'])
def issue_book_(request):
    res = IssueBook.objects.all()
    data = IssueBookSerializers(res, many=True).data
    return Response(data)