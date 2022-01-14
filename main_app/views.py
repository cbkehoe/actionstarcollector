from django.db.models import fields
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Star
from .forms import WeaponForm
from django.shortcuts import render, redirect


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
    vehicles_star_doesnt_have = Vehicle.ojects.exlude(id__in = star.vehicles.all().values_list('id'))
    weapon_form = WeaponForm()
    return render(request, 'stars/detail.html', {
        'star' : star, 'weapon_form' : weapon_form,
        'vehicle' : vehicles_star_doesnt_have})

def add_weapon(request, star_id):
    form = WeaponForm(request.POST)
    if form.is_valid():
        new_weapon = form.save(commit=False)
        new_weapon.star_id = star_id
        new_weapon.save()
    return redirect('detail', star_id=star_id)
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