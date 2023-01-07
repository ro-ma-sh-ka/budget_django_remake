from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *
from .forms import *

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


def add_currency_view(request):
    if request.method == 'POST':
        form = AddNewCurrency(request.POST)
        if form.is_valid():
            try:
                Currency.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, 'New currency has not added.')
    else:
        form = AddNewCurrency()
    context = {'form': form,
               'menu': menu,
               'message': 'add new currency',
               'title': 'add new currency'}
    return render(request, 'budget/new_currency.html', context=context)


def edit_currency_view(request, currency_id):
    try:
        currency = Currency.objects.filter(pk=currency_id)
    except:
        raise Exception
    data = {
        'currency': currency[0].currency,
        'country': currency[0].country
    }

    if request.method == 'POST':
        form = CurrencyForm(request.POST)
        if form.is_valid():
            try:
                Currency.objects.filter(pk=currency_id).update(**form.cleaned_data)
                return redirect('currencies_view')
            except:
                form.add_error(None, 'New currency has not edited.')
    else:
        form = CurrencyForm(data)
        context = {'form': form,
                   'currency_id': currency_id,
                   'menu': menu,
                   'message': 'edit currency',
                   'title': 'edit currency'}
        return render(request, 'budget/edit_currency.html', context=context)


def delete_currency_view(request, currency_id):
    try:
        currency = Currency.objects.filter(pk=currency_id)
        deleted_currency = currency[0].currency
        currency.delete()
        return HttpResponse(f"Currency {deleted_currency} successfully deleted.")
    except:
        raise Exception


def login_view(request):
    return HttpResponse("Login")


def archive_view(request):
    return HttpResponse(f"archive")


def page_not_found_view(request, exception):
    return HttpResponseNotFound("Page not found")
