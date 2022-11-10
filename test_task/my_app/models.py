from datetime import timedelta

from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category = models.CharField(verbose_name="Категория", max_length=255)


class Transaction(models.Model):
    date = models.DateField(verbose_name="Дата транзакции")
    time = models.TimeField(verbose_name="Время транзакции")
    sum = models.DecimalField(verbose_name="Сумма", decimal_places=2, max_digits=12)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    organization = models.CharField(verbose_name="Организация", max_length=255)
    description = models.TextField()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    category = models.ManyToManyField(Category)
    transaction = models.ManyToManyField(Transaction)
    balance_profile = models.DecimalField(verbose_name="Баланс", decimal_places=2, max_digits=12, blank=True)
