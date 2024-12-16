from datetime import timedelta, date
from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from transactions.models import Transaction


def weekly_report(request):
    return render(request, "reports/weekly.html")

def monthly_report(request):
    return render(request, "reports/monthly.html")

def yearly_report(request):
    return render(request, "reports/yearly.html")

def history(request):
    return render(request, 'reports/history.html')


@login_required
def weekly_report(request):
    # Get the current user
    user = request.user
    
    # Determine the start and end dates of the current week
    today = date.today()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)

    # Fetch all transactions of the current week for the user
    weekly_transactions = Transaction.objects.filter(
        user=user,
        transaction_date__range=[start_of_week, end_of_week],
        transaction_type="Expense"  # Only analyzing expenses
    )
    
    # Calculate daily expenses
    daily_expenses = [0] * 7  # 7 days of the week
    for transaction in weekly_transactions:
        day_index = (transaction.transaction_date - start_of_week).days
        daily_expenses[day_index] += float(transaction.amount)

    # Calculate total weekly expense and average
    total_weekly_expense = sum(daily_expenses)
    weekly_average = total_weekly_expense / 7 if daily_expenses else 0

    # Determine the highest spending day
    max_expense = max(daily_expenses)
    highest_day_index = daily_expenses.index(max_expense) if max_expense > 0 else None
    highest_day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][highest_day_index] if highest_day_index is not None else "N/A"

    # Pass the data to the template
    context = {
        'weekly_expense_data': daily_expenses,
        'weekly_expense_labels': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
        'total_weekly_expense': total_weekly_expense,
        'weekly_average': weekly_average,
        'highest_day': highest_day,
        'max_expense': max_expense,
    }
    return render(request, 'reports/weekly.html', context)



def monthly_expenses(request):
    # Get the current date
    today = timezone.now().date()

    # Get the first and last day of the current month
    first_day_of_month = today.replace(day=1)
    last_day_of_month = today.replace(day=28) + timedelta(days=4)  # This will give us the next month
    last_day_of_month = last_day_of_month - timedelta(days=last_day_of_month.day)

    # Fetch transactions of the current month
    transactions = Transaction.objects.filter(
        transaction_date__gte=first_day_of_month,
        transaction_date__lte=last_day_of_month,
        transaction_type='Expense'  # Only consider Expenses
    )

    # Calculate weekly expenses
    weekly_expenses = [0] * 4  # Array to store expenses for each week
    for transaction in transactions:
        # Calculate the week number
        week_number = (transaction.transaction_date.day - 1) // 7
        weekly_expenses[week_number] += transaction.amount

    # Calculate total, average, and highest week
    total_expense = sum(weekly_expenses)
    average_expense = total_expense / len(weekly_expenses) if len(weekly_expenses) > 0 else 0
    highest_week_expense = max(weekly_expenses)

    # Projected yearly expense
    projected_yearly_expense = average_expense * 12

    # Prepare the data for rendering
    context = {
        'weekly_expenses': weekly_expenses,
        'total_expense': total_expense,
        'average_expense': average_expense,
        'highest_week_expense': highest_week_expense,
        'projected_yearly_expense': projected_yearly_expense,
        'monthly_expense_data': weekly_expenses,  # For the chart data
    }

    return render(request, 'reports/monthly.html', context)
