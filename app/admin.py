from django.contrib import admin
from .models import Employer, Department, Position

from mptt.admin import MPTTModelAdmin

# Register your models here.


class EmployerAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class PositionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class DepartmentAdmin(MPTTModelAdmin):
    mptt_level_indent = 20
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Employer, EmployerAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Department, DepartmentAdmin)
