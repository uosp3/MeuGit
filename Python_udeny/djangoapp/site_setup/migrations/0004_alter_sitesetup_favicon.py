# Generated by Django 5.0.7 on 2024-08-20 22:27

import utils.model_validator
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_setup', '0003_sitesetup_favicon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesetup',
            name='favicon',
            field=models.ImageField(blank=True, default='', upload_to='assets/favicon/%Y/%m/', validators=[utils.model_validator.validate_png]),
        ),
    ]