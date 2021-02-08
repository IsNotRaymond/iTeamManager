from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect


def redirect_to_dashboard(request):
    return redirect('projetos')


urlpatterns = [
    path('', redirect_to_dashboard, name='redirect-to-dashboard'),
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include('app.urls')),
]
