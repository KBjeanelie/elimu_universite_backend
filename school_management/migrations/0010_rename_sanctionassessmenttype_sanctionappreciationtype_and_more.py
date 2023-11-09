# Generated by Django 4.1.5 on 2023-11-08 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0007_managementprofil_city_managementprofil_sex'),
        ('school_management', '0009_schedule'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SanctionAssessmentType',
            new_name='SanctionAppreciationType',
        ),
        migrations.CreateModel(
            name='SanctionAppreciation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True)),
                ('sanction_date', models.DateField()),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school_management.career')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_account.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_management.subject')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_management.sanctionappreciationtype')),
            ],
        ),
    ]
