from django.shortcuts import render

# Create your views here.
# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    print('Index called and Entered in Airport', request.GET)
    return JsonResponse({"message": "hi hello  welcome  in airport...!"})

