# Generated by Django 4.1.5 on 2024-01-18 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_management', '0015_alter_sanctionappreciation_sanction_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicyear',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='academicyear',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
