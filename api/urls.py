from django.urls import path
from api.views import lista_de_autos, detalles_del_auto


urlpatterns = [
    path('todos-los-autos', lista_de_autos), # www.miurl.com/todos-los-autos/
    path('detalles-del-auto/<str:pk>', detalles_del_auto) # www.miurl.com/todos-los-autos/
]