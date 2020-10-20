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
            Squirrel.objects.create(**data)
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
    return render(request,'squirrels/map.html',context)

def stats(request):
    sightings_total = Squirrel.objects.count()
    sightings_black = Squirrel.objects.filter(Primary_Fur_Color = 'Black').count()
    chasing_true = Squirrel.objects.filter(Chasing=True).count()
    sightings_grey = Squirrel.objects.filter(Primary_Fur_Color = 'Gray').count()
    eating_true = Squirrel.objects,filter(Eating=True).count()
    context = {
            'sightings_total':sightings_total,
            'sightings_grey':sightings_grey,
            'sightings_black': sightings_black,
            'chasing_true':chasing_true,
            'eating_true':eating_true,
            }
    return render(request,'squirrels/stats.html',context)


def update(request,unique_squirrel_id):
    squirrel=Squirrel.objects.get(unique_squirrel_id=unique_squirrel_id)
    if request.method == 'POST':
        form = SquirrelForm(request.Post, instance = squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings')
        else:
            form = SquirrelForm(instance=squirrel)
        context = {'form':form,}
        return render(request,'squirrels/update/html',conext)





