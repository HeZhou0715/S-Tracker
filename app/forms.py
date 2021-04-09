
from django.forms import ModelForm

from .models import Squirrel


class SquirrelForm(ModelForm):
    class Meta:
        model = AdoptRequest
        fields = '__all__'
