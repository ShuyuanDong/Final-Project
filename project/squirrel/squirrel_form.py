from django import forms
from django.core.exceptions import ValidationError

class SquirrelForm(forms.Form):
    Longitude = forms.FloatField(label='longitude', error_messages={"required": "This field cannot be empty!"})
    Latitude = forms.FloatField(label="latitude", error_messages={"required": "This field cannot be empty!"})
    Unique_Squirrel_ID = forms.CharField(label="Unique_Squirrel_ID", error_messages={"required": "This field cannot be empty!"})
    Shift = forms.CharField(label="Shift", error_messages={"required": "This field cannot be empty and can only be 'AM' or 'PM'"})
    Date = forms.CharField(min_length=8, max_length = 8, label = "Date", error_messages={"min_length":"Date length must be 8", "max_length":"Date length must be 8", "required": "This field cannot be empty!"})
    Age = forms.CharField(label="Age", error_messages={"required": "This field cannot be empty and can only be 'Adult' or 'Juvenile'"})


