from django.urls import path, include
from .views import main, SearchView


urlpatterns = [
    path('', main, name='home'),
    path('department/', include('departments.urls')),
    path('employer/', include('employers.urls')),
    path('search/', SearchView, name='search')
]
