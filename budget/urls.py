from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index_view, name='index_view'),
    path('about/', about_view, name='about_view'),
    path('budget/', budget_view, name='budget_view'),
    path('sections/', sections_view, name='sections_view'),
    path('currencies/', currencies_view, name='currencies_view'),
    # path('expense/<int:expense_id>', edit_expense_view, name='edit_expense_view'),
    # path('section/<int:section_id>', edit_section_view, name='edit_section_view'),
    path('currency/<int:currency_id>', edit_currency_view, name='edit_currency_view'),
    path('currency_added', add_currency_view, name='add_currency_view'),
    path('archive/', archive_view, name='archive_view'),
    # re_path(r'archive/(?P<year>[0-9]{4})/', archive_view, name='archive_view'),
    path('login/', login_view, name='login_view'),
]