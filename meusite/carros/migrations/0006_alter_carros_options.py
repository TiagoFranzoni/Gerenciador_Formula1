# Generated by Django 4.2.7 on 2023-12-07 20:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("carros", "0005_alter_carros_ativo"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="carros",
            options={
                "ordering": ["nome"],
                "permissions": [("can_delete_carro", "Can delete Carro")],
                "verbose_name": "Carro",
                "verbose_name_plural": "Carros",
            },
        ),
    ]
