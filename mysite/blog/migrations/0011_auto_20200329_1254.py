# Generated by Django 3.0.4 on 2020-03-29 12:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0010_auto_20200329_0916'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='draft_status',
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='nickname',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
