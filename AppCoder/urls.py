from django.urls import path
from AppCoder.views import ProfesoresList, curso, inicio, cursos, entregable, profesor, cursoFormulario, busquedaCamada, buscar, leerEstudiantes, estudiante, estudianteFormulario, eliminarEstudiante, editarEstudiante, ProfesorCreacion, ProfesorDetalle, ProfesorEdicion, ProfesoresList, ProfesorEliminacion

urlpatterns = [
    path('curso/', curso),
    path('cursos/', cursos, name='Cursos'),
    path('entregable/', entregable, name='Entregable'),
    path('inicio/', inicio, name='Inicio'),
    path('cursoFormulario/', cursoFormulario, name='cursoFormulario'),
    path('busquedaCamada/', busquedaCamada, name='busquedaCamada'),
    path('buscar/', buscar, name='Buscar'),    
    path('estudiante/', leerEstudiantes, name='Estudiante'),
    path('estudianteFormulario/', estudianteFormulario, name='estudianteFormulario'),
    path('eliminarEstudiante/<nombre>', eliminarEstudiante, name='eliminarEstudiante'),
    path('editarEstudiante/<nombre>', editarEstudiante, name='editarEstudiante'),
    #-----------------------------------------------------------------------------------
    path('profesor/list/', ProfesoresList.as_view(), name='profesor_listar'),
    path('profesor/<pk>', ProfesorDetalle.as_view(), name='profesor_detalle'),
    path('profesor/nuevo/', ProfesorCreacion.as_view(), name='profesor_crear'),
    path('profesor/editar/<pk>', ProfesorEdicion.as_view(), name='profesor_editar'),
    path('profesor/borrar/<pk>', ProfesorEliminacion.as_view(), name='profesor_borrar'),
]