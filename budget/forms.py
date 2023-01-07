from django import forms
from .models import *


class CurrencyForm(forms.ModelForm):
    class Meta:
        model = Currency
        fields = '__all__'


class AddNewCurrency(forms.Form):
    currency = forms.CharField(max_length=20, label='Currency:')
    country = forms.CharField(max_length=20, label='Country:')
    creator_id = forms.ModelChoiceField(queryset=FamilyMember.objects.all(), label='Creator:')
    editor_id = forms.ModelChoiceField(queryset=FamilyMember.objects.all(), label='Editor:')


class AddNewExpense(forms.Form):
    date = forms.DateField(label='Date:')
    total = forms.FloatField(label='Sum:')
    currency_id = forms.ModelChoiceField(queryset=Currency.objects.all(), initial='RUB', label='Currency:')
    what_is = forms.CharField(max_length=255, label='Description:')
    section_id = forms.ModelChoiceField(queryset=Section.objects.all(), label='Section:', initial='-')
    public = forms.BooleanField(required=False, initial=False, label='Public:')
    creator_id = forms.ModelChoiceField(queryset=FamilyMember.objects.all(), label='Creator:')
    editor_id = forms.ModelChoiceField(queryset=FamilyMember.objects.all(), label='Editor:')
