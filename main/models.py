from django.db import models

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=45)

class Continent(models.Model):
  name = models.CharField(max_length=45)

class Country(models.Model):
  name = models.CharField(max_length=45)
  continent = models.ForeignKey('Continent', on_delete=models.CASCADE)

class Winner(models.Model):
  country = models.ForeignKey('Country', on_delete=models.CASCADE)

class Person(Winner):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  gender = models.CharField(max_length=45)
  date_of_birth = models.DateField()

class Organiztion(Winner):
  name = models.CharField(max_length=100)

class Prize(models.Model):
  category = models.ForeignKey('Category', on_delete=models.CASCADE)
  winner = models.ForeignKey('Winner', on_delete=models.CASCADE)
  year = models.SmallIntegerField()
