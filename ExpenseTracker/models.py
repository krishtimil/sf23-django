from django.db import models

# Create your models here.
CATEGORY_CHOICES = (
    ("food", "Food"),
    ("transportation", "Transportation"),
    ("clothing", "Clothing"),
    ("health", "Health"),
    ("electronics", "Electronics"),
    ("recreational", "Recreational"),
    ("utility", "Utility"),
    ("miscellaneous", "Miscellaneous"),
)
EXPENSE_TYPE_CHOICES = (
    ("personal use", "Personal Use"),
    ("bill sharing", "Bill Sharing"),
    ("family expense", "Family Expense"),
    ("lend", "Lend"),
    ("miscellaneous", "Miscellaneous"),
)

PAYMENT_CHOICES = (
    ("cash", "Cash"),
    ("credit card", "Credit Card"),
    ("online payment", "Online Payment"),
)

class ExpenseRecord(models.Model):
    amount = models.FloatField()
    date = models.DateField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    expense_type = models.CharField(max_length=20, choices=EXPENSE_TYPE_CHOICES)
    mode_of_payment = models.CharField(max_length=20, choices=PAYMENT_CHOICES)
    remarks = models.CharField(null=True, blank=True, max_length=255)
    
    def __str__(self) -> str:
        return f"{self.remarks}, Rs. {self.amount}"