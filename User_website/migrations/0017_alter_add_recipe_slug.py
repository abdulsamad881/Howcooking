# Generated by Django 4.2 on 2023-04-22 12:06

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_website', '0016_delete_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_recipe',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='title', unique=True, unique_for_date=models.DateField()),
        ),
    ]
