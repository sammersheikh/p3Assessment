from django.forms import ModelForm
from .models import Stuff

class WidgetForm(ModelForm):
  class Meta:
    model = Stuff
    fields = '__all__'