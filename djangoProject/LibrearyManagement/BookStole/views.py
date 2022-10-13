from audioop import add
from turtle import up
from urllib import response
from django.shortcuts import render
from .models import LibrearyCard, BookAvaliable,StudentForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import LibrearyCardSerializers,BookAvaliableSerializers,StudentFormSerializers

# Create your views here.
@api_view(['POST'])
def libreary_card(request):
    name = request.data.get('name')
    address = request.data.get('address')
    standard = request.data.get('standard')
    division = request.data.get('division')
    sr_no = request.data.get('sr_no')
    phone_no = request.data.get('phone_no')

    if name and address:
        res = LibrearyCard.objects.create(name=name,address=address,standard=standard,
                            division=division,sr_no=sr_no,phone_no=phone_no)
        serializers = LibrearyCardSerializers(res)
        return Response(serializers.data)
    else:
        return Response('Please no card !')

@api_view(['GET'])
def libreary_(request):
    ans = LibrearyCard.objects.all()
    data = LibrearyCardSerializers(ans, many=True).data
    return Response(data)

@api_view(['POST'])
def book_Avaliable(request):
    first_year = request.data.get('first_year')
    second_year = request.data.get('second_year')
    third_year = request.data.get('third_year')
    MPSC = request.data.get('MPSC')
    UPS = request.data.get('UPS')
    god = request.data.get('god')
    good_thought = request.data.get('good_thought')
    spoken_english = request.data.get('spoken_english')

    if first_year and second_year:
        res = BookAvaliable.objects.create(first_year=first_year,second_year=second_year,
                        third_year=third_year,MPSC=MPSC,UPS=UPS,god=god,
                        good_thought=good_thought,spoken_english=spoken_english)
        serializers = BookAvaliableSerializers(res)
        return Response(serializers.data)
    else:
        return Response('Please no book avaliable !')

@api_view(['GET'])
def available_book_(request):
    ans = BookAvaliable.objects.all()
    data = BookAvaliableSerializers(ans, many=True).data
    return Response(data)


@api_view(['POST'])
def student_inform(request):
    name = request.data.get('name')
    address = request.data.get('address')
    phone_no = request.data.get('phone_no')

    if name:
        res = StudentForm.objects.create(name=name,address=address,phone_no=phone_no)
        serializers = StudentFormSerializers(res)
        return Response(serializers.data)
    else:
        return Response('no match information !')

@api_view(['GET'])
def student_(request):
    ans = StudentForm.objects.all()
    data = StudentFormSerializers(ans, many=True).data
    return Response(data)


@api_view(['DELETE'])
def s_inform(request):
    id = StudentForm.objects.filter(
    id=request.data.get('id')).delete()
    return Response('student id delete successfull')
