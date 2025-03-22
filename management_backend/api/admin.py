from django.contrib import admin
from .models import Policy_Compliance_Oversight, Salary_Release_Approval, Budget_Review_Approval, Purchasing_Approval, Project_Approval, Project_Monitoring, Staffing_Approval

# Register your models here.

admin.site.register(Policy_Compliance_Oversight)
admin.site.register(Salary_Release_Approval)
admin.site.register(Budget_Review_Approval)
admin.site.register(Purchasing_Approval)
admin.site.register(Project_Approval)
admin.site.register(Project_Monitoring)
admin.site.register(Staffing_Approval)