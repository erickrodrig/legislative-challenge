from django.http import HttpResponse
from django.shortcuts import render

from .forms import UploadFile
from .handlers import file_input_handler
from .models import Bill, Legislator
from .tables import BillDetailTable, LegislatorDetailTable


def home(request):
    return render(request, "home.html")

def bills(request):
    values = Bill.objects.all()
    table = BillDetailTable(values)
    return render(request, "bills.html", {"table": table})

def legislators(request):
    values = Legislator.objects.all()
    table = LegislatorDetailTable(values)
    return render(request, "legislators.html", {"table": table})

def upload(request):
    form = UploadFile(request.POST, request.FILES)
    if form.is_valid():
        uploaded_content = form.cleaned_data['file']
        if file_input_handler(uploaded_content.file):
            return HttpResponse("OK") 
    return render(request, "upload.html", {"form": UploadFile()})
