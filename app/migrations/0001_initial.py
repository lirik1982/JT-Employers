# Generated by Django 4.2.4 on 2023-08-17 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('age', models.IntegerField(default=18)),
                ('work_since', models.DateField()),
                ('boss', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app.employer')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.department')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.position')),
            ],
        ),
    ]
