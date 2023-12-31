# Generated by Django 4.2.4 on 2023-08-23 15:17

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_department_boss_remove_department_employer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='boss',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='boss', to='app.employer', verbose_name='Руководитель отдела'),
        ),
        migrations.AddField(
            model_name='department',
            name='employer',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='employers', to='app.employer', verbose_name='Штатный сотрудник'),
        ),
    ]
