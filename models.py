from django.db import models

# Product inventory
class Product(models.Model):
    CATEGORY_CHOICES = [
        ('T-Shirt', 'T-Shirt'),
        ('Sweatpants', 'Sweatpants'),
        ('Jumper', 'Jumper'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    size = models.CharField(max_length=10)
    color = models.CharField(max_length=20)
    stock = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.size}, {self.color})"


# Customer database
class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Orders
class Order(models.Model):
    BRANDING_CHOICES = [
        ('Heat Press', 'Heat Press'),
        ('Embroidery', 'Embroidery'),
        ('None', 'None'),
    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    branding_type = models.CharField(max_length=20, choices=BRANDING_CHOICES)
    status = models.CharField(max_length=20, default="Pending")
    order_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Auto-calc total
        self.total_price = self.product.price * self.quantity
        super().save(*args, **kwargs)


# Expenses
class Expense(models.Model):
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.description} - {self.amount}"
