from django.db import models
from django.urls import reverse


class FamilyMember(models.Model):
    member = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)

    # use this function to create absolute urls to manage our users
    def get_absolute_url(self):
        return reverse('user', kwargs={'user_id': self.pk})


class Currency(models.Model):
    currency = models.CharField(max_length=20, unique=True, verbose_name='Currency:')
    country = models.CharField(max_length=20, unique=True, verbose_name='Country:')
    creator_id = models.ForeignKey(FamilyMember, on_delete=models.CASCADE, related_name='+')
    created_at = models.DateTimeField(auto_now_add=True)
    editor_id = models.ForeignKey(FamilyMember, on_delete=models.CASCADE, related_name='+')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.currency

    # use this functions to create absolute urls to manage our currencies
    # def get_absolute_url(self):
    #     return reverse('add_currency_view', kwargs={'currency_id': self.pk})

    def edit_currency(self):
        return reverse('edit_currency', kwargs={'currency_id': self.pk})

    def delete_currency(self):
        return reverse('delete_currency', kwargs={'currency_id': self.pk})


class Section(models.Model):
    section = models.CharField(max_length=30)
    creator_id = models.ForeignKey(FamilyMember, on_delete=models.CASCADE, related_name='+')
    created_at = models.DateTimeField(auto_now_add=True)
    editor_id = models.ForeignKey(FamilyMember, on_delete=models.CASCADE, related_name='+')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.section

    def edit_section(self):
        return reverse('edit_section', kwargs={'section_id': self.pk})

    def delete_section(self):
        return reverse('delete_section', kwargs={'section_id': self.pk})

    # use this function to create absolute urls to manage our sections
    # def get_absolute_url(self, method):
    #     return reverse(method, kwargs={'section_id': self.pk})


class Budget(models.Model):
    creator_id = models.ForeignKey(FamilyMember, on_delete=models.CASCADE, related_name='+')
    created_at = models.DateTimeField(auto_now_add=True)
    editor_id = models.ForeignKey(FamilyMember, on_delete=models.CASCADE, related_name='+')
    updated_at = models.DateTimeField(auto_now=True)
    date = models.DateField()
    total = models.FloatField()
    currency_id = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='+')
    what_is = models.TextField(max_length=200)
    section_id = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='+')
    public = models.BooleanField(default=True)

    # use this function to create absolute urls to reverse user to page
    def get_absolute_url(self):
        return reverse('expense', kwargs={'expense_id': self.pk})

    def edit_expense(self):
        return reverse('edit_expense', kwargs={'expense_id': self.pk})

    def delete_expense(self):
        return reverse('delete_expense', kwargs={'expense_id': self.pk})
