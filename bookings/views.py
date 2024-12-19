from django.shortcuts import render, redirect

from .forms import BookingForm

from .models import Coupon, Event

from django.contrib import messages

from .forms import EventForm



def add_event(request):

  if request.method == "POST":

    form = EventForm(request.POST)

    if form.is_valid():

      form.save()

      messages.success(request, "Event added successfully!")

      return redirect('/book') 

  else:

    form = EventForm()

  return render(request, "add_event.html", {"form": form})





def book_event(request):

  form = BookingForm()

  error = None

  total_price = None

  discount = None

  ticket_price = None

  discount_percentage = 0



  if request.method == "POST":

    form = BookingForm(request.POST)

    if form.is_valid():

      event = form.cleaned_data['event']

      number_of_tickets = form.cleaned_data['number_of_tickets']

      coupon_code = form.cleaned_data['coupon_code']



      # Get the selected event and ticket price

      ticket_price = event.price_per_ticket

      total_price = ticket_price * number_of_tickets



      # Check if coupon code is provided

      if coupon_code:

        try:

          coupon = Coupon.objects.get(code=coupon_code)

          discount_percentage = coupon.discount_percentage

          discount = (discount_percentage / 100) * total_price

          total_price -= discount

        except Coupon.DoesNotExist:

          error = "Invalid coupon code"



  return render(request, 'book_event.html', {

    'form': form,

    'error': error,

    'total_price': total_price,

    'discount': discount,

    'ticket_price': ticket_price,

    'discount_percentage': discount_percentage,

  })







from rest_framework.decorators import api_view

from rest_framework.response import Response

from rest_framework import status

from .models import Coupon

from .serializers import CouponSerializer



@api_view(['POST'])

def create_coupon(request):

  """API to create a new coupon."""

  serializer = CouponSerializer(data=request.data)

  if serializer.is_valid():

    serializer.save()

    return Response(serializer.data, status=status.HTTP_201_CREATED)

  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])

def manage_coupon(request, code=None):

  """

  API to handle coupon operations:

  - GET without code: Retrieve all coupons.

  - GET with code: Retrieve a specific coupon.

  - PUT with code: Update a specific coupon.

  - DELETE with code: Delete a specific coupon.

  """

  if request.method == 'GET':

    if code:

      # Retrieve a specific coupon

      try:

        coupon = Coupon.objects.get(code=code)

      except Coupon.DoesNotExist:

        return Response({'error': 'Invalid coupon code.'}, status=status.HTTP_404_NOT_FOUND)

      serializer = CouponSerializer(coupon)

      return Response(serializer.data, status=status.HTTP_200_OK)

    else:

      # Retrieve all coupons

      coupons = Coupon.objects.all()

      serializer = CouponSerializer(coupons, many=True)

      return Response(serializer.data, status=status.HTTP_200_OK)



  try:

    coupon = Coupon.objects.get(code=code)

  except Coupon.DoesNotExist:

    return Response({'error': 'Invalid coupon code.'}, status=status.HTTP_404_NOT_FOUND)



  if request.method == 'PUT':

    # Update coupon

    serializer = CouponSerializer(coupon, data=request.data)

    if serializer.is_valid():

      serializer.save()

      return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



  elif request.method == 'DELETE':

    # Delete coupon

    coupon.delete()

    return Response({'message': 'Coupon deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)






















