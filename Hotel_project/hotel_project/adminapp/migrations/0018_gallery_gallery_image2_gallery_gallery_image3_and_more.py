# Generated by Django 5.0.7 on 2024-07-25 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0017_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='gallery_image2',
            field=models.ImageField(null=True, upload_to='static/uploads/'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='gallery_image3',
            field=models.ImageField(null=True, upload_to='static/uploads/'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='gallery_image4',
            field=models.ImageField(null=True, upload_to='static/uploads/'),
        ),
    ]
