# Generated by Django 4.2.4 on 2023-08-09 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='record',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='record',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]
