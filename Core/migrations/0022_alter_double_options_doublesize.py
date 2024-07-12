# Generated by Django 5.0 on 2024-07-08 02:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0021_single_image3_alter_single_image2'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='double',
            options={'ordering': ['Name'], 'verbose_name': 'double', 'verbose_name_plural': 'doubles'},
        ),
        migrations.CreateModel(
            name='DoubleSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=50)),
                ('double', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='double_sizes', to='Core.double')),
            ],
        ),
    ]
