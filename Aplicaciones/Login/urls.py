from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # ✅ Ruta para cargar index.html
    path('agregar_usuario/', views.agregar_usuario, name='agregar_usuario'),  # ✅ Ruta correcta
    path('error/', views.error_usuario, name='error_usuario'),
]