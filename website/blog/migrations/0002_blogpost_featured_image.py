# Generated by Django 2.2 on 2019-06-16 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='featured_image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
