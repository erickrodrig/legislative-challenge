from django.db import models


class Legislator(models.Model):
    name = models.CharField(max_length=80)


class Bill(models.Model):
    title = models.CharField(max_length=80)
    sponsor_id = models.ForeignKey(
        Legislator, verbose_name="Primary sponsor", on_delete=models.PROTECT
    )


class Vote(models.Model):
    bill_id = models.ForeignKey(Bill, on_delete=models.PROTECT)


class VoteResult(models.Model):
    legislator_id = models.ForeignKey(Legislator, on_delete=models.PROTECT)
    vote_id = models.ForeignKey(Vote, on_delete=models.PROTECT)
    vote_type = models.IntegerField(choices=[(1, "Yea"), (2, "Nay")])


class LegislatorBill(models.Model):
    legislator = models.ForeignKey(Legislator, on_delete=models.PROTECT)
    supported_bills = models.IntegerField(default=0)
    opposed_bills = models.IntegerField(default=0)

    def update_bill_count(self):
        sup_count = VoteResult.objects.filter(legislator_id=self.legislator.pk, vote_type=1).count()
        ops_count = VoteResult.objects.filter(legislator_id=self.legislator.pk, vote_type=2).count()

        self.supported_bills = sup_count
        self.opposed_bills = ops_count

    def save(self, *args, **kwargs):
        self.update_bill_count()
        super().save(*args, **kwargs)


class BillDetail(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.PROTECT)
    supporters = models.IntegerField(default=0)
    opposers = models.IntegerField(default=0)
    primary_sponsor = models.ForeignKey(Legislator, on_delete=models.CASCADE, blank=True)

    def update_vote_count(self):
        votes = Vote.objects.filter(bill_id=self.bill.pk)
        self.supporters = VoteResult.objects.filter(vote_id__in=votes, vote_type=1).count()
        self.opposers = VoteResult.objects.filter(vote_id__in=votes, vote_type=2).count()
        self.primary_sponsor = self.bill.sponsor_id

    def save(self, *args, **kwargs):
        self.update_vote_count()
        super().save(*args, **kwargs)
