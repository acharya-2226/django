from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def demo(request):
    # print("Hello World")
    return HttpResponse("Hello this is my first django app")
    
def countries(request):
    context= {
        "country_name" : "Nepal",
        "continent" : "asia",
        "country_code" : "+977",
    }
    return render(request, "countries.html", context)


def province(request):
    context= {
        "province_name" : "Bagmati",
        "province_cm" : "Alish Adhikari",
        "district" : "Kathmande",
    }
    return render(request, "province.html", context)
