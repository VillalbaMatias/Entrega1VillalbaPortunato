from django import forms

class CrearCursoForm (forms.Form):
    nombre = forms.CharField(max_length=40)
    comision = forms.IntegerField()


class CrearProfesorForm (forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=40)
    dni = forms.IntegerField()

class CrearEstudianteForm (forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
    dni = forms.IntegerField()
