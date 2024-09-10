# Generated by Django 5.1.1 on 2024-09-08 00:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transport_name', models.CharField(max_length=255)),
                ('transport_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure_place', models.CharField(max_length=255)),
                ('arrival_place', models.CharField(max_length=255)),
                ('departure_date', models.DateTimeField()),
                ('return_date', models.DateTimeField(blank=True, null=True)),
                ('register_date', models.DateTimeField(auto_now_add=True)),
                ('original_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('proposed_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('note', models.TextField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to=settings.AUTH_USER_MODEL)),
                ('transport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='ticket_app.transport')),
            ],
        ),
    ]
