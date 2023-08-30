from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Avg

from employers.models import Employer
from departments.models import Department
from departments.forms import DepartmentForm

from django.views import View
from datetime import date
from employers.views import clear_employers, seed


def main(request):
    departments = Department.objects.all()
    context = {'departments': departments}
    return render(request, 'index.html', context)


def calculate_age(born):
    today = date.today()
    return today.year - born.year - \
        ((today.month, today.day) < (born.month, born.day))


class ViewDepartment(View):
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
