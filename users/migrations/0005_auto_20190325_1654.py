# Generated by Django 2.1.7 on 2019-03-25 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190324_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='passport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Passport', verbose_name='账户'),
        ),
    ]