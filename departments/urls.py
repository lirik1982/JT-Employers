from django.urls import path
from .views import ViewDepartment

urlpatterns = [
    path('<int:id>', ViewDepartment.as_view(), name='department'),
]
