from django.urls import path
from . import views


urlpatterns = [
    # sets the url to home page index.html
    path("", views.home, name="index"),
    # sets the url to Create New Account page CreateNewAccount.html
    path("create/", views.create_account, name="create"),
    # sets the url to Balance Sheet page BalanceSheet.html
    path("balance/<int:pk>/", views.balance, name="balance"),
    # sets the url to Add New Transaction page AddNewTransaction.html
    path("transaction/", views.transaction, name="transaction"),
]
