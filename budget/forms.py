from django import forms
from .models import *


class CurrencyForm(forms.ModelForm):

    # run this constructor when we create a class instance
    def __init__(self, *args, **kwargs):

        # base class constructor to run all automatic actions
        super().__init__(*args, **kwargs)

        # after we run super constructor we have properties for class instances
        self.fields['creator_id'].label = 'Creator:'
        self.fields['creator_id'].empty_label = 2
        self.fields['editor_id'].label = 'Editor:'
        self.fields['editor_id'].empty_label = 2

    class Meta:
        model = Currency
        fields = ['currency', 'country', 'creator_id', 'editor_id']
        # widgets = {
        #     'currency': forms.CharField(max_length=20, label='Currency:'),
        #     'country': forms.CharField(max_length=20, label='Country:'),
        #     'creator_id': forms.ModelChoiceField(queryset=FamilyMember.objects.all(), label='Creator:'),
        #     'editor_id': forms.ModelChoiceField(queryset=FamilyMember.objects.all(), label='Editor:')
        # }
