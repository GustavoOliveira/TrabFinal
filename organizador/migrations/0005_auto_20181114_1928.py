# Generated by Django 2.1.3 on 2018-11-14 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizador', '0004_auto_20181114_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizador',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]