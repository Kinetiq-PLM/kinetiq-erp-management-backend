# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AdditionalService(models.Model):
    additional_service_id = models.CharField(primary_key=True, max_length=255)
    total_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'additional_service'


class AdditionalServiceType(models.Model):
    additional_service_type_id = models.CharField(primary_key=True, max_length=255)
    additional_service = models.ForeignKey(AdditionalService, models.DO_NOTHING, blank=True, null=True)
    service_type = models.TextField()
    service_fee = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField(blank=True, null=True)
    date_start = models.DateField()
    status = models.TextField()
    total_service_fee = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'additional_service_type'


class AfterAnalysisSched(models.Model):
    analysis_sched_id = models.CharField(primary_key=True, max_length=255)
    analysis = models.ForeignKey('ServiceAnalysis', models.DO_NOTHING, blank=True, null=True)
    service_date = models.DateField()
    technician_id = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    service_status = models.TextField()

    class Meta:
        managed = False
        db_table = 'after_analysis_sched'


class Assets(models.Model):
    asset_id = models.CharField(primary_key=True, max_length=255)
    asset_name = models.CharField(max_length=255)
    purchase_date = models.DateField(blank=True, null=True)
    purchase_price = models.DecimalField(max_digits=65535, decimal_places=65535)
    serial_no = models.CharField(max_length=225, blank=True, null=True)
    content_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assets'


class AuditLog(models.Model):
    log_id = models.CharField(primary_key=True, max_length=255)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    action = models.TextField()
    timestamp = models.DateTimeField(blank=True, null=True)
    ip_address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'audit_log'


class BusinessPartnerMaster(models.Model):
    partner_id = models.CharField(primary_key=True, max_length=255)
    employee_id = models.CharField(unique=True, max_length=255, blank=True, null=True)
    vendor_code = models.OneToOneField('Vendor', models.DO_NOTHING, db_column='vendor_code', blank=True, null=True)
    customer_id = models.CharField(unique=True, max_length=255, blank=True, null=True)
    partner_name = models.CharField(max_length=255)
    category = models.TextField(blank=True, null=True)  # This field type is a guess.
    contact_info = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'business_partner_master'


class Currency(models.Model):
    currency_id = models.CharField(primary_key=True, max_length=255)
    currency_name = models.CharField(max_length=255)
    exchange_rate = models.DecimalField(max_digits=15, decimal_places=6)
    valid_from = models.DateField()
    valid_to = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'currency'


class DeliveryOrder(models.Model):
    delivery_order_id = models.CharField(primary_key=True, max_length=255)
    service_order = models.ForeignKey('ServiceOrder', models.DO_NOTHING, blank=True, null=True)
    customer_id = models.CharField(max_length=255, blank=True, null=True)
    customer_address = models.TextField(blank=True, null=True)
    delivery_status = models.TextField()
    delivery_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'delivery_order'


