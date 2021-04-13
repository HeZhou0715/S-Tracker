from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse

from .models import Squirrel
from .forms import SquirrelForm

# Create your views here.

def mainpage(request):

    return render(request, 'app/mainpage.html', {})

def list(request):

    squirrels = Squirrel.objects.all()
    context = {
        'squirrels': squirrels,
    }

    return render(request, 'app/list.html', context)

def edit(request, unique_squirrel_id):
    
    squirrel = get_object_or_404(Squirrel, pk=unique_squirrel_id)
    
    if request.method == 'POST':
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            squirrels = Squirrel.objects.all()
            context = {
                'squirrels': squirrels,
            }
            return render(request, 'app/list.html', context)
    else:
        form = SquirrelForm(instance = squirrel)
        context = {
            'form': form,
        }
        return render(request, 'app/edit.html', context)

def add(request):

    if request.method == 'POST':
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            squirrels = Squirrel.objects.all()
            context = {
                'squirrels': squirrels,
            }
            return render(request, 'app/list.html', context)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = SquirrelForm()
        context = {
                'form': form,
            }
        return render(request, 'app/edit.html', context)

def map(request):
    part_squirrels = Squirrel.objects.all()[:100]

    context = {
        'part_squirrels' = part_squirrels,
    }
    return render(request, 'app/map.html', context)

def stats(request):

    am_count = Squirrel.objects.filter(shift = 'AM').count()
    pm_count = Squirrel.objects.filter(shift = 'PM').count()
    ground_count = Squirrel.objects.filter(location = 'Ground Plane').count()
    running_count = Squirrel.objects.filter(running = True).count()
    adult_count = Squirrel.objects.filter(age = 'Adult').count()
    total_number = len(Squirrel.objects.all())
    
    context = {
        'total_number': total_number,
        'am_count': am_count,
        'pm_count': pm_count,
        'adult_count': adult_count,
        'ground_count': ground_count,
        'running_count': running_count,
    }

    return render(request, 'app/stats.html', context)
