from django.db import models
from django.urls import reverse
# Create your models here.

WEAPONRY = (
    ('S', 'Sword'),
    ('G', 'Gun'),
    ('H', 'Hand-to-Hand')
)

class Star(models.Model):  # Note that parens are optional if not inheriting from another class
    name = models.CharField(max_length = 100) 
    powerlvl = models.IntegerField()
    description = models.TextField(max_length=250)
    specialty = models.CharField(max_length=250)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'star_id' : self.id})

class Weapon(models.Model):
    weaponry = models.CharField(
        max_length=1,
        choices=WEAPONRY,
        default=WEAPONRY[0][0])
    
    star = models.ForeignKey(Star, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_weaponry_display()}"