# Generated by Django 3.2 on 2021-04-23 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('etablissements', '0007_auto_20210423_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='inspection',
            name='dre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inspections', to='etablissements.dre'),
        ),
    ]
