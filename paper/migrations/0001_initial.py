# Generated by Django 4.2.7 on 2023-11-19 07:59

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('affiliation', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('account.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='FieldResearch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=300)),
                ('url_title', models.CharField(db_index=True, max_length=300)),
                ('is_active', models.BooleanField(verbose_name='Activated or Not')),
                ('is_delete', models.BooleanField(verbose_name='Deleted or Not')),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('citation', models.IntegerField(verbose_name='Citation')),
                ('DOI', models.CharField(db_index=True, max_length=360, null=True, verbose_name='DOI')),
                ('Abstract', models.TextField(db_index=True, verbose_name='Abstract')),
                ('slug', models.SlugField(blank=True, default='', max_length=200, unique=True)),
                ('is_active', models.BooleanField(default=False, verbose_name=' Activated or Not')),
                ('is_delete', models.BooleanField(verbose_name=' Deleted or Not')),
                ('author', models.ManyToManyField(related_name='Auth_paper', to='paper.author', verbose_name='Authors')),
                ('field_research', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paper_field', to='paper.fieldresearch', verbose_name='Field of Research')),
            ],
        ),
        migrations.CreateModel(
            name='PaperType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Conf', 'Conference'), ('Jour', 'Journal')], db_index=True, max_length=10)),
                ('url_type', models.CharField(db_index=True, max_length=300)),
                ('is_active', models.BooleanField(verbose_name='Activated or Not')),
                ('is_delete', models.BooleanField(verbose_name='Deleted or Not')),
            ],
        ),
        migrations.CreateModel(
            name='PaperTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(db_index=True, max_length=300)),
                ('paper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paper_tags', to='paper.paper')),
            ],
        ),
        migrations.AddField(
            model_name='paper',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paper_type', to='paper.papertype', verbose_name='Type of Paper'),
        ),
    ]
