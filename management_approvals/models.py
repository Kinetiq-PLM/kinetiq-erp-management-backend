from django.db import models

class ManagementApproval(models.Model):
    class StatusChoice(models.TextChoices):
        PENDING = 'pending', 'Pending'
        APPROVED = 'approved', 'Approved'
        REJECTED = 'rejected', 'Rejected'

    approval_id = models.CharField(primary_key=True, max_length=255)
    request_id_all = models.CharField(max_length=255, blank=True, null=True)
    external_id = models.CharField(max_length=255, blank=True, null=True)
    decision_date = models.DateField(blank=True, null=True)
    issue_date = models.DateField(blank=True, null=True)
    checked_by = models.CharField(max_length=255, blank=True, null=True)
    checked_date = models.DateField(blank=True, null=True)
    status = models.CharField(
        max_length=255,
        choices=StatusChoice.choices,
        default=StatusChoice.PENDING,
        blank=True,
        null=True
    )
    due_date = models.DateField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'management_approvals'
        verbose_name = 'Management Approval'
        verbose_name_plural = 'Management Approvals'