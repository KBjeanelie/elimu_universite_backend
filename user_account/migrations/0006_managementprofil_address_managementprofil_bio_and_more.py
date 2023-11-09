# Generated by Django 4.1.5 on 2023-11-08 09:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0005_managementprofil_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='managementprofil',
            name='address',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='managementprofil',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='managementprofil',
            name='email',
            field=models.CharField(blank=True, max_length=120, unique=True),
        ),
        migrations.AddField(
            model_name='managementprofil',
            name='firstname',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='managementprofil',
            name='lastname',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='managementprofil',
            name='tel',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='managementprofil',
            name='user_account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
