# Generated by Django 3.2 on 2021-10-13 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etablissements', '0017_auto_20211013_0949'),
    ]

    operations = [
        migrations.AddField(
            model_name='enseignant',
            name='photo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='enseignant',
            name='contact',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
