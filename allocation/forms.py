from .models import *
from django.forms import ModelForm

class AllocateForm(ModelForm):
    class Meta:
        model = Item
        fields =['name','district','category']
        # fields ='__all__'

class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields =['remarks']

class ReallocateForm(ModelForm):
    class Meta:
        model = Reallocation
        # fields ='__all__'
        fields = ['item','initiator','approved']