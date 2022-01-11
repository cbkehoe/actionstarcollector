from django.db import models
from django.urls import reverse
# Create your models here.

class Star(models.Model):  # Note that parens are optional if not inheriting from another class
    name = models.CharField(max_length = 100) 
    powerlvl = models.IntegerField()
    description = models.TextField(max_length=250)
    specialty = models.CharField(max_length=250)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'star_id' : self.id})

