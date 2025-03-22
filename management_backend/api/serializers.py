from rest_framework import serializers
from .models import Policy_Compliance_Oversight, Salary_Release_Approval, Budget_Review_Approval, Purchasing_Approval, Project_Approval, Project_Monitoring, Staffing_Approval

class Policy_Compliance_Oversight_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Policy_Compliance_Oversight
        fields = '__all__'

class Salary_Release_Approval_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Salary_Release_Approval
        fields = '__all__'

class Budget_Review_Approval_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Budget_Review_Approval
        fields = '__all__'

class Purchasing_Approval_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Purchasing_Approval
        fields = '__all__'

class Project_Approval_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Project_Approval
        fields = '__all__'

class Project_Monitoring_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Project_Monitoring
        fields = '__all__'

class Staffing_Approval_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Staffing_Approval
        fields = '__all__'