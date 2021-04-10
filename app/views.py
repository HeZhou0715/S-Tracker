from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse

from .models import Squirrel
from .forms import SquirrelForm

# Create your views here.

def mainpage(request):

    return render(request, 'app/mainpage.heml', {})

def list(request):

    squirrels = Squirrel.objects.all()
    context = {
        'squirrels': squirrels,
    }

    return render(request, 'app/list.html', context)

def edit(request, id):
    
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
        form = SquirrelForm()
        context = {
            'squirrel': squirrel,
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
