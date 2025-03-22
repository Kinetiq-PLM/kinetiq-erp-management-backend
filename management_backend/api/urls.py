from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    Policy_Compliance_Oversight_ViewSet,
    Salary_Release_Approval_ViewSet,
    Budget_Review_Approval_ViewSet,
    Purchasing_Approval_ViewSet,
    Project_Approval_ViewSet,
    Project_Monitoring_ViewSet,
    Staffing_Approval_ViewSet
)
from django.urls import path, include

# Create the router
router = DefaultRouter()
router.register('policy_compliance_oversight', Policy_Compliance_Oversight_ViewSet, basename='policy_compliance_oversight')
router.register('salary_release_approval', Salary_Release_Approval_ViewSet, basename='salary_release_approval')
router.register('budget_review_approval', Budget_Review_Approval_ViewSet, basename='budget_review_approval')
router.register('purchasing_approval', Purchasing_Approval_ViewSet, basename='purchasing_approval')
router.register('project_approval', Project_Approval_ViewSet, basename='project_approval')
router.register('project_monitoring', Project_Monitoring_ViewSet, basename='project_monitoring')
router.register('staffing_approval', Staffing_Approval_ViewSet, basename='staffing_approval')


def get_router():
    from api.urls import router 
    return router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

