from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View
from django.http import HttpResponse
from .models import Budget
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse
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
            context["header"] = f"searching for {name}"
        else:
            context["budgets"]= Budget.objects.all()
            context["header"] = "All Budgets"
        return context

class BudgetCreate(CreateView):
    model = Budget
    fields = ['name', 'amount']
    template_name = "budget_create.html"
    success_url = "/budgets/"

class BudgetDetail(DetailView):
    model = Budget
    template_name = "budget_detail.html"

class BudgetUpdate(UpdateView):
    model = Budget
    fields = ['name', 'amount']
    template_name = "budget_update.html"

    def get_success_url(self):
        return reverse('budget_detail', kwargs={'pk': self.object.pk})

class BudgetDelete(DeleteView):
    model = Budget
    template_name = "budget_delete_confirmation.html"
    success_url = "/budgets/"