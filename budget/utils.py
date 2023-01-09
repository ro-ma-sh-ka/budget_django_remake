from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *


menu = [
        {'title': 'About', 'url': 'about'},
        {'title': 'Budget', 'url': 'budget'},
        {'title': 'Sections', 'url': 'sections'},
        {'title': 'Currencies', 'url': 'currencies'},
]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        user_menu = menu.copy()
        # correct menu if user is not authenticated
        if not self.request.user.is_authenticated:
            user_menu.pop(1)
        context['menu'] = user_menu
        return context
