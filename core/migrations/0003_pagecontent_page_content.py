# Generated by Django 2.2 on 2019-05-01 07:23

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_pagecontent'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagecontent',
            name='page_content',
            field=tinymce.models.HTMLField(default=''),
        ),
    ]
