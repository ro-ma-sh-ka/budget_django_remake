from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class CurrencyForm(forms.ModelForm):
    # run this constructor when we create a class instance
    def __init__(self, *args, **kwargs):

        # base class constructor to run all automatic actions
        super().__init__(*args, **kwargs)

        # after we run super constructor we have properties for class instances
        self.fields['creator_id'].label = 'Creator:'
        self.fields['editor_id'].label = 'Editor:'

    # connect form with table and set fields which we show
    class Meta:
        model = Currency
        fields = ['currency', 'country', 'creator_id', 'editor_id']
        # widgets = {
        #     'currency': forms.CharField(max_length=20, label='Currency:'),
        #     'country': forms.CharField(max_length=20, label='Country:'),
        #     'creator_id': forms.ModelChoiceField(queryset=FamilyMember.objects.all(), label='Creator:'),
        #     'editor_id': forms.ModelChoiceField(queryset=FamilyMember.objects.all(), label='Editor:')
        # }


class SectionForm(forms.ModelForm):
    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)

    # connect form with table and set fields which we show
    class Meta:
        model = Section
        fields = ['section', 'creator_id', 'editor_id']


class ExpenseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Budget
        fields = ['what_is', 'total']


class RegisterUserForm(UserCreationForm):
    class Meta:
        username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
        password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
        password2 = forms.CharField(label='Password confirmation',
                                    widget=forms.PasswordInput(attrs={'class': 'form-input'}))
        model = User
        fields = ('username', 'password1', 'password2')
