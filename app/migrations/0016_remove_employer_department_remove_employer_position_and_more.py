# Generated by Django 4.2.4 on 2023-08-30 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_remove_employer_photo_small_alter_employer_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employer',
            name='department',
        ),
        migrations.RemoveField(
            model_name='employer',
            name='position',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='Employer',
        ),
        migrations.DeleteModel(
            name='Position',
        ),
    ]
