# Generated by Django 3.0.7 on 2020-11-27 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('allocation', '0007_auto_20201127_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='initiator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='allocation.Profile'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='initiator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='allocation.Profile'),
        ),
    ]
