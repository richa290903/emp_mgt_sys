# Generated by Django 5.1 on 2024-09-23 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emp',
            name='emp_photo',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='emp/'),
        ),
    ]
