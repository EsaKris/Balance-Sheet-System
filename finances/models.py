from django.db import models

# Create your models here.
class BalanceSheet(models.Model):
    month = models.CharField(max_length=20)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.month} {self.year}"
    
class Entry(models.Model):
    balance_sheet = models.ForeignKey(BalanceSheet, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_time = models.DateTimeField(auto_now_add=True)
    is_income = models.BooleanField(default=True)

    def __str__(self) :
        return f"{self.description} - {self.amount}"
    

