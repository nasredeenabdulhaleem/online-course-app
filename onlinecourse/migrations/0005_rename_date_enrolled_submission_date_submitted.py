# Generated by Django 4.2.2 on 2023-07-01 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0004_submission_date_enrolled'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submission',
            old_name='date_enrolled',
            new_name='date_submitted',
        ),
    ]
