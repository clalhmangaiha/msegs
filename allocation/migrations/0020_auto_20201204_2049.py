# Generated by Django 3.0.7 on 2020-12-04 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('allocation', '0019_reallocation_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='iteminfo',
            name='Manufacturer',
        ),
        migrations.RemoveField(
            model_name='iteminfo',
            name='colours',
        ),
        migrations.AddField(
            model_name='iteminfo',
            name='colour',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='iteminfo',
            name='current_value',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='iteminfo',
            name='purchased_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='iteminfo',
            name='purchased_price',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='iteminfo',
            name='salvage_value',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='iteminfo',
            name='useful_life',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='iteminfo',
            name='item',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='allocation.Item'),
        ),
        migrations.AddField(
            model_name='iteminfo',
            name='manufacturer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='allocation.Manufacturer'),
        ),
    ]
