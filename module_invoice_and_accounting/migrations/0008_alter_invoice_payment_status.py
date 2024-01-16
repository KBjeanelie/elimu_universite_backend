# Generated by Django 4.1.5 on 2024-01-16 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module_invoice_and_accounting', '0007_alter_invoice_payment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='payment_status',
            field=models.CharField(blank=True, choices=[('Entièrement payé', 'Entièrement payé'), ('Non payé', 'Non payé'), ('Avance', 'Avance')], max_length=20),
        ),
    ]
