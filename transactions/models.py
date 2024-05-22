from django.db import models
from accounts.models import CustomUser

# Create your models here.

class Transaction(models.Model):
    sender = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, related_name='receiver')
    Currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='currency')
    amount = models.IntegerField(default=0)
    transaction_date = models.DateTimeField(auto_now_add=True)
    transaction_status = models.CharField(max_length=30, default='pending')
    Payment_method = models.ForeignKey('PaymentMethod', on_delete=models.CASCADE, related_name='payment_method')


class Currency(models.Model):
    CURRENCY_CHOICES = [
        ('USD', 'US Dollar'),
        ('EUR', 'Euro'),
        ('GBP', 'British Pound'),
        ('ZAR', 'South African Rand'),
        ('ZiG', 'ZigCoin'),
    ]
    currency_code = models.CharField(max_length=3, choices=CURRENCY_CHOICES, unique=True)


class PaymentMethod(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('card', 'Credit Card'),
        ('bank', 'Bank Transfer'),
        ('cash', 'Cash Pickup')
    ]
    payment_method = models.CharField(max_length=30, choices=PAYMENT_METHOD_CHOICES, unique=True)
    description = models.CharField(max_length=30)


class TransactionHistory(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name='transaction')
    