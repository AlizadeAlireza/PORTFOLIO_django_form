# Generated by Django 4.0.6 on 2022-07-11 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_project_description_alter_project_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(null=True, upload_to='ProjectImages/'),
        ),
    ]