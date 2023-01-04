from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index_view, name='index_view'),
    path('about/', about_view, name='about_view'),
    path('sections/', sections_view, name='sections_view'),
    path('currencies/', currencies_view, name='currencies_view'),
    re_path(r'archive/(?P<year>[0-9]{4})/', archive_view, name='archive_view'),
]