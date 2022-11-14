from django.shortcuts import render
from .models import Curso, Profesor, Estudiante
from .forms import CrearCursoForm, CrearProfesorForm, CrearEstudianteForm
#from .forms import

# Create your views here.

#def mostrar_index(request):
#   return render(request,'index.html')

def mostrar_herencia(request):
    return render(request,'herencia.html')


def crear_curso(request): #Este se encarga de enviar los datos del formulario para que sean cargados

    if request.method == 'POST':#Se hace el metodo POST que es el encargado de enviar los datos

        formulario = CrearCursoForm(request.POST) #Se crea el objeto formulario que es el que va a almacenar los datos que se van a crear

        if formulario.is_valid(): #Django valida con .is_valid si los datos ingresados en el form son validos

            formulario_limpio = formulario.cleaned_data #.cleaned_data se encarga poner los campos en blanco

            #Se crea el objeto curso, que va a contener el nombre y comision que van a venir de formulario_limpio
            #ya que son los datos que fueron ingresados por el formulario
            curso = Curso (nombre = formulario_limpio['nombre'], comision = formulario_limpio['comision'])

            curso.save() #Se guardan los datos
            
            return render (request,'index.html')#Se renderiza index.html para volver al home
    
    else:
        #Cuando estamos en Home, y hacemos click en el boton crear curso
        #Va a pasar por este else y lo que va a hacer es instanciarse  esta variable, para luego ser utilizada
        formulario = CrearCursoForm()

    return render(request, 'crear_curso.html', {'formulario':formulario})


def crear_profesor(request):

    if request.method == 'POST':#Se hace el metodo POST que es el encargado de enviar los datos

        formulario = CrearProfesorForm(request.POST) #Se crea el objeto formulario que es el que va a almacenar los datos que se van a crear

        if formulario.is_valid(): #Django valida con .is_valid si los datos ingresados en el form son validos

            formulario_limpio = formulario.cleaned_data #.cleaned_data se encarga poner los campos en blanco

            #Se crea el objeto curso, que va a contener el nombre y comision que van a venir de formulario_limpio
            #ya que son los datos que fueron ingresados por el formulario
            profesor = Profesor (nombre = formulario_limpio['nombre'], apellido = formulario_limpio['apellido'], 
            email = formulario_limpio['email'], profesion = formulario_limpio['profesion'], dni = formulario_limpio['dni'])

            profesor.save() #Se guardan los datos
            
            return render (request,'index.html')#Se renderiza index.html para volver al home
    
    else:
        #Cuando estamos en Home, y hacemos click en el boton crear curso
        #Va a pasar por este else y lo que va a hacer es instanciarse  esta variable, para luego ser utilizada
        formulario = CrearProfesorForm()

    return render(request, 'crear_profesor.html', {'formulario':formulario})



def crear_estudiante(request):

    if request.method == 'POST':#Se hace el metodo POST que es el encargado de enviar los datos

        formulario = CrearEstudianteForm(request.POST) #Se crea el objeto formulario que es el que va a almacenar los datos que se van a crear

        if formulario.is_valid(): #Django valida con .is_valid si los datos ingresados en el form son validos

            formulario_limpio = formulario.cleaned_data #.cleaned_data se encarga poner los campos en blanco

            #Se crea el objeto curso, que va a contener el nombre y comision que van a venir de formulario_limpio
            #ya que son los datos que fueron ingresados por el formulario
            estudiante = Estudiante (nombre = formulario_limpio['nombre'], apellido = formulario_limpio['apellido'], 
            email = formulario_limpio['email'], dni = formulario_limpio['dni'])

            estudiante.save() #Se guardan los datos
            
            return render (request,'index.html')#Se renderiza index.html para volver al home
    
    else:
        #Cuando estamos en Home, y hacemos click en el boton crear curso
        #Va a pasar por este else y lo que va a hacer es instanciarse  esta variable, para luego ser utilizada
        formulario = CrearEstudianteForm()

    return render(request, 'crear_estudiante.html', {'formulario':formulario})


def buscar_comision (request):

    if request.GET.get('comision', False):
        comision = request.GET['comision']
        cursos = Curso.objects.filter(comision__icontains=comision)

        return render(request, 'buscar_comision.html', {'cursos':cursos})

    else:
        respuesta = 'No hay datos'

    return render(request, 'buscar_comision.html', {'respuesta':respuesta})


def buscar_profesor (request):

    if request.GET.get('apellido', False):
        apellido = request.GET['apellido']
        profesores = Profesor.objects.filter(apellido__icontains=apellido)

        return render(request, 'buscar_profesor.html', {'profesores':profesores})

    else:
        respuesta = 'No hay datos'

    return render(request, 'buscar_profesor.html', {'respuesta':respuesta})


def buscar_estudiante (request):

    if request.GET.get('apellido', False):
        apellido = request.GET['apellido']
        estudiantes = Estudiante.objects.filter(apellido__icontains=apellido)

        return render(request, 'buscar_estudiante.html', {'estudiantes':estudiantes})

    else:
        respuesta = 'No hay datos'

    return render(request, 'buscar_estudiante.html', {'respuesta':respuesta})