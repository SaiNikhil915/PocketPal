from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('Expense', 'Expense'),
        ('Income', 'Income'),
    )

    TRANSACTION_CATEGORIES = (
        ('Food', 'Food'),
        ('Travel', 'Travel'),
        ('Shopping', 'Shopping'),
        ('Necessities', 'Necessities'),
        ('Entertainment', 'Entertainment'),
        ('Others', 'Others'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Replace 1 with your desired default User ID
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateField()
    category = models.CharField(max_length=20, choices=TRANSACTION_CATEGORIES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.transaction_type} - {self.amount}"
