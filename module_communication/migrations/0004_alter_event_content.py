# Generated by Django 5.0 on 2024-01-05 09:34

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('module_communication', '0003_alter_eventparticipate_end_hours_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]