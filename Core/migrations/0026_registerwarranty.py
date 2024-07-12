# Generated by Django 5.0 on 2024-07-08 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0025_alter_dealer_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterWarranty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(auto_now_add=True)),
                ('Name', models.CharField(max_length=100)),
                ('Address', models.TextField(blank=True, null=True)),
                ('Contact', models.CharField(max_length=15)),
                ('Warranty', models.CharField(max_length=100, unique=True)),
                ('Dealer', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
