# Generated by Django 2.2 on 2022-04-11 12:56

from django.db import migrations, models
import utils.upload
import utils.validators


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0020_auto_20220228_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to=utils.upload.book_image_directory_path, validators=[utils.validators.validate_image_size, utils.validators.validate_image_extension]),
        ),
    ]
