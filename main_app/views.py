from django.shortcuts import render, redirect
from .forms import WidgetForm
from .models import Stuff
# Create your views here.

def home(request):
    widget_form = WidgetForm()
    widgets = Stuff.objects.all()
    print(widgets)
    return render(request, 'home.html', {'widget_form': widget_form, 'widgets': widgets})

def add_widget(request):
    form = WidgetForm(request.POST)
    if form.is_valid():
        new_widget = form.save(commit=False)
        new_widget.save()
    return redirect('home')