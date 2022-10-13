from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BookOrder,Customer,BookReview,OrderDetail,UserProfile,OnlineBook
from .serializers import BookOrderSerializers,CustomerSerializers,BookReviewSerializers,OrderDetailSerializrs,UserProfileSerializers,OnlineBookSerializers

@api_view(['POST'])
def book_order(request):
    order_id = request.data.get('order_id')
    customer_id = request.data.get('customer_id')
    order_date = request.data.get('order_date')
    address = request.data.get('address')
    name = request.data.get('name')
    phone_no = request.data.get('phone_no')
    payment_method = request.data.get('payment_method')
    order_total = request.data.get('order_total')

    if order_id and customer_id:
        res = BookOrder.objects.create(order_id=order_id,customer_id=customer_id,order_date=order_date,
                        address=address,name=name,phone_no=phone_no,payment_method=payment_method,order_total=order_total)
        serializers = BookOrderSerializers(res)
        return Response(serializers.data)
    else:
        return Response('No book order !')

@api_view(['GET'])
def order_book_(request):
    ans = BookOrder.objects.all()
    data = BookOrderSerializers(ans, many=True).data
    return Response(data)

@api_view(['POST'])
def customer_info(request):
    customer_id = request.data.get('customer_id')
    email = request.data.get('email')
    full_name = request.data.get('full_name')
    address = request.data.get('address')
    city = request.data.get('city')
    country = request.data.get('country')
    contact_no = request.data.get('contact_no')
    password = request.data.get('password')
    register_date = request.data.get('register_date')

    if customer_id and email and full_name:
        res = Customer.objects.create(customer_id=customer_id,email=email,full_name=full_name,
                    address=address,city=city,country=country,contact_no=contact_no,
                    password=password,register_date=register_date)
        serializers = CustomerSerializers(res)
        return Response(serializers.data)
    else:
        return Response('inform no match !')

@api_view(['GET'])
def customer_info_(request):
    ans = Customer.objects.all()
    data = CustomerSerializers(ans, many=True).data
    return Response(data)


@api_view(['POST'])
def book_review(request):
    review_id = request.data.get('review_id')
    book_id = request.data.get('book_id')
    rating = request.data.get('rating')
    headline = request.data.get('headline')
    comments = request.data.get('comments')
    review_time = request.data.get('review_time')

    if review_id and book_id:
        res = BookReview.objects.create(review_id=review_id,book_id=book_id,rating=rating,headline=headline,
                                        review_time=review_time,comments=comments)
        serializers = BookReviewSerializers(res)
        return Response(serializers.data)
    else:
        return Response('No review book !')


@api_view(['GET'])
def book_review_ge(request):
    ans = BookReview.objects.all()
    data = BookReviewSerializers(ans, many=True).data
    return Response(data)

@api_view(['DELETE'])
def review(request):
    id = BookReview.objects.filter(
    id = request.data.get('id')
    ).delete()
    return Response('id book sucessfull')

@api_view(['POST'])
def order_detail(request):
    order_id = request.data.get('order_id')
    book_id = request.data.get('book_id')
    quantity = request.data.get('quantity')
    sub_total = request.data.get('sub_total')

    if sub_total and quantity:
        res = OrderDetail.objects.create(order_id=order_id,book_id=book_id,quantity=quantity,sub_total=sub_total)
        serializers = OrderDetailSerializrs(res)
        return Response(serializers.data)
    else:
        return Response('Please order check !')

@api_view(['GET'])
def order_detail_ge(request):
    ans = OrderDetail.objects.all()
    data = OrderDetailSerializrs(ans, many=True).data
    return Response(data)

@api_view(['POST'])
def user_profile(request):
    user_name = request.data.get('user_name')
    password = request.data.get('password')
    signature = request.data.get('signature')
    email = request.data.get('email')

    if email and signature:
        abc = UserProfile.objects.create(user_name=user_name,password=password,signature=signature,
                            email=email)
        serializers = UserProfileSerializers(abc)
        return Response(serializers.data)
    else:
        return Response('please no profile')

@api_view(['GET'])
def profile_(request):
    ans = UserProfile.objects.all()
    data = UserProfileSerializers(ans, many=True).data
    return Response(data)

@api_view(['DELETE'])
def profile_del(request):
    id = UserProfile.objects.filter(
    id=request.data.get('id')).delete()
    return Response('id delete succesfull ! ')

@api_view(['POST'])
def online_book(request):
    book_name = request.data.get('book_name')
    book_price = request.data.get('book_price')
    book_witer = request.data.get('book_witer')
    author_write_year = request.data.get('author_write_year')
    publish_date = request.data.get('publish_date')

    if book_name and book_price:
        res = OnlineBook.objects.create(book_name=book_name,book_price=book_price,
                    book_witer=book_witer,author_write_year=author_write_year,publish_date=publish_date)
        serializers = OnlineBookSerializers(res)
        return Response(serializers.data)
    else:
        return Response('please no book !')

@api_view(['GET'])
def book_online(request):
    ans = OnlineBook.objects.all()
    data = OnlineBookSerializers(ans, many=True).data
    return Response(data)


@api_view(['DELETE'])
def book_(request):
    id = OnlineBook.objects.filter(
        id = request.data.get('id')
    ).delete()
    return Response('id delete succesfull ! ')

