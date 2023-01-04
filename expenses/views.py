from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404


def expenses_view(request):
    return HttpResponse("expenses")


def sections_view(request):
    return HttpResponse("Sections")


def currencies_view(request):
    return HttpResponse("Currencies")


def archive_view(request, year):
    if int(year) > 2022:
        # redirect to main page if no year
        return redirect('expenses_view', permanent=True)
    return HttpResponse(f"archive {year}")


def page_not_found_view(request, exception):
    return HttpResponseNotFound("Page not found")
