# Generated by Django 3.0.7 on 2020-11-30 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('allocation', '0014_item_process'),
    ]

    operations = [
        migrations.AddField(
            model_name='reallocation',
            name='current',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='current', to='allocation.District'),
        ),
    ]
