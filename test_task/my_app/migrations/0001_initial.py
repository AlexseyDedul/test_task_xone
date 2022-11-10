# Generated by Django 4.1.3 on 2022-11-10 13:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255, verbose_name='Категория')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата транзакции')),
                ('time', models.TimeField(auto_now_add=True, verbose_name='Время транзакции')),
                ('sum', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Сумма')),
                ('organization', models.CharField(max_length=255, verbose_name='Организация')),
                ('description', models.TextField()),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='my_app.category', verbose_name='Категория')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance_profile', models.DecimalField(blank=True, decimal_places=2, max_digits=12, verbose_name='Баланс')),
                ('category', models.ManyToManyField(to='my_app.category')),
                ('transaction', models.ManyToManyField(to='my_app.transaction')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
