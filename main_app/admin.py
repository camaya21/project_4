from django.contrib import admin
from .models import Budget
from .models import Expenses

admin.site.register(Budget)
admin.site.register(Expenses)

# Register your models here.
