from django.db import models
from composite_field import CompositeField

class NameModel(models.Model):
  name = models.CharField(max_length=45)

  class Meta:
    abstract = True

  def __str__(self):
    return self.name

# Create your models here.
class Category(NameModel):
  pass

class Continent(NameModel):
  pass

class Country(NameModel):
  continent = models.ForeignKey('Continent', on_delete=models.CASCADE)

class Winner(models.Model):
  country = models.ForeignKey('Country', on_delete=models.CASCADE)

class Person(Winner):
  name_first = models.CharField(max_length=45)
  name_last = models.CharField(max_length=45)
  gender = models.BooleanField()
  date_of_birth = models.DateField()

  def __str__(self):
    return '{} {}'.format(self.name_first, self.name_last)

class Organization(Winner, NameModel):
  pass

class Prize(models.Model):
  category = models.ForeignKey('Category', on_delete=models.CASCADE)
  winner = models.ForeignKey('Winner', on_delete=models.CASCADE)
  year = models.SmallIntegerField()
