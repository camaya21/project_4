from django.contrib import admin
from .models import Budget
from .models import Expense

admin.site.register(Budget)
admin.site.register(Expense)

# Register your models here.
