from django.db import models


class FamilyMember(models.Model):
    member = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.member


class Currency(models.Model):
    currency = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    creator_id = models.ForeignKey(FamilyMember, on_delete=models.CASCADE, related_name='+')
    created_at = models.DateTimeField(auto_now_add=True)
    editor_id = models.ForeignKey(FamilyMember, on_delete=models.CASCADE, related_name='+')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.currency


class Section(models.Model):
    section = models.CharField(max_length=30)
    creator_id = models.ForeignKey(FamilyMember, on_delete=models.CASCADE, related_name='+')
    created_at = models.DateTimeField(auto_now_add=True)
    editor_id = models.ForeignKey(FamilyMember, on_delete=models.CASCADE, related_name='+')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.section


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
