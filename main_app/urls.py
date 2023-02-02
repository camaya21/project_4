from django.urls import path, include
from . import views
from django.contrib import admin
# from django.conf.urls.static import static
# from django.conf import settings

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    # Budget Paths
    path('budgets/', views.BudgetList.as_view(), name="budget_list"),
    path('bugdets/new/', views.BudgetCreate.as_view(), name="budget_create"),
    path('budgets/<int:pk>/', views.BudgetDetail.as_view(), name="budget_detail"),
    path('budgets/<int:pk>/update', views.BudgetUpdate.as_view(), name="budget_update"),
    path('budgets/<int:pk>/delete', views.BudgetDelete.as_view(), name="budget_delete"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    # Expense Paths
    path('expenses/', views.ExpenseList.as_view(), name="expense_list"),
    
]