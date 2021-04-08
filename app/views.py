from django.shortcuts import render

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
