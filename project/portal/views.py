from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

from .forms import UploadFile
from .handlers import handle_input_file
from .models import Bill, Legislator
from .tables import BillDetailTable, LegislatorDetailTable, get_table_for


@login_required
def home(request):
    return render(request, "home.html")


@login_required
def bills(request):
    values = Bill.objects.all()
    table = BillDetailTable(values)
    return render(request, "bills.html", {"table": table})


@login_required
def legislators(request):
    values = Legislator.objects.all()
    table = LegislatorDetailTable(values)
    return render(request, "legislators.html", {"table": table})


@login_required
@user_passes_test(lambda u: u.is_superuser, login_url="/")
def upload(request):
    form = UploadFile(request.POST, request.FILES)
    if form.is_valid():
        uploaded_content = form.cleaned_data["file"]
        success, model, imported_data = handle_input_file(uploaded_content.file)

        if success:
            table = get_table_for(model, imported_data)
            return render(request, "upload.html", {"imported_data": table})
    return render(request, "upload.html", {"form": UploadFile()})
