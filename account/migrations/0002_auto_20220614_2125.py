# Generated by Django 3.1.4 on 2022-06-14 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='verified_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='matric_no',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='staff_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
