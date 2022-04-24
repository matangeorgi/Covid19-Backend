from email import message
from django.test import TestCase
from django.db import models
from datetime import datetime

def checkInput(data):
    message = ""
    if data['CitizenFirstName'] == "":
       message = "First name field is empty."

    elif data['CitizenLastName'] == "":
       message = "Last name field is empty."

    elif data['CitizenAddress'] == "":
       message = "Address field is empty."

    elif data['CitizenCity'] == "":
       message = "City field is empty."

    elif not data['CitizenZipCode'].strip().isdigit():
        message = "The Zip Code must contain only digits."

    elif not data['CitizenLandLine'].strip().isdigit():
       message = "The Land line must contain only digits."

    elif not data['CitizenCellular'].strip().isdigit():
        message = "The Cellular must contain only digits."

    elif data['CitizenDOB'] == "": 
        message = "Date of birth field is empty." 
    
    else:

        now = datetime.now()
        if now < datetime.strptime(data['CitizenDOB'] ,"%Y-%m-%d"):
            message = "The date is not valid" 

        newDate = data['CitizenDOB'].split('-')
        if int(newDate[1]) > 12 or int (newDate[2]) > 31:
            message = "The date is not valid" 
        
        
    return message
