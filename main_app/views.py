from django.db.models import fields
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView



from .models import Star
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def stars_index(request):
    stars = Star.objects.all()
    return render(request, 'stars/index.html', { 'stars' : stars})

def stars_detail(request, star_id):
    star = Star.objects.get(id=star_id)
    return render(request, 'stars/detail.html', {'star' : star})


#class based objects below

class StarCreate(CreateView):
    model = Star
    fields = '__all__'

class StarUpdate(UpdateView):
    model = Star
    fields = ['powerlvl', 'description', 'specialty']

class StarDelete(DeleteView):
    model = Star
    success_url = '/stars/'