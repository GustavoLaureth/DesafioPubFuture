# Generated by Django 4.0.1 on 2022-01-10 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desafio_pub_future', '0006_alter_balance_value_alter_expense_value_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='income',
            name='comment_char',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='income',
            name='comment_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
