from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.


class Employer(models.Model):
    name = models.CharField(max_length=200, verbose_name='ФИО сотрудника')

    position = models.ForeignKey(
        'Position', on_delete=models.PROTECT, verbose_name='Должность',
        blank=True, null=True
    )

    department = models.ForeignKey(
        'Department', on_delete=models.PROTECT, verbose_name='Отдел',
        blank=True, null=True
    )

    salary = models.IntegerField()
    work_since = models.DateField(auto_now=False, auto_now_add=False)
    birth_date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Position(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Department(MPTTModel):
    fullname = models.CharField(max_length=100, default='',
                                verbose_name="Название отдела")
    parent = TreeForeignKey(
        "self", on_delete=models.PROTECT, null=True, blank=True,
        related_name='children', db_index=True, verbose_name='Старший отдел')

    staffing = models.IntegerField(
        default=2000, verbose_name='Штатная численность')

    def __str__(self):
        return self.fullname

    class MPTTMeta:
        order_insertetion_by = ['fullname']

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'
