# Generated by Django 5.1.3 on 2024-11-21 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_house_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='work_image',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
