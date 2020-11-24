# Generated by Django 3.1.2 on 2020-10-19 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20201007_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='ar',
            field=models.FloatField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='customer_country',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='document_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='ptp',
            field=models.DateTimeField(null=True),
        ),
    ]
