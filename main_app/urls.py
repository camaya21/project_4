from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('budgets/', views.BudgetList.as_view(), name="budget_list"),
    path('bugdets/new/', views.BudgetCreate.as_view(), name="budget_create"),
    path('budgets/<int:pk>/', views.BudgetDetail.as_view(), name="budget_detail"),
    path('budgets/<int:pk>/update', views.BudgetUpdate.as_view(), name="budget_update"),
    path('budgets/<int:pk>/delete', views.BudgetDelete.as_view(), name="budget_delete"),
]