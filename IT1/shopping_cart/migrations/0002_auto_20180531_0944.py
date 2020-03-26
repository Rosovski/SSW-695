from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='VAT',
        ),
        migrations.RemoveField(
            model_name='order',
            name='voucher_applied',
        ),
    ]