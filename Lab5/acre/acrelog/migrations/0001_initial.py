# Generated by Django 3.2.6 on 2021-10-22 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_type', models.CharField(choices=[('research', 'Research'), ('commercial', 'Commercial')], max_length=100)),
                ('current_state', models.CharField(choices=[('used', 'Used'), ('not used', 'Not Used')], max_length=64)),
                ('field_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=64)),
                ('LastName', models.CharField(max_length=64)),
                ('worker_type', models.CharField(choices=[('technician', 'Technician'), ('researcher', 'Researcher'), ('student', 'Student'), ('manager', 'Manager')], max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=200)),
                ('job_description', models.CharField(max_length=200)),
                ('job_date', models.DateTimeField()),
                ('material_used', models.CharField(max_length=100)),
                ('material_amount', models.CharField(max_length=100)),
                ('job_type', models.CharField(choices=[('research job', 'Research Job'), ('commercial job', 'Commercial Job'), ('class practice', 'Class Practice')], max_length=100)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_done', to='acrelog.field')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='acrelog.worker')),
            ],
        ),
    ]