from django.urls import path
from api.views import lista_de_hidrometricas, detalles_de_hidrometricas


urlpatterns = [
    path('hidrometricas', lista_de_hidrometricas), # www.miurl.com/todos-los-autos/
    path('detalles-de-hidrometricas/<str:pk>', detalles_de_hidrometricas) # www.miurl.com/todos-los-autos/
]