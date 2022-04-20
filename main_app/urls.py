from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('add_widget/', views.add_widget, name='add_widget')
]