from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from api.models import Auto
from api.serializers import AutoSerializer


@csrf_exempt
def lista_de_autos(request):
    """Listado, creación de nuevos autos"""
    if request.method == 'GET':
        autos = Auto.objects.all()
        serializer = AutoSerializer(autos, many=True)
        return JsonResponse(serializer.data, safe=False)
      
    elif request.method == 'POST':
        data_parseado = JSONParser().parse(request)
        serializer = AutoSerializer(data=data_parseado)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def detalles_del_auto(request, pk):
    try:
        auto = Auto.objects.get(id=pk)
    except Auto.DoesNotExist:
        return JsonResponse(status=404)
    
    if request.method == 'GET':
        serializer = AutoSerializer(auto)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AutoSerializer(auto, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        auto.delete()
        return JsonResponse({"id": auto.id}, status=204) # NO CONTENT
    