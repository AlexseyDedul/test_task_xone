# Generated by Django 4.1.3 on 2022-11-10 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_alter_transaction_date_alter_transaction_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateField(verbose_name='Дата транзакции'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='time',
            field=models.TimeField(verbose_name='Время транзакции'),
        ),
    ]
