from django.urls import path
from .views import *

urlpatterns = [
    path('', index_view, name='home'),
    path('about/', about_view, name='about'),
    path('budget/', budget_view, name='budget'),
    path('sections/', SectionsView.as_view(), name='sections'),
    path('section_edit/<int:section_id>', edit_section_view, name='edit_section'),
    path('section_add/', AddSection.as_view(), name='add_section'),
    path('section_delete/<int:section_id>', delete_section_view, name='delete_section'),
    # path('expense/<int:expense_id>', edit_expense_view, name='edit_expense_view'),
    # path('section/<int:section_id>', edit_section_view, name='edit_section_view'),

    # use CBV to show list of currencies. Method as_view connects class with path to page
    path('currencies/', CurrenciesView.as_view(), name='currencies'),
    path('currency_add/', AddCurrency.as_view(), name='add_currency'),
    path('currency_edit/<int:currency_id>', edit_currency_view, name='edit_currency'),
    path('currency_delete/<int:currency_id>', delete_currency_view, name='delete_currency'),
    path('logout/', logout_user_view, name='logout'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
]