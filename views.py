from django.shortcuts import render
from django.views import generic
from .models import Location,Property

class IndexView(generic.ListView):
    template_name = 'homesapp/index.html'

# Create your views here.
    def get_queryset(self):
        return Location.objects.all()


class LocationView(generic.DetailView):
    model = Location
    template_name = 'homesapp/locationview.html'     


class PropertyDetail(generic.DetailView):
    model = Property
    template_name  = 'homesapp/propertyview.html'    