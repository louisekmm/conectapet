# Generated by Django 2.2a1 on 2020-11-09 02:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conectapet', '0002_estado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=120, null=True)),
                ('estado_uf', models.CharField(blank=True, max_length=5, null=True)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conectapet.Estado')),
            ],
        ),
    ]
