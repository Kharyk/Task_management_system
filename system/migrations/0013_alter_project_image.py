# Generated by Django 4.2.13 on 2024-08-24 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0012_alter_task_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/img/projects/'),
        ),
    ]
