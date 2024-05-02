from django.shortcuts import render
from . import models, tables, forms
from .forms import UploadFile
from .handlers import file_input_handler
from django.http import HttpResponse

def home(request):
    return render(request, "home.html")

def bills(request):
    values = tables.BillDetailTable(models.BillDetail.objects.all())
    return render(request, "bills.html", {"table": values})

def legislators(request):
    values = tables.LegislatorBillTable(models.LegislatorBill.objects.all())
    return render(request, "legislators.html", {"table": values})

def upload(request):
    form = UploadFile(request.POST, request.FILES)
    if form.is_valid():
        uploaded_content = form.cleaned_data['file']
        if file_input_handler(uploaded_content.file):
            return HttpResponse("OK") 
    return render(request, "upload.html", {"form": UploadFile()})
