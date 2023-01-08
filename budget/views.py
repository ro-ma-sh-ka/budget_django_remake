from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *
from .utils import *


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


# CBV - Class Based Views
class CurrenciesView(DataMixin, ListView):
    model = Currency
    # this class uses template <app_name>/<model_name>_list.html but we set our template
    template_name = 'budget/currencies.html'
    # this class uses variable object_list but we set name of variable which we send to template
    context_object_name = 'currencies'

    # method to send to our template dynamic and/or static content
    def get_context_data(self, *, object_list=None, **kwargs):
        # catch context - all named parameters which already exist such as: template_name, context_object_name
        context = super().get_context_data(**kwargs)

        # use this method to send data to mixin
        c_def = self.get_user_context(title='Currencies')
        context = dict(list(context.items()) + list(c_def.items()))
        # context['menu'] = menu
        # context['title'] = 'Currencies'
        return context

    # use this method to filter from database
    def get_queryset(self):
        return Currency.objects.all()


# def currencies_view(request):
#     try:
#         currencies = Currency.objects.all()
#         context = {'menu': menu,
#                    'title': 'Currencies',
#                    'currencies': currencies
#                    }
#         return render(request, 'budget/currencies.html', context=context)
#     except:
#         raise Exception


class AddCurrency(LoginRequiredMixin, DataMixin, CreateView):
    form_class = CurrencyForm
    template_name = 'budget/new_currency.html'

    # redirect after we add new currency
    success_url = reverse_lazy('currencies_view')

    # redirect to login page thanks to LoginRequiredMixin
    login_url = reverse_lazy('currencies_view')

    # method to send to our template dynamic and/or static content
    def get_context_data(self, *, object_list=None, **kwargs):

        # catch context - all named parameters which already exist such as: template_name, context_object_name
        context = super().get_context_data(**kwargs)

        # use this method to send data to mixin
        c_def = self.get_user_context(title='Add new currency')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

# @login_required(redirect_field_name='login')
# def add_currency_view(request):
#     if request.method == 'POST':
#         form = CurrencyForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('currencies_view')
#     else:
#         form = CurrencyForm()
#     context = {'form': form,
#                'menu': menu,
#                'message': 'add new currency',
#                'title': 'add new currency'}
#     return render(request, 'budget/new_currency.html', context=context)


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
        currency.delete()
        return redirect('currencies_view')
    except:
        raise Exception


def login_view(request):
    return HttpResponse("Login")


def register_view(request):
    return HttpResponse("Register")


def archive_view(request):
    return HttpResponse(f"archive")


def page_not_found_view(request, exception):
    return HttpResponseNotFound("Page not found")
