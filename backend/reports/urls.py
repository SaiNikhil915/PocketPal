from django.urls import path
from . import views

urlpatterns = [
    path("weekly/", views.weekly_report, name="weekly"),
    path("monthly/", views.monthly_report, name="monthly"),
    path("yearly/", views.yearly_report, name="yearly"),

    path('weekly/', views.weekly_report, name='weekly_report'),
    path('monthly/', views.monthly_expenses, name='monthly_expenses'),
    path('history/', views.history, name='history'),
    path('output/', views.output, name='output'),
]

