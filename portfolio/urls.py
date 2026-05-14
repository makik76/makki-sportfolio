from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('skills/', views.skills, name='skills'),
    path('works/', views.works, name='works'),
    path('projects/', views.projects, name='projects'),
    path('chartboard/', views.chartboard, name='chartboard'),
    path('contact/', views.contact, name='contact'),
]
