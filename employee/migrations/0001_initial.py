# Generated by Django 4.0 on 2021-12-22 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=30)),
                ('position', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]
