from django.shortcuts import render
from .models import Category, Poem


def index(request):
    data = {"categories": Category.objects.all()}
    return render(request, "core/Index.html", data)


def about_author(request):
    return render(request, "core/obomne.html")


def publications(request):
    return render(request, "core/publications.html")


def contacts(request):
    return render(request, "core/Contacts.html")


def portal(request):
    return render(request, "core/")


def lyrics_list(request):
    category_id = request.GET.get("category_id")
    data = {"poems": Poem.objects.all().filter(category__id=category_id), "category": Category.objects.all().filter(id=category_id).first()}
    return render(request, "core/Grazhdlyrics.html", data)


def poem(request):
    poem_id = request.GET.get("id")
    data = {"poem": Poem.objects.all().filter(id=poem_id).first}
    return render(request, "core/poem.html", data)


