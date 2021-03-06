# Generated by Django 4.0 on 2021-12-24 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_alter_customer_phone_number'),
        ('employee', '0001_initial'),
        ('service', '0001_initial'),
        ('attendance', '0003_rename_customer_id_attendance_customer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.customer'),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.employee'),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='service.service'),
        ),
    ]
