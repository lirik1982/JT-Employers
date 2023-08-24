from django.db import models
from django.urls import reverse
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
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Position(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class Department(MPTTModel):
    name = models.CharField(max_length=100, default='', unique=True)
    # будет применятся для автонаполнения
    # vacancy = models.IntegerField(blank=True, null=True)
    parent = TreeForeignKey(
        "self", on_delete=models.PROTECT, null=True, blank=True,
        related_name='children', db_index=True, verbose_name='Старший отдел')
    slug = models.SlugField(max_length=50, unique=True)

    staffing = models.IntegerField(default=2000)

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertetion_by = ['name']

    class Meta:
        unique_together = [['parent', 'slug']]
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

    def get_absolute_url(self):
        return reverse("employer_by_department", args=[str(self.slug)])
