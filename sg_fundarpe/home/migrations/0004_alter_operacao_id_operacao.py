# Generated by Django 4.2.11 on 2024-05-13 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_pagamento_descricao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operacao',
            name='id_operacao',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
