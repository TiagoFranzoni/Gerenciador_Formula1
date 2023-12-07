# Generated by Django 4.2.7 on 2023-12-07 18:31

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("pilotos", "0006_alter_pilotos_ativo"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="pilotos",
            options={
                "ordering": ["nome"],
                "permissions": [("can_delete_piloto", "Can delete Piloto")],
                "verbose_name": "Piloto",
                "verbose_name_plural": "Pilotos",
            },
        ),
    ]
