from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *

menu = [{'title': 'About', 'url': 'about_view'},
        {'title': 'Budget', 'url': 'budget_view'},
        {'title': 'Sections', 'url': 'sections_view'},
        {'title': 'Currencies', 'url': 'currencies_view'},
        {'title': 'Archive', 'url': 'archive_view'},
        {'title': 'Login', 'url': 'login_view'}]


def index_view(request):
    members = FamilyMember.objects.all()
    context = {'menu': menu,
               'title': 'Expenses',
               'members': members
               }
    return render(request, 'budget/index.html', context=context)


def about_view(request):
    return render(request, 'budget/about.html', {'menu': menu})


def budget_view(request):
    return HttpResponse("Expenses")


def sections_view(request):
    return HttpResponse("Sections")


def currencies_view(request):
    try:
        currencies = Currency.objects.all()
        context = {'menu': menu,
                   'title': 'Currencies',
                   'currencies': currencies
                   }
        return render(request, 'budget/currencies.html', context=context)
    except:
        raise Exception


def edit_currency_view(request, currency_id):
    try:
        currency = Currency.objects.filter(pk=currency_id)
        edited_currency = currency[0].currency
        return HttpResponse(f"Currency {edited_currency} successfully updated.")
    except:
        raise Exception


def delete_currency_view(request, currency_id):
    try:
        currency = Currency.objects.filter(pk=currency_id)
        deleted_currency = currency[0].currency
        currency.delete()
        return HttpResponse(f"Currency {deleted_currency} successfully deleted.")
    except:
        raise Exception


def add_currency_view(request):
    try:
        new_currency = Currency(currency='GEL',
                                country='Georgia',
                                creator_id_id=2,
                                editor_id_id=2
                                )
        new_currency.save()
        context = {'message': f'New currency {new_currency.currency} successfully added'}
        return render(request, 'budget/success.html', context=context)
    except:
        raise Exception


def login_view(request):
    return HttpResponse("Login")


def archive_view(request):
    return HttpResponse(f"archive")


def page_not_found_view(request, exception):
    return HttpResponseNotFound("Page not found")
