# Generated by Django 3.2.4 on 2021-08-26 22:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciamento', '0003_remove_funcionario_ampanha'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gerenciamento.empresa'),
        ),
    ]
