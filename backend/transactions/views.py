from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Sum, Case, When, F
from .models import Transaction


def calculate_wallet_balance(user):
    """
    Helper function to calculate the wallet balance for a user.
    """
    transactions = Transaction.objects.filter(user=user).aggregate(
        income=Sum(Case(When(transaction_type="Income", then=F('amount')))),
        expense=Sum(Case(When(transaction_type="Expense", then=F('amount'))))
    )
    income = transactions['income'] or 0  # Default to 0 if None
    expense = transactions['expense'] or 0  # Default to 0 if None
    return income - expense


@login_required
def add_money(request):
    if request.method == 'POST':
        transaction_type = request.POST.get('transaction_type')
        amount = request.POST.get('amount')
        transaction_date = request.POST.get('transaction_date')
        category = request.POST.get('category')

        # Save the transaction
        transaction = Transaction(
            user=request.user,
            transaction_type=transaction_type,
            amount=float(amount),
            transaction_date=transaction_date,
            category=category
        )
        transaction.save()

        # Redirect to index page
        return redirect('index')

    return render(request, 'transactions/addmoney.html')


@login_required
def delete_transaction(request, pk):
    transaction = Transaction.objects.get(pk=pk)
    transaction.delete()
    return redirect('/dashboard/')

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Transaction
from django.http import HttpResponse

@login_required
def edit_transaction(request, pk):
    transaction = get_object_or_404(Transaction, id=pk, user=request.user)

    if request.method == "POST":
        # Get form data
        transaction.transaction_type = request.POST.get('transaction_type')
        transaction.amount = request.POST.get('amount')
        transaction.transaction_date = request.POST.get('transaction_date')
        transaction.category = request.POST.get('category')

        transaction.save()

        return redirect('/dashboard/')  # Redirect to the transaction list view

    return render(request, 'transactions/expense_edit.html', {'transaction': transaction})
