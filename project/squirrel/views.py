from django.shortcuts import render, redirect
from django.http import HttpResponse
from squirrel.models import Squirrel
from django.template import Context, loader
from squirrel.my_form import EmpForm
from squirrel.squirrel_form import SquirrelForm
from django.views.decorators.csrf import csrf_exempt
import re

def sightings(request):
    squirrels_list = Squirrel.objects.all()
    template = loader.get_template('squirrels/sightings.html')
    context = {
        'squirrels_list': squirrels_list,
    }
    return render(request, 'squirrels/sightings.html', context)
    #return HttpResponse(template.render(context))

def detail(request, sid):
    squirrel = Squirrel.objects.get(Unique_Squirrel_ID = sid)
    context = {
            'squirrel': squirrel,
            }

    return render(request, 'squirrels/detail.html', context)

@csrf_exempt
def add(request):
    if request.method == "GET":
        form = EmpForm()
        return render(request, "squirrels/add.html", {"form": form})
    else:
        form = EmpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            squirrel = Squirrel.objects.filter(Unique_Squirrel_ID=data['Unique_Squirrel_ID']).first()
            if squirrel is not None:
                return HttpResponse('The Squirrel ID is dulplicated!')
            Squirrel.objects.create(**data)
            return HttpResponse(
                    'The squirrel is successfully uploaded!'
                )
                # return render(request, "add.html", {"form": form})
        else:
            clean_errors = form.errors.get("__all__")
            return render(request, "squirrels/add.html", {"form": form, "clean_errors":clean_errors})

def map(request):
    sightings = Squirrel.objects.all()[:100]
    context = {
            'sightings': sightings
    }
    return render(request,'squirrels/map.html',context)

def stats(request):
    sightings_total = Squirrel.objects.count()
    sightings_black = Squirrel.objects.filter(Primary_Fur_Color = 'Black').count()
    chasing_true = Squirrel.objects.filter(Chasing=True).count()
    sightings_grey = Squirrel.objects.filter(Primary_Fur_Color = 'Gray').count()
    eating_true = Squirrel.objects.filter(Eating=True).count()
    context = {
            'sightings_total':sightings_total,
            'sightings_grey':sightings_grey,
            'sightings_black': sightings_black,
            'chasing_true':chasing_true,
            'eating_true':eating_true,
            }
    return render(request,'squirrels/stats.html',context)


def update(request,uid):
    squirrel=Squirrel.objects.get(Unique_Squirrel_ID=uid)
    context = {'Latitude':squirrel.Latitude, 'Longitude':squirrel.Longitude,
                'Unique_Squirrel_ID':squirrel.Unique_Squirrel_ID, 
                'Shift':squirrel.Shift, 'Date':squirrel.Date, 'Age':squirrel.Age}
    if request.method == "GET":
        form = SquirrelForm(context)
        return render(request, "squirrels/update.html", {"form": form})
    else:
        form = SquirrelForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            squirrel.Unique_Squirrel_ID = cleaned_data.get('Unique_Squirrel_ID')
            squirrel.Date = cleaned_data.get('Date')
            squirrel.Longitude = cleaned_data.get('Longitude')
            squirrel.Latitude = cleaned_data.get('Latitude')
            squirrel.Shift = cleaned_data.get('Shift')
            squirrel.Age = cleaned_data.get('Age')
            squirrel.save()
            return redirect('sightings')
        else:
            form = SquirrelForm(context)
            clean_errors = form.errors.get("__all__")
            return render(request, "squirrels/update.html", {"form": form, "clean_errors":clean_errors})
    




