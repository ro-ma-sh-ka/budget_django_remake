from django.shortcuts import render
from django.http import HttpResponse


def expenses_view(request):
    return HttpResponse("expenses")


def sections_view(request):
    return HttpResponse("Sections")


def currencies_view(request):
    return HttpResponse("Currencies")
