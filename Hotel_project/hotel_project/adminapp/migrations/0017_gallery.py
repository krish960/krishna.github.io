# Generated by Django 5.0.7 on 2024-07-25 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0016_discovr'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_image1', models.ImageField(upload_to='static/uploads/')),
            ],
        ),
    ]
