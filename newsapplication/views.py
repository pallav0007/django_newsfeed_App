from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
import requests
import json
from decouple import config
from django.urls import reverse_lazy
# Create your views here.
class MyForm(forms.Form): #Note that it is not inheriting from forms.ModelForm
        category = forms.CharField(label="category",help_text="like sports,bussiness etc.",widget=forms.Textarea(attrs={'class': 'form-control', 'cols': 5, 'rows': 1}))
        country = forms.CharField(label="country",help_text="Enter countries ISO 3166-1 alpha-2 code",widget=forms.Textarea(attrs={'class': 'form-control', 'cols': 5, 'rows': 1}))
key2 = config("key2")
url2 = "https://newsapi.org/v2/top-headlines"

def universal(request,country="in",category="business"):

    param = {"country":country, "category": category, "apiKey": key2}
    response = requests.get(url2, param)
    res = json.loads(response.content)
    return render(request, "home.html", {"res": res})
def home(request,country="in",category="business"):
    form = MyForm()
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # now in the object cd, you have the form as a dictionary.
            # content = cd.get('content')
            # sources = cd.get('sources')
            category = cd.get('languages')
            country = cd.get('country')
            universal(request, **cd)
            print("dictionary check",cd)

    param = {"country":country, "category": category,"apiKey": key2}
    response = requests.get(url2, param)
    res = json.loads(response.content)

    return render(request,"home.html",{"res":res,"form":form})
def homeus(request):

    param = {"country":"us", "category": "business", "apiKey": key2}
    response = requests.get(url2, param)
    res = json.loads(response.content)
    return render(request,"home.html",{"res":res})
def homesp(request):

    param = {"country":"in", "category": "sport", "apiKey": key2}
    response = requests.get(url2, param)
    res = json.loads(response.content)
    return render(request,"home.html",{"res":res})
def homeusp(request):

    param = {"country":"us", "category": "sport", "apiKey": key2}
    response = requests.get(url2, param)
    res = json.loads(response.content)
    return render(request,"home.html",{"res":res})

