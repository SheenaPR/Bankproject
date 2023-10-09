# Generated by Django 4.2.5 on 2023-10-06 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=50)),
                ('phone_no', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField(max_length=250)),
                ('district', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=50)),
                ('account_type', models.CharField(max_length=50)),
                ('materials_req', models.CharField(max_length=50)),
            ],
        ),
    ]