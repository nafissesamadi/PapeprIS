# Generated by Django 4.2.7 on 2023-11-21 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0008_alter_paper_doi_alter_paper_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='keywords',
            field=models.ManyToManyField(related_name='paper_tags', to='paper.papertag'),
        ),
    ]