from django.urls import path
from .views import ViewEmployer, ViewEmployersList


urlpatterns = [
    path('<int:id>', ViewEmployer.as_view(), name="employer"),
    path('list/<int:id>', ViewEmployersList.as_view(), name="employerslist"),
]
