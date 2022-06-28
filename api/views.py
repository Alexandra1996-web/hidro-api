from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from api.models import Hidrometrica
from api.serializers import HidrometricaSerializer

  
@csrf_exempt
def lista_de_hidrometricas(request):
    """
    List all code datos, or create a new dato.
    """
    if request.method == 'GET':
        hidrometricas = Hidrometrica.objects.all()
        serializer = HidrometricaSerializer(hidrometricas, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = HidrometricaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
  

@csrf_exempt
def detalles_de_hidrometricas(request, id):
    """
    Retrieve, update or delete a code hidrometrica.
    """
    try:
        hidrometrica = Hidrometrica.objects.get(id=id)
    except hidrometrica.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = HidrometricaSerializer(hidrometrica)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = HidrometricaSerializer(hidrometrica, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        hidrometrica.delete()
        return JsonResponse({'id': hidrometrica.id}, status=204)

