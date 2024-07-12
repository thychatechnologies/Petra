# Generated by Django 5.0 on 2024-07-08 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0023_double_image3'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(auto_now_add=True)),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('Contact_number', models.CharField(max_length=15)),
                ('Business', models.CharField(max_length=100)),
                ('Address', models.TextField()),
                ('State', models.CharField(max_length=50)),
                ('District', models.CharField(max_length=50)),
            ],
        ),
    ]