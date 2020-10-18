from django.shortcuts import render
from django.http import HttpResponse
from squirrel.models import Squirrel
from django.template import Context, loader
from squirrel.my_form import EmpForm
from django.views.decorators.csrf import csrf_exempt

def sightings(request):
    squirrels_list = Squirrel.objects.all()
    template = loader.get_template('squirrels/sightings.html')
    context = {
        'squirrels_list': squirrels_list,
    }
    return render(request, 'squirrels/sightings.html', context)
    #return HttpResponse(template.render(context))

def detail(request, sid):
    return HttpResponse(sid)

@csrf_exempt
def add(request):
    if request.method == "GET":
        form = EmpForm()
        return render(request, "squirrels/add.html", {"form": form})
    else:
        form = EmpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data['Tail_twiches'])
            #Squirrel.objects.create(**data)
            return HttpResponse(
                    'The squirrel is successfully uploaded!'
                )
                # return render(request, "add.html", {"form": form})
        else:
            print(form.errors)
            clean_errors = form.errors.get("__all__")
            print(222, clean_errors)
        return render(request, "squirrels/add.html", {"form": form, "clean_errors":     clean_errors})
    #return render(request, 'squirrels/add.html')
# Create your views here.

def map(request):
    sightings = Squirrel.objects.all()[:100]
    context = {
            'sightings': sightings
    }
    return render(request,'squirrel/map.html',context)


