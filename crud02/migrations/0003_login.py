# Generated by Django 4.1.3 on 2022-11-03 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud02', '0002_alter_customer_pincode_alter_vender_pincode'),
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100, null=True)),
                ('password', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]