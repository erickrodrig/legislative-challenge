from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def bills(request):
    return render(request, "bills.html")

def legislators(request):
    return render(request, "legislators.html")

def upload(request):
    return render(request, "upload.html")
