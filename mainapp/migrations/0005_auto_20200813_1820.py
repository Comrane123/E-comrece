# Generated by Django 3.1 on 2020-08-13 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20200813_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.customer', verbose_name='Owner'),
        ),
    ]
