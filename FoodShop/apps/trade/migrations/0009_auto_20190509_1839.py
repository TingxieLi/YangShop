# Generated by Django 2.2 on 2019-05-09 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0008_auto_20190509_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfo',
            name='order_num',
            field=models.CharField(blank=True, max_length=30, unique=True, verbose_name='订单号'),
        ),
    ]