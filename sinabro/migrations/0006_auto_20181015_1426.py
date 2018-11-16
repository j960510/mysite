# Generated by Django 2.1.1 on 2018-10-15 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sinabro', '0005_auto_20180930_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_company',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]