# Generated by Django 4.1.3 on 2022-11-22 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave_app', '0005_alter_employe_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='employe',
            name='total_leave',
            field=models.IntegerField(default=0),
        ),
    ]
