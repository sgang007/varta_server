from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


# Create your views here.
@csrf_exempt
def get_sender(request):
    data = request.POST


@csrf_exempt
def echo(request):
    return HttpResponse(request.body, content_type=request.content_type)