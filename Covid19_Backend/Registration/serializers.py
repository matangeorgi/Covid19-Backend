from dataclasses import fields
from rest_framework import serializers
from Registration.models import CitizenDetails

class CitizenSerializer(serializers.ModelSerializer):
    class Meta:
        model = CitizenDetails
        fields = ('CitizenId', 
        'CitizenFirstName',
        'CitizenLastName',
        'CitizenDOB',
        'CitizenAddress',
        'CitizenCity',
        'CitizenZipCode',
        'CitizenCellular',
        'CitizenLandLine',
        'CitizenInfected',
        'CitizenConditions')
