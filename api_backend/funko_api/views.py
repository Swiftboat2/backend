from django.shortcuts import render
from django.shortcuts import render
from funko_api.models import Funko
from django.http import JsonResponse
from funko_api.serializers import FunkoSerializer
 
def get_all_funkos():
    funkos = Funko.objects.all().order_by('number')
    funkos_serializers = FunkoSerializer(funkos, many=True)
    return funkos_serializers.data

def index(request):
    funkos = get_all_funkos()
    return render(request, 'index.html', {'funkos': funkos})

def funkos_rest(request):
    funkos = get_all_funkos()
    return JsonResponse(funkos, safe=False)

def about(request):
    return render(request, 'about.html')