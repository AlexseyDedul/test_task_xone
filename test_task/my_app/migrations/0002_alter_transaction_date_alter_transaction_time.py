# Generated by Django 4.1.3 on 2022-11-10 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateField(auto_now=True, verbose_name='Дата транзакции'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='time',
            field=models.TimeField(auto_now=True, verbose_name='Время транзакции'),
        ),
    ]
