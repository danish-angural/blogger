# Generated by Django 3.0.4 on 2020-03-28 14:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0008_auto_20200328_1415'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_profile',
            name='id',
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key='True', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
