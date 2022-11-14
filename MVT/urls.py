"""MVT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from MiApp import views


urlpatterns = [
    path('', views.mostrar_herencia, name='Home'),
    re_path('crear_curso/',views.crear_curso, name='CrearCurso'),
    re_path('crear_profesor/',views.crear_profesor, name='CrearProfesor'),
    re_path('crear_estudiante/',views.crear_estudiante, name='CrearEstudiante'),
    re_path('buscar_comision/',views.buscar_comision, name='BuscarComision'),
    re_path('buscar_profesor/',views.buscar_profesor, name='BuscarProfesor'),
    re_path('buscar_estudiante/',views.buscar_estudiante, name='BuscarEstudiante'),
    re_path('admin/',admin.site.urls)
]
