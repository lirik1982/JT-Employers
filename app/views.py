from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Avg

from .models import Department, Employer, Position
from .forms import DepartmentForm
from django.views import View
from faker import Faker
from random import randint
from dateutil.relativedelta import relativedelta
from datetime import datetime
from datetime import date


def calculate_age(born):
    today = date.today()
    return today.year - born.year - \
        ((today.month, today.day) < (born.month, born.day))


def main(request):
    departments = Department.objects.all()
    context = {'departments': departments}
    return render(request, 'index.html', context)


class view_department(View):
    def get(self, request, id):
        departments = Department.objects.all()
        department_edit = get_object_or_404(Department, pk=id)
        form = DepartmentForm(instance=department_edit)
        employers_count = Employer.objects.filter(
            department=department_edit).count()

        employers = Employer.objects.all()
        avg_age = 0
        for employer in employers:
            avg_age += calculate_age(employer.birth_date)
        if len(employers) > 0:
            avg_age = int(avg_age/len(employers))

        try:
            boss = Employer.objects.get(
                department=department_edit, position_id=9999)
        except Employer.DoesNotExist:
            boss = None

        mid_salary_dict = Employer.objects.filter(
            department=department_edit).aggregate(mid_salary=Avg('salary'))
        if mid_salary_dict['mid_salary']:
            mid_salary = int(mid_salary_dict['mid_salary'])
        else:
            mid_salary = '-'
        return render(request, 'includes/department.html', locals())

    def post(self, request, id):
        form = DepartmentForm(request.POST)

        if form.is_valid():
            if "save_changes" in request.POST:
                department_edit = get_object_or_404(Department, pk=id)
                department_edit.fullname = form.cleaned_data['fullname']
                department_edit.staffing = form.cleaned_data['staffing']
                select = get_object_or_404(
                    Department, fullname=form.cleaned_data['parent'])
                department_edit.parent = select
                department_edit.save()
                messages.success(
                    request, 'Изменения сохранены')
                return redirect(request.META.get('HTTP_REFERER'))

            if "seed" in request.POST:
                clear_employers(request, id=id)
                seed(request, id=id)
                return redirect(request.META.get('HTTP_REFERER'))

            if "clear" in request.POST:
                clear_employers(request, id=id)
                return redirect(request.META.get('HTTP_REFERER'))

        return redirect('home')


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
