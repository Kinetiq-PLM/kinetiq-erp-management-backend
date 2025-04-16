from django.urls import path
from .views import (
    ManagementApprovalListCreateView,
    ManagementApprovalDetailView
)

app_name = 'management_approvals'

urlpatterns = [
    path('approvals/', ManagementApprovalListCreateView.as_view(), name='approval-list-create'),
    path('approvals/<str:pk>/', ManagementApprovalDetailView.as_view(), name='approval-detail'),
]