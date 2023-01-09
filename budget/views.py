from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

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


class AddSection(LoginRequiredMixin, DataMixin, CreateView):
    form_class = SectionForm
    template_name = 'budget/new_section.html'

    # redirect after we add new section
    success_url = reverse_lazy('sections')

    # redirect to login page thanks to LoginRequiredMixin
    login_url = reverse_lazy('sections')

    # method to send to our template dynamic and/or static content
    def get_context_data(self, *, object_list=None, **kwargs):

        # catch context - all named parameters which already exist such as: template_name, context_object_name
        context = super().get_context_data(**kwargs)

        # use this method to send data to mixin
        c_def = self.get_user_context(title='Add new section')
        context = dict(list(context.items()) + list(c_def.items()))
        return context


def edit_section_view(request, section_id):
    try:
        section = Section.objects.filter(pk=section_id)
    except:
        raise Exception
    data = {
        'section': section[0].section,
    }

    if request.method == 'POST':
        form = SectionForm(request.POST)
        if form.is_valid():
            try:
                Section.objects.filter(pk=section_id).update(**form.cleaned_data)
                return redirect('sections')
            except:
                form.add_error(None, 'New section has not edited.')
    else:
        form = SectionForm(data)
        context = {'form': form,
                   'section_id': section_id,
                   'menu': menu,
                   'message': 'edit section',
                   'title': 'edit section'}
        return render(request, 'budget/edit_section.html', context=context)


def delete_section_view(request, section_id):
    try:
        section = Section.objects.filter(pk=section_id)
        section.delete()
        return redirect('sections')
    except:
        raise Exception


# CBV - Class Based Views
class SectionsView(DataMixin, ListView):
    model = Section
    template_name = 'budget/sections.html'
    context_object_name = 'sections'

    # method to send to our template dynamic and/or static content
    def get_context_data(self, *, object_list=None, **kwargs):
        # catch context - all named parameters which already exist such as: template_name, context_object_name
        context = super().get_context_data(**kwargs)
        # use this method to send data to mixin
        c_def = self.get_user_context(title='Sections')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    # by default ListView takes all data from database, but we can use this method to filter from database
    def get_queryset(self):
        return Section.objects.all()


# CBV - Class Based Views
class CurrenciesView(DataMixin, ListView):
    model = Currency
    # by default this class uses template <app_name>/<model_name>_list.html, but we set our template
    template_name = 'budget/currencies.html'
    # by default this class uses variable object_list, but we set name of variable which we send to template
    context_object_name = 'currencies'

    # method to send to our template dynamic and/or static content
    def get_context_data(self, *, object_list=None, **kwargs):
        # catch context - all named parameters which already exist such as: template_name, context_object_name
        context = super().get_context_data(**kwargs)

        # use this method to send data to mixin
        c_def = self.get_user_context(title='Currencies')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    # by default ListView takes all data from database, but we can use this method to filter from database
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
    success_url = reverse_lazy('currencies')

    # redirect to login page thanks to LoginRequiredMixin
    login_url = reverse_lazy('currencies')

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
                return redirect('currencies')
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
        return redirect('currencies')
    except:
        raise Exception


def logout_user_view(request):
    logout(request)
    return redirect('login')


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'budget/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        # catch context - all named parameters which already exist such as: template_name, context_object_name
        context = super().get_context_data(**kwargs)

        # use this method to send data to mixin
        c_def = self.get_user_context(title='Authorization')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_success_url(self):
        return reverse_lazy('home')


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'budget/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):

        # catch context - all named parameters which already exist such as: template_name, context_object_name
        context = super().get_context_data(**kwargs)

        # use this method to send data to mixin
        c_def = self.get_user_context(title='Registration')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    # automatic redirect authorized user to the main page
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


def page_not_found_view(request, exception):
    return HttpResponseNotFound("Page not found")
