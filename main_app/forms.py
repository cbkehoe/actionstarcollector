from django.db.models import fields
from django.forms import ModelForm
from .models import Weapon
class WeaponForm(ModelForm):
    class Meta:
        model = Weapon
        fields = ['weaponry']