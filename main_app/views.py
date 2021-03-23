from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect

# import models
from .models import Plant
from .forms import GardeningForm


# handle CRUD
class PlantCreate(CreateView):
    model = Plant
    fields = '__all__'
    success_url = "/plants"

class PlantUpdate(UpdateView):
    model = Plant
    fields = ['name', 'plant', 'instruction']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect('/plants/' +str(self.object.pk))

class PlantDelete(DeleteView):
    model = Plant
    success_url = '/plants'


# Create your views here.
def index(request):
    return render(request, 'index.html')

def plants_index(request):
    plants = Plant.objects.all()
    return render(request, 'plants/index.html', { 'plants': plants })

def plants_show(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    gardening_form = GardeningForm()
    return render(request, 'plants/show.html',{
        'plant': plant,
        'gardening_form': gardening_form
    })