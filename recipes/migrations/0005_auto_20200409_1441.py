# Generated by Django 3.0.4 on 2020-04-09 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_auto_20200406_1519'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ['-created_on', 'course'], 'verbose_name': 'Recipe', 'verbose_name_plural': 'Recipes'},
        ),
    ]
