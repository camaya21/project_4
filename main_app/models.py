from django.db import models
from django.contrib.auth.models import User
import datetime
from djmoney.models.fields import MoneyField
from django import forms

class Budget(models.Model):
    name = models.CharField(max_length=100)
    amount = MoneyField(max_digits=19, decimal_places=4, default_currency='USD')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Expense(models.Model):
    name = models.CharField(max_length=100)
    amount = MoneyField(max_digits=19, decimal_places=4, default_currency='USD')
    date = models.DateField(null=True)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name="expenses", default=1)

    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

# class Balance(models.Model):
#     name = models.CharField(max_length=100)
#     amount = MoneyField(max_digits=19, decimal_places=4, default_currency='USD')
#     date = models.DateField(null=True, )

# Create your models here.

