from rest_framework import generics
from .models import ManagementApproval
from .serializers import ManagementApprovalSerializer

class ManagementApprovalListCreateView(generics.ListCreateAPIView):
    queryset = ManagementApproval.objects.all()
    serializer_class = ManagementApprovalSerializer

class ManagementApprovalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ManagementApproval.objects.all()
    serializer_class = ManagementApprovalSerializer