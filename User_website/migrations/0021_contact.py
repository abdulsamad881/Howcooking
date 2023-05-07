# Generated by Django 4.2 on 2023-04-23 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_website', '0020_alter_add_recipe_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('query_or_problem', models.TextField()),
            ],
        ),
    ]
