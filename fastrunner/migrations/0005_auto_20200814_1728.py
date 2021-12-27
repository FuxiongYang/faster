# Generated by Django 2.1.11 on 2020-08-14 17:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fastrunner', '0004_auto_20200814_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='debugtalk',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='创建时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='debugtalk',
            name='creator',
            field=models.CharField(max_length=20, null=True, verbose_name='创建人'),
        ),
        migrations.AddField(
            model_name='debugtalk',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
        migrations.AddField(
            model_name='debugtalk',
            name='updater',
            field=models.CharField(max_length=20, null=True, verbose_name='更新人'),
        ),
    ]
