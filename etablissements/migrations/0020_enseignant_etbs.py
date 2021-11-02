# Generated by Django 3.2 on 2021-10-14 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('etablissements', '0019_remove_enseignant_etbs'),
    ]

    operations = [
        migrations.AddField(
            model_name='enseignant',
            name='etbs',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='enseignants', to='etablissements.etablissement'),
        ),
    ]
