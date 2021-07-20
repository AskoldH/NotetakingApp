# Generated by Django 3.2.5 on 2021-07-18 11:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0002_auto_20210717_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='priority',
            field=models.CharField(choices=[('H', 'High'), ('M', 'Medium'), ('L', 'Low')], default=django.utils.timezone.now, max_length=1),
            preserve_default=False,
        ),
    ]