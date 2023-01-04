from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *


menu = ['About', 'Add expenses', 'Add currency', 'Add section']


def index_view(request):
    members = FamilyMember.objects.all()
    return render(request, 'expenses/index.html', {'menu': menu, 'title': 'Main page', 'members': members})


def about_view(request):
    return render(request, 'expenses/about.html', {'menu': menu, 'title': 'About'})


def sections_view(request):
    return HttpResponse("Sections")


def currencies_view(request):
    return HttpResponse("Currencies")


def archive_view(request, year):
    if int(year) > 2022 or int(year) < 2020:
        # redirect to the main page if no year
        return redirect('expenses_view', permanent=True)
    return HttpResponse(f"archive {year}")


def page_not_found_view(request, exception):
    return HttpResponseNotFound("Page not found")
