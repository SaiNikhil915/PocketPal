from django.urls import path
from . import views

urlpatterns = [
    # path('dashboard/', views.index, name='index'),
    path('addmoney/', views.add_money, name='add_money'),
    # path('api/wallet-balance/', views.wallet_balance, name='wallet_balance'),
    # path('wallet-balance/', views.wallet_balance, name='wallet_balance'),
    # path('', views.index, name='index'),
    path('delete_transaction/<pk>', views.delete_transaction, name='delete_transaction'),
    path('edit_transaction/<pk>', views.edit_transaction, name='edit_transaction')

]