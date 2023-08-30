from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


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
