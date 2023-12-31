# Generated by Django 4.2.4 on 2023-08-23 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_department_options_alter_employer_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='boss',
        ),
        migrations.RemoveField(
            model_name='department',
            name='employer',
        ),
        migrations.RemoveField(
            model_name='department',
            name='vacancy',
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
