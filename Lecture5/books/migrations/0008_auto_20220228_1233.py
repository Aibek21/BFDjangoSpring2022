# Generated by Django 2.2 on 2022-02-28 12:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
