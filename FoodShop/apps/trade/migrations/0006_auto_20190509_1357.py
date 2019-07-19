# Generated by Django 2.2 on 2019-05-09 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0005_auto_20190508_2249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderinfo',
            name='message',
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='freight',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True, verbose_name='运费'),
        ),
    ]