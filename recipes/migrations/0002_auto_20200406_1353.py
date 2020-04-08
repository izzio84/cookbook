# Generated by Django 3.0.4 on 2020-04-06 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='prepatation',
            new_name='preparation',
        ),
        migrations.AddField(
            model_name='recipe',
            name='main_ingredient',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
