from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from employers.models import Employer, Position
from departments.models import Department
from employers.forms import EmployerForm

from django.views import View
from faker import Faker
from random import randint
from dateutil.relativedelta import relativedelta
from datetime import datetime
from datetime import date

# Create your views here.


def fakedate():
    return str(date(randint(2000, 2023), randint(1, 12), randint(1, 28)))


def create_employer(department, position):
    fake = Faker(locale="ru_RU")
    employer = Employer()
    employer.name = fake.name()
    employer.salary = randint(3, 8) * 10000
    employer.department = department
    employer.work_since = datetime.fromisoformat(fakedate())
    employer.birth_date = datetime.date(
        employer.work_since + relativedelta(
            years=-randint(20, 35),
            month=randint(1, 12),
            days=-randint(1, 30))
    )
    employer.position = position
    employer.save()


def create_boss(department):
    try:
        position = Position.objects.get(id=9999)
    except Position.DoesNotExist:
        position = Position()
        position.id = 9999
        position.name = "Начальник"
        position.save()
    create_employer(department=department, position=position)


def seed(request, id) -> bool:
    department_edit = get_object_or_404(Department, pk=id)
    pos_col = len(Position.objects.all()) - 1
    for _ in range(department_edit.staffing):
        create_employer(department_edit, get_object_or_404(
            Position, id=randint(1, pos_col)))
    create_boss(department_edit)
    messages.success(
        request, 'Изменения сохранены')
    return True


def clear_employers(request, id) -> bool:
    department_edit = get_object_or_404(Department, pk=id)
    Employer.objects.filter(department=department_edit).delete()
    messages.success(
        request, 'Удалены записи о сотрудниках')

    return True


class ViewEmployer(View):
    def get(self, request, id):
        departments = Department.objects.all()
        employer = get_object_or_404(Employer, pk=id)
        department = get_object_or_404(Department, employer=employer)
        form = EmployerForm(instance=employer)
        try:
            boss = Employer.objects.get(
                department=department, position_id=9999)
        except Employer.DoesNotExist:
            boss = None
        return render(request, 'includes/employer.html', locals())

    def post(self, request, id):
        form = EmployerForm(request.POST)
        if form.is_valid():
            if "save_changes" in request.POST:
                employer = get_object_or_404(Employer, pk=id)
                employer.name = form.cleaned_data['name']

                employer_new_position = get_object_or_404(
                    Position, name=form.cleaned_data['position'])

                department = get_object_or_404(
                    Department, fullname=form.cleaned_data['department']
                )

                try:
                    boss = Employer.objects.get(
                        department=department, position_id=9999)
                except Employer.DoesNotExist:
                    boss = None
                if boss and employer_new_position.id == 9999 and \
                        employer.position != employer_new_position:
                    messages.error(request, 'Позиция начальника занята')
                    return redirect(request.META.get('HTTP_REFERER'))

                employer.position = employer_new_position
                employer.department = department
                employer.work_since = form.cleaned_data['work_since']
                employer.birth_date = form.cleaned_data['birth_date']
                employer.save()
                messages.success(
                    request, 'Изменения сохранены')
                return redirect(request.META.get('HTTP_REFERER'))

            if "move" in request.POST:
                try:
                    departmnet = Department.objects.get(id=8888)
                except Department.DoesNotExist:
                    departmnet = Department()
                    departmnet.id = 8888
                    departmnet.fullname = "Резерв"
                    departmnet.parent = None
                    departmnet.save()
                    messages.success(
                        request, 'Создан отдел - Резерв')

                employer = get_object_or_404(Employer, pk=id)
                employer.department = departmnet
                employer.save()
                messages.success(
                    request, 'Изменения сохранены')

        return redirect('home')


class ViewEmployersList(View):
    def get(self, request, id):
        order_by = request.GET.get('order_by', 'id')
        # Model.objects.all().order_by(order_by)
        departments = Department.objects.all()
        department = get_object_or_404(Department, pk=id)
        employers = Employer.objects.filter(
            department=department).all().order_by(order_by)
        try:
            boss = Employer.objects.get(
                department=department, position_id=9999)
        except Employer.DoesNotExist:
            boss = None

        return render(request, 'includes/employers_list.html', locals())
