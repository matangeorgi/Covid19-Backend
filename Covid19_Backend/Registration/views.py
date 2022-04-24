
from datetime import datetime
from urllib.request import Request
from urllib.robotparser import RequestRate
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Registration.models import CitizenDetails
from Registration.serializers import CitizenSerializer
from Registration.middleware import checkInput
import re
import xlwt

citizens = CitizenDetails.objects.all()

# POST request to send data for registration.
@api_view(['POST'])
def addData(request):
    JsonResponse.status_code = 200
    citizen_data=JSONParser().parse(request)
    error = checkInput(citizen_data)

    if error != '':
        JsonResponse.status_code = 400
        return JsonResponse({'Error':error})

    citizen_serializer=CitizenSerializer(data=citizen_data)
    if citizen_serializer.is_valid():
        citizen_serializer.save()
        return JsonResponse({},safe=False)
    
    JsonResponse.status_code = 400
    return JsonResponse({},safe=False)


# This function will download the last data requested
@api_view(['GET'])
def ExportExcel(request):
    global citizens
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Summary.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Summary')
    row_num = 0
    
    cols =[
    'First name',
    'Last name',
    'Date of birth',
    'Address',
    'City',
    'Zip code',
    'Land Line',
    'Cellular Phone',
    'infected',
    'Conditions']

    for col_num in range(len(cols)):
        ws.write(row_num,col_num,cols[col_num])

    rows = citizens.values_list(
        'CitizenFirstName',
        'CitizenLastName',
        'CitizenDOB',
        'CitizenAddress',
        'CitizenCity',
        'CitizenZipCode',
        'CitizenCellular',
        'CitizenLandLine',
        'CitizenInfected',
        'CitizenConditions'
    )

    for row in rows:
        row_num +=1
        for col_num in range(len(row)):
            ws.write(row_num,col_num,str(row[col_num]))

    wb.save(response)
    return response


# GET request for the load of summary page.
@api_view(['GET'])
def getData(request):
    global citizens
    JsonResponse.status_code = 200
    citizens = CitizenDetails.objects.all()
    citizens_serializer = CitizenSerializer(citizens,many=True)
    return JsonResponse(citizens_serializer.data, safe=False)

# GET Request to get filtered data for the summary page.
@api_view(['GET'])
def getDataFilter(request):
    global citizens
    JsonResponse.status_code = 200
    citizens = CitizenDetails.objects.all()
    data = request.GET

    if data.get('city'):
        citizens = citizens.filter(CitizenCity=data.get('city'))
    
    if data.get('first') and data.get('second'):
        pat = re.compile(r"\d{4}-\d{2}-\d{2}")

        if re.fullmatch(pat,data.get('first')) and re.fullmatch(pat,data.get('second')):
            citizens = citizens.filter(CitizenDOB__range=[data.get('first'), data.get('second')])
        else:
            JsonResponse.status_code = 400
            return JsonResponse({'Error':"The dates are not in the right format."}, safe=False)


    citizens_serializer = CitizenSerializer(citizens,many=True)
    return JsonResponse(citizens_serializer.data, safe=False)
    