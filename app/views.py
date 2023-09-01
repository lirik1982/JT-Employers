from django.shortcuts import render, redirect
from django.db.models import Q
from departments.models import Department
from employers.models import Employer


def main(request):
    if not request.user.is_authenticated:
        print('redirect')
        return redirect('login')

    departments = Department.objects.all()
    context = {'departments': departments}
    return render(request, 'index.html', context)


def SearchView(request):
    departments = Department.objects.all()
    order_by = request.GET.get('order_by', 'id')

    if request.method == "GET":
        search = request.GET['query']

        employers = Employer.objects.filter(
            Q(name__icontains=search) |
            Q(department__fullname__icontains=search) |
            Q(position__name__icontains=search) |
            Q(salary__icontains=search) |
            Q(work_since__icontains=search) |
            Q(birth_date__icontains=search)
        ).order_by(order_by)

        return render(request, 'includes/search_result.html', locals())
    else:
        return render(request, 'includes/search_result.html', locals())
