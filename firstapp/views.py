from django.shortcuts import render
from django.http import HttpResponse
from .forms import CountryForm,ProvinceForm



# Create your views here.
def demo(request):
    # print("Hello World")
    return HttpResponse("Hello this is my first django app")
    
def country(request):
    context= {
        "country_name" : "Nepal",
        "continent" : "asia",
        "country_code" : "+977",
    }
    return render(request, "country.html", context)


def province(request):
    context= {
        "province_name" : "Bagmati",
        "province_cm" : "Alish Adhikari",
        "district" : "Kathmande",
    }
    return render(request, "province.html", context)

def add_country(request):
    add_country_form = CountryForm()
    context={
        "form" : add_country_form,
        "title" : "country | Add Page"
    }
    if request.method == "POST":
        request_data = {
            "name" : request.POST.get("country_name"),
            "code" : request.POST.get("code"),
            "continent" :request.POST.get("continent"),
        }
        context.setdefault("new_data", request_data)
        return render(request, "add_country.html", context)
    return render(request, "add_country.html", context)

def add_province(request):
    add_province_form = ProvinceForm()
    context={
        "form" : add_province_form,
        "title" : "Province | Add Page"
    }
    return render(request, "add_province.html", context)