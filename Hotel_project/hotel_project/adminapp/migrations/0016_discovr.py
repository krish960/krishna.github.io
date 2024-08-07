# Generated by Django 5.0.7 on 2024-07-23 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0015_about_us_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discovr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background_image', models.ImageField(upload_to='static/uploads/')),
                ('image_title', models.CharField(max_length=50)),
                ('sub_title', models.CharField(max_length=100)),
                ('video_link', models.TextField()),
            ],
        ),
    ]
