from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse ("index")
    return render(request, 'shareRes/index.html')

def restaurantDetail(request):
    # return HttpResponse ("restaruantDetail")
    return render(request, 'shareRes/restaruantDetail.html')

def restaurantCreate(request):
    # return HttpResponse ("restaurantCreate")
    return render(request, 'shareRes/restaruantCreate.html')

def categoryCreate(request):
    return render(request, 'shareRes/categoryCreate.html')
