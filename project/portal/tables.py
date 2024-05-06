from django_tables2 import Table
from . import models

TABLE_ATTRS = {
    'id': 'table',
    'class': 'table table-striped table-hover'
}

class BillDetailTable(Table):
    class Meta:
        model = models.BillDetail
        attrs = TABLE_ATTRS

class LegislatorBillTable(Table):
    class Meta:
        model = models.LegislatorBill
        attrs = TABLE_ATTRS
