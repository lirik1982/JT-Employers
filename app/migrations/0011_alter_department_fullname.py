# Generated by Django 4.2.4 on 2023-08-27 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_department_name_department_fullname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='fullname',
            field=models.CharField(default='', max_length=100, verbose_name='Название отдела'),
        ),
    ]
