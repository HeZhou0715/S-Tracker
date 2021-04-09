from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Squirrel

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
    context = {
        'squirrel': squirrel,
    }

    return render(request, 'app/edit.html', context)
