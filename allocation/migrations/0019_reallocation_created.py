# Generated by Django 3.0.7 on 2020-12-04 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allocation', '0018_request_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='reallocation',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]