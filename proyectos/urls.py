from listadoApp.views import (agregarProyecto, index, listadoProyectos, eliminarProyecto, actualizarProyecto)
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('proyectos/', listadoProyectos),
    path('agregarProyecto/', agregarProyecto),
    path('eliminarProyecto/<int:id>', eliminarProyecto),
    path('actualizarProyecto/<int:id>', actualizarProyecto),

]
