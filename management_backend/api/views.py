# Create your views here.
from rest_framework import viewsets
from .models import Policy_Compliance_Oversight, Salary_Release_Approval, Budget_Review_Approval, Purchasing_Approval, Project_Approval, Project_Monitoring, Staffing_Approval
from .serializers import Policy_Compliance_Oversight_Serializer, Salary_Release_Approval_Serializer, Budget_Review_Approval_Serializer, Purchasing_Approval_Serializer, Project_Approval_Serializer, Project_Monitoring_Serializer, Staffing_Approval_Serializer
from django.core.exceptions import ValidationError

class Policy_Compliance_Oversight_ViewSet(viewsets.ModelViewSet):
    queryset = Policy_Compliance_Oversight.objects.all()
    serializer_class = Policy_Compliance_Oversight_Serializer

class Salary_Release_Approval_ViewSet(viewsets.ModelViewSet):
    queryset = Salary_Release_Approval.objects.all()
    serializer_class = Salary_Release_Approval_Serializer

class Budget_Review_Approval_ViewSet(viewsets.ModelViewSet):
    queryset = Budget_Review_Approval.objects.all()
    serializer_class = Budget_Review_Approval_Serializer

class Purchasing_Approval_ViewSet(viewsets.ModelViewSet):
    queryset = Purchasing_Approval.objects.all()
    serializer_class = Purchasing_Approval_Serializer

class Project_Approval_ViewSet(viewsets.ModelViewSet):
    queryset = Project_Approval.objects.all()
    serializer_class = Project_Approval_Serializer

class Project_Monitoring_ViewSet(viewsets.ModelViewSet):
    queryset = Project_Monitoring.objects.all()
    serializer_class = Project_Monitoring_Serializer

class Staffing_Approval_ViewSet(viewsets.ModelViewSet):
    queryset = Staffing_Approval.objects.all()
    serializer_class = Staffing_Approval_Serializer
