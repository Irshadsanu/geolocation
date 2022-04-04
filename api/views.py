from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def get_api(request):
    if request.method == 'GET':
        return JsonResponse("api project", safe=False)
    else:
        print(request.data)
        return JsonResponse("apiproject done", safe=False)
