# Generated by Django 5.0.7 on 2024-08-22 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_category_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='is_published',
            field=models.BooleanField(default=False, help_text='Este campo precisará estar marcado para a página ser exibida publicamente.'),
        ),
    ]