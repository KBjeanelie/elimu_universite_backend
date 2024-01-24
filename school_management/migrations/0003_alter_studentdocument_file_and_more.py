# Generated by Django 4.1.5 on 2024-01-24 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_management', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdocument',
            name='file',
            field=models.FileField(upload_to='student_documents'),
        ),
        migrations.AlterField(
            model_name='teacherdocument',
            name='file',
            field=models.FileField(upload_to='teacher_documents'),
        ),
    ]
