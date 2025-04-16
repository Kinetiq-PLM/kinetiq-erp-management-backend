from django.contrib import admin
from .models import ManagementApproval

@admin.register(ManagementApproval)
class ManagementApprovalAdmin(admin.ModelAdmin):
    list_display = ('approval_id', 'request_id_all', 'external_id', 'status')
    list_filter = ('status', 'decision_date', 'issue_date')
    search_fields = ('approval_id', 'request_id_all', 'remarks')
    readonly_fields = ('approval_id',)
    ordering = ('-issue_date',)

    fieldsets = (
        ('Basic Information', {
            'fields': ('approval_id', 'request_id_all', 'external_id')
        }),
        ('Dates', {
            'fields': ('issue_date', 'decision_date', 'checked_date', 'due_date')
        }),
        ('Status & Verification', {
            'fields': ('status', 'checked_by', 'remarks')
        }),
    )

    def save_model(self, request, obj, form, change):
        if not obj.approval_id:
            # Generate a unique approval_id if not provided
            import uuid
            obj.approval_id = str(uuid.uuid4())
        super().save_model(request, obj, form, change)