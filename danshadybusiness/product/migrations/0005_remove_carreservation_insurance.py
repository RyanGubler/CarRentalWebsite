# Generated by Django 4.1.1 on 2023-03-30 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_carreservation_insurance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carreservation',
            name='insurance',
        ),
    ]