# Generated by Django 5.0.7 on 2024-07-23 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0013_services_services_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='About_Us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_heading', models.CharField(max_length=100)),
                ('about_point1', models.CharField(max_length=100)),
                ('about_point2', models.CharField(max_length=100)),
                ('about_point3', models.CharField(max_length=100)),
                ('about_point4', models.CharField(max_length=100)),
                ('about_point5', models.CharField(max_length=100)),
                ('about_content', models.TextField()),
            ],
        ),
    ]
