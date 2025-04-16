# Generated by Django 5.1.6 on 2025-04-15 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ManagementApproval',
            fields=[
                ('approval_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('request_id_all', models.CharField(blank=True, max_length=255, null=True)),
                ('external_id', models.CharField(blank=True, max_length=255, null=True)),
                ('decision_date', models.DateField(blank=True, null=True)),
                ('issue_date', models.DateField(blank=True, null=True)),
                ('checked_by', models.CharField(blank=True, max_length=255, null=True)),
                ('checked_date', models.DateField(blank=True, null=True)),
                ('status', models.TextField()),
                ('due_date', models.DateField(blank=True, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Management Approval',
                'verbose_name_plural': 'Management Approvals',
                'db_table': 'management_approvals',
                'managed': False,
            },
        ),
    ]
