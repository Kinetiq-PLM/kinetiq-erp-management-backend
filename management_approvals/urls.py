from django.urls import path
from .views import (
    ManagementApprovalListCreateView,
    ManagementApprovalDetailView
)

app_name = 'management_approvals'

urlpatterns = [
    path('', ManagementApprovalListCreateView.as_view(), name='approval-list-create'),
    path('<str:pk>/', ManagementApprovalDetailView.as_view(), name='approval-detail'),
]