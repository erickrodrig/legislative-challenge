from django.db.models import Model
from django_tables2 import Column, Table

from .models import Bill, Legislator

TABLE_ATTRS = {"id": "table", "class": "table table-striped table-hover"}


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


def get_table_for(model_class: Model, data: dict) -> Table:
    class GenericTable(Table):
        class Meta:
            model = model_class
            attrs = TABLE_ATTRS

    return GenericTable(data)
