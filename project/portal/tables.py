from django_tables2 import Table
from . import models

class BillDetailTable(Table):
    class Meta:
        model = models.BillDetail
        # fields = ("bill", "supporters", "opposers", "primary_sponsor") # excludes id
        attrs = {
            'id': 'table-bills',
            'class': 'table table-striped'
        }

class LegislatorBillTable(Table):
    class Meta:
        model = models.LegislatorBill
        # fields = ("legislator", "supported_bills", "opposed_bills")
        attrs = {
            'id': 'table-legislators',
            'class': 'table table-striped'
        }
