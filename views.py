from django.shortcuts import render
from .models import Product, Order, Customer, Expense

def dashboard(request):
    total_sales = sum(order.total_price for order in Order.objects.all())
    total_expenses = sum(exp.amount for exp in Expense.objects.all())
    profit = total_sales - total_expenses

    context = {
        "products": Product.objects.count(),
        "customers": Customer.objects.count(),
        "orders": Order.objects.count(),
        "sales": total_sales,
        "expenses": total_expenses,
        "profit": profit,
    }
    return render(request, "dashboard.html", context)


def inventory(request):
    return render(request, "inventory.html", {"products": Product.objects.all()})


def customers(request):
    return render(request, "customers.html", {"customers": Customer.objects.all()})


def orders(request):
    return render(request, "orders.html", {"orders": Order.objects.all()})


def expenses(request):
    return render(request, "expenses.html", {"expenses": Expense.objects.all()})
