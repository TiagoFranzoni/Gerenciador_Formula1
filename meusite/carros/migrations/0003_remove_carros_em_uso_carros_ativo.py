# Generated by Django 4.2.7 on 2023-12-03 19:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("carros", "0002_carros_equipe"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="carros",
            name="em_uso",
        ),
        migrations.AddField(
            model_name="carros",
            name="ativo",
            field=models.BooleanField(
                blank=True, default=False, null=True, verbose_name="ativo"
            ),
        ),
    ]
