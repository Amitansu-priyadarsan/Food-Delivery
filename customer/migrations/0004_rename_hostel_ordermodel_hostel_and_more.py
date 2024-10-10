# Generated by Django 5.0.6 on 2024-07-07 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_ordermodel_hostel_ordermodel_block_ordermodel_mobile_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordermodel',
            old_name='Hostel',
            new_name='hostel',
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='mobile',
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='email',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]