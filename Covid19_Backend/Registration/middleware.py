from asyncio.windows_events import NULL
from email import message
from django.test import TestCase
from django.db import models
from datetime import datetime


def checkInput(data):
    print(len(data['CitizenLandLine']))
    message = ""
    if data['CitizenFirstName'] == "":
       message = "First name field is empty."

    elif data['CitizenLastName'] == "":
       message = "Last name field is empty."

    elif data['CitizenAddress'] == "":
       message = "Address field is empty."

    elif data['CitizenCity'] == "":
       message = "City field is empty."

    elif data['CitizenLandLine'] == "":
        message = "Land line field is empty."

    elif data['CitizenCellular'] == "":
       message = "Cellular field is empty."

    elif data['CitizenDOB'] == "": 
        message = "Date of birth field is empty." 

    elif not (data['CitizenZipCode'].strip().isdigit()):
        if data['CitizenZipCode'] != '':
            message = "The Zip Code must contain only digits."

    elif not data['CitizenLandLine'].strip().isdigit():
       message = "The Land line must contain only digits."
       print('here')

    elif not data['CitizenCellular'].strip().isdigit():
        message = "The Cellular must contain only digits."

    
    else:

        now = datetime.now()
        if now < datetime.strptime(data['CitizenDOB'] ,"%Y-%m-%d"):
            message = "The date is not valid" 

        newDate = data['CitizenDOB'].split('-')
        if int(newDate[1]) > 12 or int (newDate[2]) > 31:
            message = "The date is not valid" 
        
        
    return message
