from django_tables2 import Table, Column
from .models import Legislator, Bill


TABLE_ATTRS = {
    'id': 'table',
    'class': 'table table-striped table-hover'
}


class BillDetailTable(Table):
    title = Column(verbose_name="Bill")
    supporters = Column()
    opposers = Column()

    class Meta:
        model = Bill
        attrs = TABLE_ATTRS

class LegislatorDetailTable(Table):
    name = Column()
    supported_bills = Column()
    opposed_bills = Column()

    class Meta:
        model = Legislator
        attrs = TABLE_ATTRS
