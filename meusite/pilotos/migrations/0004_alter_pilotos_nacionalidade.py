# Generated by Django 4.2.7 on 2023-12-03 20:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pilotos", "0003_alter_pilotos_data_de_nascimento"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pilotos",
            name="nacionalidade",
            field=models.CharField(
                blank=True, max_length=200, null=True, verbose_name="nacionalidade"
            ),
        ),
    ]
