# Generated by Django 4.2.13 on 2024-08-24 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0013_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/projects/'),
        ),
    ]