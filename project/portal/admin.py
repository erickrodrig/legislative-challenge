from django.contrib import admin
from . import models


class LegislatorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    
class BillAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'sponsor_id']

class VoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'bill_id']
    
class VoteResultAdmin(admin.ModelAdmin):
    list_display = ['id', 'legislator_id', 'vote_id', 'vote_type']


admin.site.register(models.Vote, VoteAdmin)
admin.site.register(models.VoteResult, VoteResultAdmin)
admin.site.register(models.Legislator, LegislatorAdmin)
admin.site.register(models.Bill, BillAdmin)
admin.site.register(models.LegislatorBill,)
admin.site.register(models.BillDetail)
