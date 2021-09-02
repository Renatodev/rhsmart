# Generated by Django 3.2.4 on 2021-08-26 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciamento', '0005_quadro'),
        ('comunicacao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atendimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pedido', models.TextField(max_length=200)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, null=True)),
                ('funcionario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gerenciamento.funcionario')),
                ('servico', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='comunicacao.servico')),
            ],
            options={
                'verbose_name_plural': 'Atendimentos',
                'ordering': ['created_on'],
            },
        ),
    ]
