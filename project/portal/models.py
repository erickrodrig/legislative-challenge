from django.db import models


class Legislator(models.Model):
    name = models.CharField(max_length=80, unique=True, null=True)

    @property
    def supported_bills(self):
        return VoteResult.objects.filter(legislator_id=self.pk, vote_type=1).count() or "-"

    @property
    def opposed_bills(self):
        return VoteResult.objects.filter(legislator_id=self.pk, vote_type=2).count() or "-"

    def __str__(self):
        return self.name or '-'


class Bill(models.Model):
    title = models.CharField(max_length=80, unique=True, null=True)
    sponsor_id = models.ForeignKey(
        to=Legislator, 
        verbose_name="Primary sponsor", 
        on_delete=models.PROTECT
    )

    @property
    def supporters(self):
        return VoteResult.objects.filter(vote_id__bill_id=self.pk, vote_type=1).count() or "-"

    @property
    def opposers(self):
        return VoteResult.objects.filter(vote_id__bill_id=self.pk, vote_type=2).count() or "-"

    @property
    def primary_sponsor(self):
        return self.sponsor_id

    def __str__(self):
        return self.title


class Vote(models.Model):
    bill_id = models.ForeignKey(Bill, null=True, on_delete=models.PROTECT)


class VoteResult(models.Model):
    legislator_id = models.ForeignKey(Legislator, on_delete=models.PROTECT)
    vote_id = models.ForeignKey(Vote, on_delete=models.PROTECT)
    vote_type = models.IntegerField(choices=[(1, "Yea"), (2, "Nay")])
