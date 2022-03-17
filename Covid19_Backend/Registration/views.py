from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Registration.models import CitizenDetails
from Registration.serializers import CitizenSerializer

# Create your views here.

@api_view(['GET'])
def getData(request):
    citizens = CitizenDetails.objects.all()
    citizens_serializer = CitizenSerializer(citizens,many=True)
    return JsonResponse(citizens_serializer.data, safe=False)