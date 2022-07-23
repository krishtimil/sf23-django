# Generated by Django 4.0.6 on 2022-07-20 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenseRecords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('date', models.DateField()),
                ('category', models.CharField(choices=[('food', 'Food'), ('transportation', 'Transportation'), ('clothing', 'Clothing'), ('health', 'Health'), ('electronics', 'Electronics'), ('recreational', 'Recreational'), ('utility', 'Utility'), ('miscellaneous', 'Miscellaneous')], max_length=20)),
                ('expense_type', models.CharField(choices=[('personal use', 'Personal Use'), ('bill sharing', 'Bill Sharing'), ('family expense', 'Family Expense'), ('lend', 'Lend'), ('miscellaneous', 'Miscellaneous')], max_length=20)),
                ('mode_of_payment', models.CharField(choices=[('cash', 'Cash'), ('credit card', 'Credit Card'), ('online payment', 'Online Payment')], max_length=20)),
                ('remarks', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
