from django.shortcuts import render
from departments.models import Department


def main(request):
    departments = Department.objects.all()
    context = {'departments': departments}
    return render(request, 'index.html', context)


def SearchView(request):

    return render(request, 'search_result.html', locals())
