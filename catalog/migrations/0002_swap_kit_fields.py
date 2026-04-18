from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="kit",
            old_name="cost",
            new_name="sale_price_temp",
        ),
        migrations.RenameField(
            model_name="kit",
            old_name="price",
            new_name="cost",
        ),
        migrations.RenameField(
            model_name="kit",
            old_name="sale_price_temp",
            new_name="sale_price",
        ),
    ]
