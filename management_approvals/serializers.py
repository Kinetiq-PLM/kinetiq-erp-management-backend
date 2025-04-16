from rest_framework import serializers
from .models import ManagementApproval

class ManagementApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagementApproval
        fields = '__all__'