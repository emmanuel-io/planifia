# Generated by Django 5.1.7 on 2025-03-09 15:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_tenant_project_created_at_project_updated_at_and_more'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='tenant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='tasks.tenant'),
        ),
    ]
