# Generated by Django 5.0.7 on 2024-07-22 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0011_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('services_image', models.ImageField(upload_to='static/uploads/')),
                ('services_name', models.TextField()),
            ],
        ),
    ]
