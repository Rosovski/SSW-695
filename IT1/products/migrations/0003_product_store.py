# Generated by Django 3.0.3 on 2020-03-12 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200312_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='store',
            field=models.TextField(default='Unknown Store'),
        ),
    ]
