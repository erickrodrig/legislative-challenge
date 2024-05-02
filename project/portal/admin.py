from django.contrib import admin
from . import models

admin.site.register(models.Legislator)
admin.site.register(models.Bill)
admin.site.register(models.Vote)
admin.site.register(models.VoteResult)
admin.site.register(models.LegislatorBill)
admin.site.register(models.BillDetail)
