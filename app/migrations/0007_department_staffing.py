# Generated by Django 4.2.4 on 2023-08-24 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_rename_depend_on_department_parent_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='staffing',
            field=models.IntegerField(default=2000),
        ),
    ]
