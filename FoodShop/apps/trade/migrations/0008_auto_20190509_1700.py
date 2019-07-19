# Generated by Django 2.2 on 2019-05-09 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0007_auto_20190509_1400'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordergoods',
            old_name='content',
            new_name='comment',
        ),
        migrations.AlterField(
            model_name='ordergoods',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_goods', to='trade.OrderInfo', verbose_name='订单'),
        ),
    ]