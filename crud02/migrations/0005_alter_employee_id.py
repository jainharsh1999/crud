# Generated by Django 4.1.3 on 2022-11-04 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud02', '0004_employee_delete_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]