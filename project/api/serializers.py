from rest_framework.serializers import ModelSerializer

from project.portal import models


class BillSerializer(ModelSerializer):
    class Meta:
        model = models.Bill
        fields = "__all__"

class LegislatorSerializer(ModelSerializer):
    class Meta:
        model = models.Legislator
        fields = "__all__"

class VoteSerializer(ModelSerializer):
    class Meta:
        model = models.Vote
        fields = "__all__"

class VoteResultSerializer(ModelSerializer):
    class Meta:
        model = models.VoteResult
        fields = "__all__"
