# Generated by Django 4.1.5 on 2024-01-23 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_management', '0003_studentcareer_is_registered'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='coefficient',
            field=models.IntegerField(default=1),
        ),
    ]