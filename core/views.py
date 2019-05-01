from django.shortcuts import render
from .models import Category


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


