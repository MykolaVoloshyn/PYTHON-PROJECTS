from django.db import models


TRANSACTION_TYPES = [("Deposit", "Deposit"), ("Withdrawal", "Withdrawal")]


class Account(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    initial_deposit = models.DecimalField(max_digits=15, decimal_places=2)

    # defines the model Manager for Accounts
    Accounts = models.Manager()

    # Allows references to a specific account be returned as the owner's name not the primary key
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Transaction(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.CharField(max_length=100)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    # defines the model Manager for Transaction
    Transactions = models.Manager()
