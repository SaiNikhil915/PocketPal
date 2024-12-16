from django.urls import path
from . import views

urlpatterns = [
    path('addmoney/', views.add_money, name='add_money'),
    path('delete_transaction/<pk>', views.delete_transaction, name='delete_transaction'),
    path('edit_transaction/<pk>', views.edit_transaction, name='edit_transaction')
]