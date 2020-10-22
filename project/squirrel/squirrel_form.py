from django import forms
from django.core.exceptions import ValidationError
import re

class SquirrelForm(forms.Form):
    Longitude = forms.FloatField(label='longitude', error_messages={"required": "This field cannot be empty!"})
    Latitude = forms.FloatField(label="latitude", error_messages={"required": "This field cannot be empty!"})
    Unique_Squirrel_ID = forms.CharField(label="Unique_Squirrel_ID", error_messages={"required": "This field cannot be empty!"})
    Shift = forms.CharField(label="Shift", error_messages={"required": "This field cannot be empty and can only be 'AM' or 'PM'"})
    Date = forms.CharField(min_length=8, max_length = 8, label = "Date", error_messages={"min_length":"Date length must be 8", "max_length":"Date length must be 8", "required": "This field cannot be empty!"})
    Age = forms.CharField(label="Age", error_messages={"required": "This field cannot be empty and can only be 'Adult' or 'Juvenile'"})

    def clean(self):
        UID = self.cleaned_data.get('Unique_Squirrel_ID')
        if self._check(UID) is None:
            self.add_error('Unique_Squirrel_ID', ValidationError('Squirrel ID is invalid'))
        else:
            return self.cleaned_data

    def _check(self, UID):
        return re.match(r'(\d+[A-Z])-(PM|AM)-(\d{4})-(\d{2})', UID)

