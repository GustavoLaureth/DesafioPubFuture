# Generated by Django 4.0.1 on 2022-01-10 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('desafio_pub_future', '0007_income_comment_char_income_comment_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='income',
            old_name='comment_text',
            new_name='comment',
        ),
        migrations.RemoveField(
            model_name='income',
            name='comment_char',
        ),
    ]
