from django.urls import path

from . import views

urlpatterns = [
    path('bill/', views.BillList.as_view(), name="bill-list"),
    path('legislator/', views.LegislatorList.as_view(), name="legislator-list"),
    path('vote/', views.VoteList.as_view(), name="vote-list"),
    path('voteresult/', views.VoteResultList.as_view(), name="voteresult-list"),
    # path('bill/<int:pk>/', views.BillUpdate.as_view(), name="bill-update-delete"),
]
