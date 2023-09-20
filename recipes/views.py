from django.shortcuts import render, HttpResponse
from . import models

recipes = [
    {
        'author': 'Dennis L.',
        'title': 'Vodka Orange',
        'content': 'mix vodka with orange',
        'date_posted': 'May 9th, 2023'
    },

    {
        'author': 'Dennis F.',
        'title': 'Vodka Cranberry',
        'content': 'mix vodka with Cranberry',
        'date_posted': 'May 15th, 2023'
    },

    {
        'author': 'Dennis L.',
        'title': 'Vodka Orange',
        'content': 'mix vodka with orange',
        'date_posted': 'May 9th, 2023'
    }
]

# Create your views here.


def home(request):
    recipes = models.recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, "recipes/home.html", context)


def about(request):
    return render(request, "recipes/about.html",)
