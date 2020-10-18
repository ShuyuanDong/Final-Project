from django import forms
from django.core.exceptions import ValidationError

class EmpForm(forms.Form):
    Longitude = forms.FloatField(label='longitude', error_messages={"required": "This field cannot be empty!"})
    Latitude = forms.FloatField(label="latitude", error_messages={"required": "This field cannot be empty!"})
    Unique_Squirrel_ID = forms.CharField(label="Unique_Squirrel_ID", error_messages={"required": "This field cannot be empty!"})
    Shift = forms.CharField(label="Shift", error_messages={"required": "This field cannot be empty and can only be 'AM' or 'PM'"})
    Date = forms.CharField(min_length=8, max_length = 8, label = "Date", error_messages={"min_length":"Date length must be 8", "max_length":"Date length must be 8", "required": "This field cannot be empty!"})
    Age = forms.CharField(label="Age", error_messages={"required": "This field cannot be empty and can only be 'Adult' or 'Juvenile'"})
    Primary_Fur_Color = forms.CharField(label="Primary_Fur_Color", required=False)
    Location = forms.CharField(label="Location", required=False)
    Specific_Location = forms.CharField(label="Specific_Location", required=False)
    Running = forms.BooleanField(label="Running", required=False)
    Chasing = forms.BooleanField(label="Chasing", required=False)
    Climbing = forms.BooleanField(label="Climbing", required=False)
    Eating = forms.BooleanField(label="Eating", required=False)
    Foraging = forms.BooleanField(label="Foraging", required=False)
    Other_Activities = forms.CharField(label="Other_Activities", required=False)
    Kuks = forms.BooleanField(label="Kuks", required=False)
    Quaas = forms.BooleanField(label="Quaas", required=False)
    Moans = forms.BooleanField(label="Moans", required=False)
    Tail_flags = forms.BooleanField(label="Tail_flags", required=False)
    Tail_twiches = forms.BooleanField(label="Tail_twiches", required=False)
    Approaches = forms.BooleanField(label="Approaches", required=False)
    Indifferent = forms.BooleanField(label="Indifferent", required=False)
    Runs_from = forms.BooleanField(label="Runs_from", required=False)



    #running = forms.BooleanField(label="running", required=False)


