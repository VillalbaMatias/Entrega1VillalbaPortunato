from django.urls import path
from .views import mostrar_herencia, crear_curso, crear_profesor,crear_estudiante,buscar_comision,buscar_profesor,buscar_estudiante

urlpatterns = [
    path('', mostrar_herencia),
    path('crear_curso/', crear_curso),
    path('crear_profesor/', crear_profesor),
    path('crear_estudiante/', crear_estudiante),
    path('buscar_comision/', buscar_comision), 
    path('buscar_profesor/', buscar_profesor),
    path('buscar_estudiante/', buscar_estudiante)


]

