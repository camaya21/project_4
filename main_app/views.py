from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views import View
from django.http import HttpResponse
from .models import Budget
from .models import Expense
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

 #adds artist class for mock database data

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"


# BUDGET ROUTES
@method_decorator(login_required, name='dispatch')
class BudgetList(TemplateView):
    template_name = "budget_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["budgets"] = Budget.objects.filter(name__icontains=name, user=self.request.user)
            context["header"] = f"searching for {name}"
        else:
            context["budgets"]= Budget.objects.filter(user=self.request.user)
            context["header"] = "All Budgets"
        return context

class BudgetCreate(CreateView):
    model = Budget
    fields = ['name', 'amount']
    template_name = "budget_create.html"
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BudgetCreate, self).form_valid(form)

    def get_success_url(self):
        print(self.kwargs)
        return reverse('budget_detail', kwargs={'pk': self.object.pk})

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

class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("budget_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)

# EXPENSES ROUTES
class ExpenseList(TemplateView):
    template_name = "expense_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["expenses"] = Expense.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["expenses"] = Expense.objects.all()
            context["header"] = "All Expenses"
        return context

class ExpenseCreate(CreateView):
    model = Expense
    fields = ['name', 'amount', 'date']
    template_name = "expense_create.html"
    success_url = "/expenses/"

class ExpenseUpdate(UpdateView):
    model = Expense
    fields = ['name', 'amount', 'date']
    template_name = "expense_update.html"
    success_url = "/expenses/"


