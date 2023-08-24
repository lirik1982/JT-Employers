from typing import Any, Optional
from django.core.management.base import BaseCommand

from app.models import Department, Employer, Position


departsments = [
    ['Отдел разработки №1', 15000],
    ['Отдел разработки №2', 4000],
    ['Отдел разработки №3', 3000],
    ['Отдел разработки №4', 2000],
    ['Отдел разработки №5', 1000],
    ['Отдел разработки №6', 500],
    ['Отдел разработки №7', 100],
    ['Отдел разработки №8', 10],

    ['Отдел тестирования №1', 15000],
    ['Отдел тестирования №2', 4000],
    ['Отдел тестирования №3', 3000],
    ['Отдел тестирования №4', 2000],
    ['Отдел тестирования №5', 1000],
    ['Отдел тестирования №6', 500],
    ['Отдел продаж', 10000],
    ['Отдел маркетинга', 2000],
    ['Отдел кадров', 50],
    ['Бухгалтерия', 50],
    ['Отдел снабжения', 100],
    ['Отдел логистики', 50],
    ['Канцелярия', 30]
]


class Command(BaseCommand):

    help = 'Seeds the database whith initial data'

    def handle(self, *args: Any, **options: Any):

        Department.objects.create('Отдел разработки')
        Department.objects.create('Отдел продаж')
        Department.objects.create('Отдел разработки')
        Department.objects.create('Отдел разработки')
        Department.objects.create('Отдел разработки')
        Department.objects.create('Отдел разработки')
        Department.objects.create('Отдел разработки')

        pass
