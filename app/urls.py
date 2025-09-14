# nc_tutorials/urls.py
from . import views
from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    # path('', views.home, name='home'),
    # # path('admin/', admin.site.urls),
    # path('tutorials/', include('tutorials.urls')),
    # path('users/', include('users.urls')),

    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # <-- root URL
    path('tutorials/', include('tutorials.urls')),
]

