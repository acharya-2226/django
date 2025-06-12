from django import forms
from .models import country, Province

class CountryForm(forms.ModelForm):
    class Meta :
        model= country
        fields = "__all__"


class ProvinceForm(forms.ModelForm):
    class Meta : 
        model= Province
        fields=("province_name","province_cm")