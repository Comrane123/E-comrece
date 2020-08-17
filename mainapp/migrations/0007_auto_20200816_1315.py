# Generated by Django 3.1 on 2020-08-16 13:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_auto_20200813_1823'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='Name')),
                ('last_name', models.CharField(max_length=255, verbose_name='Surname')),
                ('phone', models.CharField(max_length=20, verbose_name='Phone')),
                ('address', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Address')),
                ('status', models.CharField(choices=[('new', 'New order'), ('in_progress', 'Order processed'), ('ready', 'Order ready'), ('completed', 'Order completed')], default='new', max_length=100, verbose_name='Order status')),
                ('buying_type', models.CharField(choices=[('self', 'Self pick-up'), ('delivery', 'Delivery')], default='self', max_length=100, verbose_name='Order type')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Comment to order')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Order creation date')),
                ('order_date', models.DateField(default=django.utils.timezone.now, verbose_name='Receive date')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_orders', to='mainapp.customer', verbose_name='Buyer')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='orders',
            field=models.ManyToManyField(related_name='related_customer', to='mainapp.Order', verbose_name='Customer orders'),
        ),
    ]