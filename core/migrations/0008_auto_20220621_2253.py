# Generated by Django 3.2.6 on 2022-06-21 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_invoice_finish_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='billingproject',
            name='email_notification',
            field=models.EmailField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='flavorprice',
            name='flavor_id',
            field=models.CharField(max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name='volumeprice',
            name='volume_type_id',
            field=models.CharField(max_length=256, unique=True),
        ),
    ]
