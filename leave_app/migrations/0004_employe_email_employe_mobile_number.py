# Generated by Django 4.1.3 on 2022-11-22 11:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('leave_app', '0003_employe_employe_created_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employe',
            name='email',
            field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employe',
            name='mobile_number',
            field=models.CharField(default=django.utils.timezone.now, max_length=15),
            preserve_default=False,
        ),
    ]