class DocumentHeader(models.Model):
    document_id = models.CharField(primary_key=True, max_length=255)
    document_type = models.TextField()  # This field type is a guess.
    vendor_code = models.CharField(max_length=255, blank=True, null=True)
    document_no = models.IntegerField(unique=True, blank=True, null=True)
    transaction_id = models.CharField(unique=True, max_length=255)
    content_id = models.CharField(max_length=255, blank=True, null=True)
    invoice_id = models.CharField(max_length=255, blank=True, null=True)
    ar_credit_memo = models.CharField(unique=True, max_length=255, blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    posting_date = models.DateField()
    delivery_date = models.DateField(blank=True, null=True)
    document_date = models.DateField()
    buyer = models.CharField(max_length=255, blank=True, null=True)
    employee_id = models.CharField(max_length=255, blank=True, null=True)
    initial_amount = models.DecimalField(max_digits=18, decimal_places=2)
    discount_rate = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    discount_amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    freight = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    tax_amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    transaction_cost = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'document_header'


class DocumentItems(models.Model):
    content_id = models.CharField(primary_key=True, max_length=255)
    asset_id = models.CharField(max_length=255, blank=True, null=True)
    document_id = models.CharField(max_length=255, blank=True, null=True)
    material_id = models.CharField(max_length=255, blank=True, null=True)
    serial_id = models.CharField(max_length=255, blank=True, null=True)
    productdocu_id = models.CharField(max_length=255, blank=True, null=True)
    external_id = models.CharField(max_length=255, blank=True, null=True)
    delivery_request_id = models.CharField(max_length=255, blank=True, null=True)
    request_date = models.DateField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    total = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    batch_no = models.CharField(unique=True, max_length=100, blank=True, null=True)
    warehouse_id = models.CharField(max_length=255, blank=True, null=True)
    cost = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    delivery_type = models.TextField(blank=True, null=True)  # This field type is a guess.
    receiving_module = models.TextField(blank=True, null=True)  # This field type is a guess.
    status = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'document_items'


class ExternalModule(models.Model):
    external_id = models.CharField(primary_key=True, max_length=255)
    content_id = models.CharField(max_length=255, blank=True, null=True)
    purchase_id = models.CharField(max_length=255, blank=True, null=True)
    request_id = models.CharField(max_length=255, blank=True, null=True)
    approval_id = models.CharField(max_length=255, blank=True, null=True)
    goods_issue_id = models.CharField(max_length=255, blank=True, null=True)
    approval_request_id = models.CharField(max_length=255, blank=True, null=True)
    billing_receipt_id = models.CharField(max_length=255, blank=True, null=True)
    delivery_receipt_id = models.CharField(max_length=255, blank=True, null=True)
    project_resources_id = models.CharField(max_length=255, blank=True, null=True)
    project_tracking_id = models.CharField(max_length=255, blank=True, null=True)
    project_request_id = models.CharField(max_length=255, blank=True, null=True)
    production_order_detail_id = models.CharField(max_length=255, blank=True, null=True)
    rework_id = models.CharField(max_length=255, blank=True, null=True)
    deprecation_report_id = models.CharField(max_length=255, blank=True, null=True)
    expiry_report_id = models.CharField(max_length=255, blank=True, null=True)
    rework_quantity = models.IntegerField(blank=True, null=True)
    reason_rework = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'external_module'


class ItemMasterData(models.Model):
    item_id = models.CharField(primary_key=True, max_length=255)
    asset = models.ForeignKey(Assets, models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey('Products', models.DO_NOTHING, blank=True, null=True)
    material = models.ForeignKey('RawMaterials', models.DO_NOTHING, blank=True, null=True)
    item_name = models.CharField(max_length=255)
    item_type = models.TextField(blank=True, null=True)  # This field type is a guess.
    unit_of_measure = models.TextField(blank=True, null=True)  # This field type is a guess.
    item_status = models.TextField(blank=True, null=True)  # This field type is a guess.
    manage_item_by = models.TextField(blank=True, null=True)  # This field type is a guess.
    preferred_vendor = models.CharField(max_length=255, blank=True, null=True)
    purchasing_uom = models.TextField(blank=True, null=True)  # This field type is a guess.
    items_per_purchase_unit = models.IntegerField(blank=True, null=True)
    purchase_quantity_per_package = models.IntegerField(blank=True, null=True)
    sales_uom = models.TextField(blank=True, null=True)  # This field type is a guess.
    items_per_sale_unit = models.IntegerField(blank=True, null=True)
    sales_quantity_per_package = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_master_data'


class ManagementApprovals(models.Model):
    approval_id = models.CharField(primary_key=True, max_length=255)
    request_id_all = models.CharField(max_length=255, blank=True, null=True)
    external_id = models.CharField(max_length=255, blank=True, null=True)
    decision_date = models.DateField(blank=True, null=True)
    issue_date = models.DateField(blank=True, null=True)
    checked_by = models.CharField(max_length=255, blank=True, null=True)
    checked_date = models.DateField(blank=True, null=True)
    status = models.TextField()  # This field type is a guess.
    due_date = models.DateField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'management_approvals'


class Notifications(models.Model):
    notifications_id = models.CharField(primary_key=True, max_length=255)
    module = models.CharField()
    to_user = models.ForeignKey('Users', models.DO_NOTHING)
    message = models.TextField()
    notifications_status = models.TextField()  # This field type is a guess.
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notifications'


class Policies(models.Model):
    policy_id = models.CharField(primary_key=True, max_length=255)
    policy_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    effective_date = models.DateField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'policies'


class ProductDocumentItems(models.Model):
    productdocu_id = models.CharField(primary_key=True, max_length=255)
    product_id = models.CharField(max_length=255, blank=True, null=True)
    manuf_date = models.DateField()
    expiry_date = models.DateField()
    content_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_document_items'


class Products(models.Model):
    product_id = models.CharField(primary_key=True, max_length=255)
    product_name = models.CharField(max_length=255)
    description = models.TextField()
    selling_price = models.DecimalField(max_digits=65535, decimal_places=65535)
    stock_level = models.IntegerField(blank=True, null=True)
    unit_of_measure = models.TextField()  # This field type is a guess.
    batch_no = models.CharField(max_length=255, blank=True, null=True)
    item_status = models.TextField(blank=True, null=True)  # This field type is a guess.
    warranty_period = models.IntegerField(blank=True, null=True)
    policy = models.ForeignKey(Policies, models.DO_NOTHING, blank=True, null=True)
    content_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'


class RawMaterials(models.Model):
    material_id = models.CharField(primary_key=True, max_length=255)
    material_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    unit_of_measure = models.TextField(blank=True, null=True)  # This field type is a guess.
    cost_per_unit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    vendor_code = models.ForeignKey('Vendor', models.DO_NOTHING, db_column='vendor_code', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'raw_materials'


class RolesPermission(models.Model):
    role_id = models.CharField(primary_key=True, max_length=255)
    role_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    permissions = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles_permission'


class SerialTracking(models.Model):
    serial_id = models.CharField(primary_key=True, max_length=255)
    document_id = models.CharField(max_length=255, blank=True, null=True)
    serial_no = models.CharField(unique=True, max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'serial_tracking'


class ServiceAnalysis(models.Model):
    analysis_id = models.CharField(primary_key=True, max_length=255)
    service_request = models.ForeignKey('ServiceRequest', models.DO_NOTHING, blank=True, null=True)
    analysis_date = models.DateField(blank=True, null=True)
    technician_id = models.CharField(max_length=255, blank=True, null=True)
    customer_id = models.CharField(max_length=255, blank=True, null=True)
    analysis_status = models.TextField()
    analysis_description = models.TextField(blank=True, null=True)
    product_id = models.CharField(max_length=255, blank=True, null=True)
    contract = models.ForeignKey('ServiceContract', models.DO_NOTHING, blank=True, null=True)
    labor_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'service_analysis'


class ServiceBilling(models.Model):
    service_billing_id = models.CharField(primary_key=True, max_length=255)
    service_order = models.ForeignKey('ServiceOrder', models.DO_NOTHING, blank=True, null=True)
    renewal = models.ForeignKey('WarrantyRenewal', models.DO_NOTHING, blank=True, null=True)
    analysis = models.ForeignKey(ServiceAnalysis, models.DO_NOTHING, blank=True, null=True)
    service_request = models.ForeignKey('ServiceRequest', models.DO_NOTHING, blank=True, null=True)
    service_billing_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    outsource_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    operational_cost_id = models.CharField(max_length=255, blank=True, null=True)
    total_payable = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    billing_status = models.TextField()
    date_paid = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'service_billing'


class ServiceCall(models.Model):
    service_call_id = models.CharField(primary_key=True, max_length=255)
    date_created = models.DateTimeField(blank=True, null=True)
    service_ticket_id = models.CharField(max_length=255, blank=True, null=True)
    customer_id = models.CharField(max_length=255, blank=True, null=True)
    call_type = models.TextField()
    technician_id = models.CharField(max_length=255, blank=True, null=True)
    call_status = models.TextField()
    date_closed = models.DateTimeField(blank=True, null=True)
    contract = models.ForeignKey('ServiceContract', models.DO_NOTHING, blank=True, null=True)
    product_id = models.CharField(max_length=255, blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    priority_level = models.TextField()
    resolution = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'service_call'


class ServiceContract(models.Model):
    contract_id = models.CharField(primary_key=True, max_length=255)
    statement_item_id = models.CharField(max_length=255, blank=True, null=True)
    customer_id = models.CharField(max_length=255, blank=True, null=True)
    additional_service = models.ForeignKey(AdditionalService, models.DO_NOTHING, blank=True, null=True)
    contract_description = models.TextField(blank=True, null=True)
    date_issued = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    product_id = models.CharField(max_length=255, blank=True, null=True)
    contract_status = models.TextField()
    product_quantity = models.IntegerField(blank=True, null=True)
    renewal = models.ForeignKey('WarrantyRenewal', models.DO_NOTHING, blank=True, null=True)
    renewal_date = models.DateField(blank=True, null=True)
    renewal_end_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'service_contract'


class ServiceOrder(models.Model):
    service_order_id = models.CharField(primary_key=True, max_length=255)
    analysis = models.ForeignKey(ServiceAnalysis, models.DO_NOTHING, blank=True, null=True)
    customer_id = models.CharField(max_length=255, blank=True, null=True)
    order_date = models.DateTimeField(blank=True, null=True)
    order_total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'service_order'


class ServiceOrderItem(models.Model):
    service_order_item_id = models.CharField(primary_key=True, max_length=255)
    service_order = models.ForeignKey(ServiceOrder, models.DO_NOTHING, blank=True, null=True)
    item_id = models.CharField(max_length=255, blank=True, null=True)
    principal_item_id = models.CharField(max_length=255, blank=True, null=True)
    item_name = models.CharField(max_length=255, blank=True, null=True)
    item_quantity = models.IntegerField(blank=True, null=True)
    item_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'service_order_item'


class ServiceReport(models.Model):
    report_id = models.CharField(primary_key=True, max_length=255)
    service_call = models.ForeignKey(ServiceCall, models.DO_NOTHING, blank=True, null=True)
    service_ticket_id = models.CharField(max_length=255, blank=True, null=True)
    service_billing = models.ForeignKey(ServiceBilling, models.DO_NOTHING, blank=True, null=True)
    service_request = models.ForeignKey('ServiceRequest', models.DO_NOTHING, blank=True, null=True)
    renewal = models.ForeignKey('WarrantyRenewal', models.DO_NOTHING, blank=True, null=True)
    technician_id = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    report_status = models.TextField()
    request_type = models.TextField(blank=True, null=True)
    submission_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'service_report'


class ServiceRequest(models.Model):
    service_request_id = models.CharField(primary_key=True, max_length=255)
    service_call = models.ForeignKey(ServiceCall, models.DO_NOTHING, blank=True, null=True)
    request_date = models.DateField(blank=True, null=True)
    customer_id = models.CharField(max_length=255, blank=True, null=True)
    technician_id = models.CharField(max_length=255, blank=True, null=True)
    request_type = models.TextField()
    request_status = models.TextField()
    request_description = models.TextField(blank=True, null=True)
    request_remarks = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'service_request'


class Users(models.Model):
    user_id = models.CharField(primary_key=True, max_length=255)
    employee_id = models.CharField(unique=True, max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    role = models.ForeignKey(RolesPermission, models.DO_NOTHING, blank=True, null=True)
    status = models.TextField(blank=True, null=True)  # This field type is a guess.
    type = models.TextField(blank=True, null=True)  # This field type is a guess.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class Vendor(models.Model):
    vendor_code = models.CharField(primary_key=True, max_length=255)
    application_reference = models.CharField(max_length=255, blank=True, null=True)
    vendor_name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255, blank=True, null=True)
    status = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'vendor'


class Warehouse(models.Model):
    warehouse_id = models.CharField(primary_key=True, max_length=255)
    warehouse_location = models.CharField(max_length=255)
    stored_materials = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouse'


class WarrantyRenewal(models.Model):
    renewal_id = models.CharField(primary_key=True, max_length=255)
    service_call = models.ForeignKey(ServiceCall, models.DO_NOTHING, blank=True, null=True)
    contract = models.ForeignKey(ServiceContract, models.DO_NOTHING, blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    renewal_warranty_start = models.DateField(blank=True, null=True)
    renewal_warranty_end = models.DateField(blank=True, null=True)
    renewal_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warranty_renewal'
