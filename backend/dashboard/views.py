from django.shortcuts import render
from transactions.models import Transaction
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'dashboard/index.html')  


def index(request):
    transactions = Transaction.objects.filter(user=request.user)
    wallet_balance = 0
    for transaction in transactions:
        if transaction.transaction_type == "Income":
            wallet_balance += transaction.amount
        elif transaction.transaction_type == "Expense":
            wallet_balance -= transaction.amount
    print(wallet_balance)

    print(transactions)

    return render(request, 'dashboard/index.html', {'wallet_balance': wallet_balance, 'transactions' : transactions})



def add_money(request):
    return render(request, 'transactions/addmoney.html')