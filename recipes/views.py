from django.http import HttpResponse
from django.shortcuts import render
from utils.recipes.factory import make_recipe

from recipes.models import Recipe

# Create your views here.

def home(request):
    recipes = Recipe.objects.all().filter(is_published=True).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={'recipes': recipes,})

def recipe(request, id):
    recipes = Recipe.objects.filter(id=id, is_published=True).first()
    return render(request, 'recipes/pages/recipe-view.html', context={'recipe': recipes,'is_detail_page':True,})

def category(request, category_id):
    recipes = Recipe.objects.filter(category__id=category_id, is_published=True).order_by('-id')
    return render(request, 'recipes/pages/category.html', context={'recipes': recipes,})
