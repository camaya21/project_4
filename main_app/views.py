from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View
from django.http import HttpResponse
from .models import Budget
# Create your views here.

 #adds artist class for mock database data

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class BudgetList(TemplateView):
    template_name = "budget_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["budgets"] = Budget.objects.filter(name__icontains=name)
        else:
            context["budgets"]= Budget.objects.all()
        return context


