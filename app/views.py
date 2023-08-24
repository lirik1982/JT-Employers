from django.shortcuts import render, get_object_or_404, HttpResponseRedirect

from .models import Department

from .forms import DepartmnentForm
# Create your views here.


def main(request):
    department = Department.objects.all()
    context = {'department': department}
    return render(request, 'index.html', context)


def view_department(request, id):

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DepartmnentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DepartmnentForm()
        department = Department.objects.all()
        department_edit = get_object_or_404(Department, pk=id)
        context = {
            'department': department,
            'department_edit': department_edit,
            'form': form
        }
    return render(request, 'includes/department.html', context)
