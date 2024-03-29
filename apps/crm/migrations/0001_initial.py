# Generated by Django 3.2.5 on 2022-02-19 11:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.CharField(db_index=True, max_length=60, unique=True)),
                ('first_name', models.CharField(max_length=300)),
                ('last_name', models.CharField(blank=True, default='', max_length=300, null=True)),
                ('client_type', models.CharField(blank=True, choices=[('Client', 'Client'), ('Farmer', 'Farmer'), ('Input Partner', 'Input Partner'), ('CMC', 'Collateral Management Client'), ('AFEXBroker', 'AFEXBroker'), ('Broker', 'Broker'), ('Dealer', 'Broker'), ('Affiliate', 'Affiliate'), ('Broker-Dealer', 'Broker-Dealer'), ('Promoter', 'Promoter'), ('Investor', 'Investor')], default='', max_length=300, null=True)),
                ('country_code', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('phone', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['cid'],
            },
        ),
        migrations.CreateModel(
            name='ClientWallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_balance', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('available_balance', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('lien_balance', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('cash_advance_limit', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('cash_advance_spent', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='crm.client')),
            ],
        ),
    ]
