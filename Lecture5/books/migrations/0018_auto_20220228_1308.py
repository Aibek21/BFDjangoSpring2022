# Generated by Django 2.2 on 2022-02-28 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0017_auto_20220228_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publisher',
            name='name',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Название'),
        ),
    ]
