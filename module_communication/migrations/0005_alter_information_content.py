# Generated by Django 4.1.5 on 2024-01-15 13:15

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('module_communication', '0004_alter_event_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
