from django.http import JsonResponse
from django.shortcuts import render
from skins_cs2.models import Skins
from skins_cs2.serializers import SkinsSerializer

def get_all_skins():
    try:
        skins = Skins.objects.all().order_by('name')
        skins_serializers = SkinsSerializer(skins, many=True)
        return skins_serializers.data
    except Exception as e:
        # Handle exceptions (e.g., log them or return an error message)
        return []

def skins_rest(request):
    skins = get_all_skins()
    return JsonResponse(skins, safe=False)

def index_sk(request):
    skins = get_all_skins()
    print(skins)
    return render(request, 'index_sk.html', {'Skins': skins})
