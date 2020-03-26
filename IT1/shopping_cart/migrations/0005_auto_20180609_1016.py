from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0004_transaction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='transaction_id',
            new_name='token',
        ),
    ]