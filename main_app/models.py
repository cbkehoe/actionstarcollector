from django.db import models

# Create your models here.

class Star:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, powerlvl, description, specialty):
    self.name = name
    self.powerlvl = powerlvl
    self.description = description
    self.specialty = specialty

Stars = [
  Star('Arnold', 10, 'The Terminator', 'Super Strength, Guns'),
  Star('Van Damme', 8, 'Master of the splits', 'Martial Arts'),
  Star('Seagal', 11, 'Master of Akido and gaining mass', 'Martial Arts, Firearms, Seduction')
]