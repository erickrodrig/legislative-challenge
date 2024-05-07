from rest_framework.generics import ListCreateAPIView

from project.portal import models

from . import serializers


class BillList(ListCreateAPIView):
    queryset = models.Bill.objects.all()
    serializer_class = serializers.BillSerializer

class LegislatorList(ListCreateAPIView):
    queryset = models.Legislator.objects.all()
    serializer_class = serializers.LegislatorSerializer

class VoteList(ListCreateAPIView):
    queryset = models.Vote.objects.all()
    serializer_class = serializers.VoteSerializer

class VoteResultList(ListCreateAPIView):
    queryset = models.VoteResult.objects.all()
    serializer_class = serializers.VoteResultSerializer

# class BillUpdate(RetrieveUpdateDestroyAPIView):
#     queryset = models.Bill.objects.all()
#     serializer_class = BillSerializer
#     lookup_field = 'pk'
