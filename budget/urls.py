from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index_view, name='home'),
    path('about/', about_view, name='about_view'),
    path('budget/', budget_view, name='budget_view'),
    path('sections/', sections_view, name='sections_view'),
    # path('expense/<int:expense_id>', edit_expense_view, name='edit_expense_view'),
    # path('section/<int:section_id>', edit_section_view, name='edit_section_view'),
    # use CBV to show list of currencies. Method as_view connects class with path to page
    path('currencies/', CurrenciesView.as_view(), name='currencies_view'),
    path('currency_add', AddCurrency.as_view(), name='add_currency_view'),
    # path('currencies/', currencies_view, name='currencies_view'),

    path('currency_edit/<int:currency_id>', edit_currency_view, name='edit_currency_view'),
    path('currency_delete/<int:currency_id>', delete_currency_view, name='delete_currency_view'),
    # path('currency_add', add_currency_view, name='add_currency_view'),
    # path('archive/', archive_view, name='archive_view'),
    path('logout/', logout_user_view, name='logout'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    # path('register/', register_view, name='register_view'),
]