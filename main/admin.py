from django.contrib import admin

from .models import *

# Register your models here.
@admin.register(Category, Continent, Country, Organization)
class NameAdmin(admin.ModelAdmin):
  list_display = ('id', 'name')

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
  list_display = ('id', 'name_last', 'name_first', 'gender', 'date_of_birth')

@admin.register(Prize)
class PrizeAdmin(admin.ModelAdmin):
  list_display = ('id', 'category', 'winner', 'year')
