# Generated by Django 3.2 on 2021-05-01 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('etablissements', '0012_auto_20210428_1943'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatiereClasse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coef', models.IntegerField(default=1)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('classe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='matieres', to='etablissements.classe')),
                ('enseigant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='matieres', to='etablissements.enseignant')),
                ('matiere', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='matieres', to='etablissements.matiere')),
            ],
            options={
                'verbose_name': 'Matière de la classe',
                'verbose_name_plural': 'Matières de la classe',
                'db_table': 'matiere_classe',
            },
        ),
    ]
