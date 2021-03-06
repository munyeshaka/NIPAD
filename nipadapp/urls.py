from django.urls import path, re_path

from .import views
from .views import CutomerNumJsonView

app_name = 'nipadapp'

urlpatterns = [
    re_path(r'^$', views.home, name='home'),

    re_path(r'^propos/', views.propos, name='propos'),
    re_path(r'^regions/', views.regions, name='regions'),
    re_path(r'^program/', views.program, name='program'),
    re_path(r'^rejoindre/', views.rejoindre, name='rejoindre'),
    re_path(r'^contactes/', views.contactes, name='contactes'),
    re_path(r'^services/', views.services, name='services'),
    path('customers-json/', CutomerNumJsonView.as_view(), name='customers-json'),

]
