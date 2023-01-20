from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *


menu = [
        {'title': 'Expenses', 'url': 'expenses'},
        # {'title': 'Load expenses', 'url': ''},
        # {'title': 'History', 'url': ''}
        {'title': 'Sections', 'url': 'sections'},
        {'title': 'Currencies', 'url': 'currencies'},
        {'title': 'About', 'url': 'about'},
]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        user_menu = menu.copy()
        # correct menu if user is not authenticated
        if not self.request.user.is_authenticated:
            user_menu.pop(1)
        else:
            context['user_id'] = self.request.user.id
        context['menu'] = user_menu
        return context
