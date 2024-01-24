# Generated by Django 4.1.5 on 2024-01-24 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module_communication', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='file',
            field=models.FileField(blank=True, upload_to='events_files/'),
        ),
        migrations.AlterField(
            model_name='event',
            name='photo',
            field=models.ImageField(blank=True, upload_to='events_image/'),
        ),
        migrations.AlterField(
            model_name='information',
            name='file',
            field=models.FileField(blank=True, upload_to='info_files'),
        ),
    ]
