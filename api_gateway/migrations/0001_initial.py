# Generated by Django 4.2.6 on 2023-10-30 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.CharField(max_length=3)),
                ('payment_type', models.CharField(max_length=20)),
                ('card_number', models.CharField(max_length=16)),
                ('expiration_month', models.CharField(max_length=2)),
                ('expiration_year', models.CharField(max_length=4)),
                ('cvv', models.CharField(max_length=3)),
                ('status', models.CharField(max_length=20)),
                ('authorization_code', models.CharField(max_length=20)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
