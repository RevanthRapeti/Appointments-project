from .models import Appointment
from .serializers import doctor_serializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404


# Create your views here.

@api_view(['POST'])
def booking_view(request):
    if request.method == 'POST':
        item = Appointment.objects.all()
        items_list = doctor_serializer(item, many=True)
        return Response(items_list.data, status=status.HTTP_200_OK)
    else:
        app = doctor_serializer(data=request.data)
        app.is_valid(raise_exception=True)
        app.save()
        return Response(app.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def bookings_list_view(request, pk):
    booking = get_object_or_404(Appointment, id=pk)
    if request.method == 'GET':
        items = doctor_serializer(booking)
        return Response(items.data, status=status.HTTP_200_OK)

