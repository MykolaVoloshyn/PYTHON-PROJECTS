from django.shortcuts import redirect, render, get_object_or_404
from .forms import AccountForm, TransactionFrom
from .models import Account, Transaction


# this function will render the Home page when requested
def home(request):
    form = TransactionFrom(data=request.POST or None)

    if request.method == "POST":
        # if the form is submitted, retrieve which account the user wants to view
        pk = request.POST["account"]
        return balance(request, pk)

    content = {"form": form}

    return render(request, "checkbook/index.html", content)


# this function will render the Create New Account page when requested
def create_account(request):
    form = AccountForm(data=request.POST or None)  # retrieve the Account form

    # checks if request method is POST
    if request.method == "POST":
        if form.is_valid():
            form.save()  # saves new account
            return redirect("index")  # returns user back to the home page

    content = {"form": form}  # saves content to the template as a dictionary

    return render(request, "checkbook/CreateNewAccount.html", content)


# this function will render the Balance page when requested
def balance(request, pk):
    # retrieve the requested account using its primary key
    account = get_object_or_404(Account, pk=pk)
    # retrieve all of that account's transactions
    transactions = Transaction.Transactions.filter(account=pk)
    current_total = account.initial_deposit
    table_contents = {}

    for t in transactions:
        if t.type == "Deposit":
            current_total += t.amount
            # add transaction and total to the dictionary
            table_contents.update({t: current_total})
        else:
            current_total -= t.amount
            table_contents.update({t: current_total})

    content = {"account": account, "table_contents": table_contents, "balance": current_total}

    return render(request, "checkbook/BalanceSheet.html", content)


# this function will render the Transaction page when requested
def transaction(request):
    form = TransactionFrom(data=request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            pk = request.POST["account"]
            form.save()
            return balance(request, pk)

    content = {"form": form}

    return render(request, "checkbook/AddTransaction.html", content)
