# Generated by Django 4.2.7 on 2023-12-04 00:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pilotos", "0005_alter_pilotos_ativo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pilotos",
            name="ativo",
            field=models.BooleanField(default=True, verbose_name="ativo"),
        ),
    ]