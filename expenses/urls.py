from django.urls import path
from .views import *

urlpatterns = [
    path('', expenses_view, name='expenses_view'),
    path('sections/', sections_view, name='sections_view'),
    path('currencies/', currencies_view, name='currencies_view'),
]