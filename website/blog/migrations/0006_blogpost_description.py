# Generated by Django 2.2 on 2019-12-23 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blogpost_draft_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='description',
            field=models.CharField(blank=True, max_length=160, null=True),
        ),
    ]
