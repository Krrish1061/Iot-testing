from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import SensorValue, MachineDescription
from .serializers import SensorValueSerializer
from rest_framework.decorators import authentication_classes
from .auth import APIKeyAuthentication
from .utilis import set_data


def home(request):
    return render(request, "index.html")


# Create your views here.
@api_view(["GET", "POST"])
@authentication_classes([APIKeyAuthentication])
def sensor_value_list(request):
    if request.method == "GET":
        queryset = SensorValue.objects.all()
        serializer = SensorValueSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        # content = request.body.decode("utf-8")
        # data = set_data(content)
        # # api_key=Zp8OzUK5VXC2IncqDw5GTbDSZCbLVWSR&field1=20.3&field2=45.8&field3=1&board=1&gpio=36&cboard=3
        print(request.POST)
        serializer = SensorValueSerializer(data=request.POST)
        serializer.is_valid(raise_exception=True)
        machine_id = MachineDescription.objects.get(pk=request.POST.get("cboard"))
        serializer.save(machine_id=machine_id)
        return Response(serializer.data, status=status.HTTP_200_OK)
        # return Response(serializer.data, status=status.HTTP_200_OK)
