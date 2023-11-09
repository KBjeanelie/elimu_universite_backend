# Generated by Django 4.1.5 on 2023-11-08 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('module_assessments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assessment',
            name='type_evaluation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='module_assessments.typeofevaluation'),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='note',
            field=models.IntegerField(default=0),
        ),
    ]
