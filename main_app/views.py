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
        context["budgets"] = Budget.objects.all # this is where we add the key into our context object for the view to use
        return context


