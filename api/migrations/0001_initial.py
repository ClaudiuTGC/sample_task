# Generated by Django 3.2.3 on 2021-05-27 11:41

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
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payload', models.CharField(max_length=300)),
                ('utc_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='new', max_length=50)),
                ('userId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('discountCode', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.chat')),
                ('clientId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.client')),
                ('operatorGroup', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='operatorGroup', to='api.operator', to_field='group')),
                ('operatorId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='operatorId', to='api.operator')),
                ('storeId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.store')),
            ],
        ),
    ]