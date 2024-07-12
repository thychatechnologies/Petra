# Generated by Django 4.2.4 on 2023-11-28 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0009_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(auto_now_add=True)),
                ('Name', models.CharField(max_length=100)),
                ('Mobile', models.CharField(max_length=20, null=True)),
                ('Description', models.TextField()),
            ],
        ),
    ]