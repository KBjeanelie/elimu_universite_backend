# Generated by Django 4.1.5 on 2024-01-17 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_management', '0014_alter_schedule_end_hours_alter_schedule_start_hours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sanctionappreciation',
            name='sanction_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
