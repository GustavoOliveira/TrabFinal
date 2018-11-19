# Generated by Django 2.1.3 on 2018-11-14 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organizador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('sede', models.CharField(max_length=100)),
                ('presidente', models.CharField(max_length=100)),
                ('fundacao', models.DateTimeField()),
                ('imagem', models.FileField(upload_to='')),
                ('creat_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]