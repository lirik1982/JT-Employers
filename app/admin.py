from django.contrib import admin
# from .models import Employer, Department, Position
from employers.models import Employer, Position
from departments.models import Department

from mptt.admin import MPTTModelAdmin


class EmployerAdmin(admin.ModelAdmin):
    pass


class PositionAdmin(admin.ModelAdmin):
    pass


class DepartmentAdmin(MPTTModelAdmin):
    mptt_level_indent = 20


admin.site.register(Employer, EmployerAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Department, DepartmentAdmin)
