# Generated by Django 4.2.7 on 2023-11-20 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email_active_code',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]