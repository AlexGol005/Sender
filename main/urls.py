from django.urls import path

from . import views


urlpatterns = [
    path('', views.Main.as_view(), name='main'),
    path('about/', views.About.as_view(), name='about'),
      ]
