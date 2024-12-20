# Generated by Django 4.2.16 on 2024-12-06 01:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_otp.util


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp_secret', models.CharField(default=django_otp.util.random_hex, max_length=32)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
