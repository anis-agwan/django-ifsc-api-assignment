# Generated by Django 3.0.8 on 2020-07-03 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bank',
            options={'ordering': ('bank_name',)},
        ),
        migrations.RenameField(
            model_name='bank',
            old_name='bankName',
            new_name='bank_name',
        ),
        migrations.RenameField(
            model_name='branch',
            old_name='bank',
            new_name='bank_name',
        ),
    ]