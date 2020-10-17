from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):
    Latitude  = models.FloatField()
    Longitude = models.FloatField()
    Date = models.CharField(max_length = 100)
    Unique_Squirrel_ID = models.CharField(max_length = 100)
    
    PM = 'PM'
    AM = 'AM'
    Shift_Choices = [
            (PM, _('PM')),
            (AM, _('AM'))
            ]
    Shift = models.CharField(choices=Shift_Choices, max_length = 100)
    
    Adult = 'Adult'
    Juvenile = 'Juvenile'
    Age_Choices = [
            (Adult, _('Adult')),
            (Juvenile, _('Juvenile'))
            ]
    Age = models.CharField(choices=Age_Choices, blank=True, null=True, max_length = 100)
    Gray = 'Gray'
    Black = 'Black'
    Cinnamon = 'Cinnamon'
    Primary_Fur_Color_Choices = [
            (Gray, _('Gray')),
            (Black, _('Black')),
            (Cinnamon, _('Cinnamon'))
            ]
    Primary_Fur_Color = models.CharField(choices=Primary_Fur_Color_Choices, blank=True, null=True, max_length = 100)
    Ground_Plane = 'Ground Plane'
    Above_Ground = 'Above Ground'
    Location_Choices = [
            (Ground_Plane, _('Ground Plane')),
            (Above_Ground, _('Above Ground'))
            ]
    Location = models.CharField(choices=Location_Choices, blank=True, null=True, max_length = 100)
    Specific_Location = models.CharField(blank=True, null=True, max_length = 100)
    Running = models.BooleanField(blank=True, null=True)
    Chasing = models.BooleanField(blank=True, null=True)
    Climbing = models.BooleanField(blank=True, null=True)
    Eating = models.BooleanField(blank=True, null=True)
    Foraging = models.BooleanField(blank=True, null=True)
    Other_Activities = models.CharField(blank=True, null=True, max_length = 100)
    Kuks = models.BooleanField(blank=True, null=True)
    Quaas = models.BooleanField(blank=True, null=True)
    Moans = models.BooleanField(blank=True, null=True)
    Tail_flags = models.BooleanField(blank=True, null=True)
    Tail_twitches = models.BooleanField(blank=True, null=True)
    Approaches = models.BooleanField(blank=True, null=True)
    Indifferent = models.BooleanField(blank=True, null=True)
    Runs_from = models.BooleanField(blank=True, null=True)

