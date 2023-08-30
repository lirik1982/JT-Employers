from django.urls import path
from .views import main, view_department, ViewEmployer, ViewEmployersList

urlpatterns = [
    path('', main, name='home'),
    path('department/<int:id>', view_department.as_view(), name='department'),
    path('employer/<int:id>', ViewEmployer.as_view(), name='employer'),
    path('employerslist/<int:id>',
         ViewEmployersList.as_view(), name='employerslist')
]
