# Generated by Django 2.2 on 2022-02-28 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_auto_20220228_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(default='Алматы', max_length=500),
        ),
    ]
