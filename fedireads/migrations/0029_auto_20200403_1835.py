# Generated by Django 3.0.3 on 2020-04-03 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fedireads', '0028_auto_20200401_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
