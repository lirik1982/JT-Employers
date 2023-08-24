from django.urls import path
from .views import main, view_department

urlpatterns = [
    path('', main, name='home'),
    path('department/<int:id>', view_department, name='department'),
]
