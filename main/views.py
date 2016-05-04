from django.http import HttpResponse
from django.shortcuts import render

from .models import Prize

def index(request):
  prizes = Prize.objects.all()
  context = {'prizes': prizes}
  return render(request, 'main/index.html', context)

