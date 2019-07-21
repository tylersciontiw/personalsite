# Generated by Django 2.2 on 2019-07-21 00:23

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190719_0205'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=100)),
                ('about', tinymce.models.HTMLField()),
                ('featured_image', models.ImageField(blank=True, upload_to='')),
            ],
        ),
    ]