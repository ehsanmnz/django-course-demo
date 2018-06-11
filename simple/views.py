from django.shortcuts import render, HttpResponse
from .models import Person
# Create your views here.


def index(request):
    persons = Person.objects.all()
    return render(request, 'simple/index.html', context={"persons": persons})
