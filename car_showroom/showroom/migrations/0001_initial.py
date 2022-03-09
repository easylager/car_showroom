# Generated by Django 4.0.2 on 2022-02-28 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('car', '0001_initial'),
        (u'customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Showroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=80)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=5)),
                ('features', models.JSONField()),
                ('cars', models.ManyToManyField(blank=True, null=True, to='car.Car')),
                ('customers', models.ManyToManyField(blank=True, null=True, to='customer.Customer')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='showroom.location')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ShowroomHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.car')),
                ('showroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='showroom.showroom')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ShowroomDiscount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start_at', models.DateTimeField(auto_now_add=True)),
                ('end_at', models.DateTimeField()),
                ('percent', models.DecimalField(decimal_places=2, max_digits=4)),
                ('cars', models.ManyToManyField(to='car.Car')),
                ('showroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='showroom.showroom')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
