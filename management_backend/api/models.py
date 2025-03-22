import uuid
from django.db import models
from django.contrib.auth.models import User, AbstractUser, Group, Permission

# Create your models here.

class user(AbstractUser):
    pass
    groups = models.ManyToManyField(
        Group, 
        related_name='api_user_groups',   # Custom related name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission, 
        related_name='api_user_permissions',  # Custom related name
        blank=True
    )
class Policy_Compliance_Oversight(models.Model):
    class Compliance_Status(models.TextChoices): #define the choices for the compliance status
        APPROVED = 'Approved'
        DENIED = 'Denied'
        IN_PROGRESS = 'In Progress'
    policy_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) #create a unique id for the policy
    policy_name = models.CharField(max_length=100) #create a field for the policy name
    policy_effective_date = models.DateField() #create a field for the policy effective date
    policy_last_update = models.DateField() #create a field for the policy last update
    policy_description = models.TextField() #create a field for the policy description
    policy_Compliance_status = models.CharField(
    max_length=30, 
    choices=Compliance_Status.choices, 
    default=Compliance_Status.IN_PROGRESS
) #create a field for the policy compliance status

class Salary_Release_Approval(models.Model):
    class Compliance_Status(models.TextChoices): #define the choices for the compliance status
        APPROVED = 'Approved'
        DENIED = 'Denied'
        IN_PROGRESS = 'In Progress'
    Employee_ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) #create a unique id for the employee
    Employee_Name = models.CharField(max_length=100) #create a field for the employee name
    Employee_Position = models.CharField(max_length=100)
    Employee_Salary = models.DecimalField(max_digits=10, decimal_places=2)
    Salary_Amount = models.DecimalField(max_digits=10, decimal_places=2)
    Payment_Date = models.DateField()
    Payroll_Summary = models.TextField()
    salary_compliance_status = models.CharField(
        max_length=30,
        choices=Compliance_Status.choices,
        default=Compliance_Status.IN_PROGRESS
    )



class Budget_Review_Approval(models.Model):
    class Compliance_Status(models.TextChoices): #define the choices for the compliance status
        APPROVED = 'Approved'
        DENIED = 'Denied'
        IN_PROGRESS = 'In Progress'
    Budget_ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) #create a unique id for the budget
    Budget_Department = models.CharField(max_length=100) #create a field for the budget department
    Budget_Amount_Requested = models.DecimalField(max_digits=10, decimal_places=2) #create a field for the budget amount requested
    Budget_Allocated = models.DecimalField(max_digits=10, decimal_places=2) #create a field for the budget allocated
    Budget_Justification = models.TextField() #create a field for the budget justification
    Budget_Compliance_Status = models.CharField(
        max_length=30,
        choices=Compliance_Status.choices,
        default=Compliance_Status.IN_PROGRESS
    )

class Purchasing_Approval(models.Model):
    class Compliance_Status(models.TextChoices): #define the choices for the compliance status
        APPROVED = 'Approved'
        DENIED = 'Denied'
        IN_PROGRESS = 'In Progress'
    Purchase_Req_ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) #create a unique id for the purchase request
    Purchase_Vendor_Details = models.CharField(max_length=100) #create a field for the purchase vendor details
    Purchase_Item_Desc = models.TextField() #create a field for the purchase item description
    Purchase_Quantity = models.DecimalField(max_digits=10, decimal_places=0) #create a field for the purchase quantity
    Purchase_Cost_Breakdown = models.DecimalField(max_digits=10, decimal_places=2) #create a field for the purchase cost breakdown
    Purchase_Justification = models.TextField() #create a field for the purchase justification
    Purchase_Compliance_Status = models.CharField(
        max_length=30,
        choices=Compliance_Status.choices,
        default=Compliance_Status.IN_PROGRESS
    ) 

class Project_Approval(models.Model):
    class Compliance_Status(models.TextChoices): #define the choices for the compliance status
        APPROVED = 'Approved'
        DENIED = 'Denied'
        IN_PROGRESS = 'In Progress'
    Project_ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Project_Name = models.CharField(max_length=100)
    Project_Objectives = models.TextField()
    Project_Details = models.TextField()
    Project_Timeline = models.CharField(max_length=100)
    Project_Approval_Status = models.CharField(
        max_length=30,
        choices=Compliance_Status.choices,
        default=Compliance_Status.IN_PROGRESS
    ) 

class Project_Monitoring(models.Model):
    class Compliance_Status(models.TextChoices): #define the choices for the compliance status
        APPROVED = 'Active'
        DENIED = 'Terminated'
        IN_PROGRESS = 'In Progress'
    Project_Monitoring_ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Project_Monitoring_Name = models.CharField(max_length=100)
    Project_Monitoring_Objectives = models.TextField()
    Project_Monitoring_Details = models.TextField()
    Project_Monitoring_Status = models.CharField(
        max_length=30,
        choices=Compliance_Status.choices,
        default=Compliance_Status.IN_PROGRESS
    )

class Staffing_Approval(models.Model):
    class Compliance_Status(models.TextChoices): #define the choices for the compliance status
        APPROVED = 'Approved'
        DENIED = 'Denied'
        IN_PROGRESS = 'In Progress'
    Staffing_ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Staffing_Job_Role = models.CharField(max_length=100)
    Staffing_Department = models.CharField(max_length=100)
    Staffing_Request_Type = models.CharField(max_length=20)
    Staffing_Leave_Duration = models.CharField(max_length=20)
    Staffing_Reason_for_Leave = models.TextField()
    Staffing_Status_Approval = models.CharField(
        max_length=30,
        choices=Compliance_Status.choices,
        default=Compliance_Status.IN_PROGRESS
    )
    Staffing_Contract_Duration = models.CharField(max_length=20)
