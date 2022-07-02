# Generated by Django 4.0.5 on 2022-06-04 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano_veiculo', models.CharField(max_length=200)),
                ('marca_veiculo', models.CharField(max_length=200)),
                ('modelo_veiculo', models.CharField(max_length=200)),
                ('servicos', models.TextField(blank=True)),
                ('comentarios', models.TextField(blank=True)),
                ('data_do_agendamento', models.DateTimeField()),
                ('tipo_contato', models.CharField(max_length=100)),
                ('nome', models.CharField(max_length=200)),
                ('sobrenome', models.CharField(max_length=200)),
                ('cpf', models.CharField(max_length=20)),
                ('telefone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('confirmado', models.BooleanField(default=False)),
                ('servico_realizado', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Agendamento',
                'verbose_name_plural': 'Agendamentos',
            },
        ),
    ]
