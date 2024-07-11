from django.http import HttpResponse
from django.shortcuts import render

from films.models import Film


def index(request):
    return render(request, 'films/index.html')


def watched_list(request):
    films = Film.objects.filter(
        ...
    )