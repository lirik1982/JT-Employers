from django.db import models


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

    salary = models.IntegerField(verbose_name='Жалование')
    work_since = models.DateField(
        auto_now=False, auto_now_add=False, verbose_name='Дата трудоустройства')
    birth_date = models.DateField(
        auto_now=False, auto_now_add=False, verbose_name='Дата рождения')
    photo = models.ImageField(
        upload_to='photo/', null=True, verbose_name='Фото')
    # photo_small = models.ImageField(upload_to='photo/', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Position(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
