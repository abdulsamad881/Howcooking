# Generated by Django 4.2 on 2023-04-23 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_website', '0021_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='subject',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
