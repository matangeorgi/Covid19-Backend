# Generated by Django 4.0.3 on 2022-03-17 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citizendetails',
            name='CitizenCellular',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='citizendetails',
            name='CitizenDOB',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='citizendetails',
            name='CitizenZipCode',
            field=models.IntegerField(),
        ),
    ]
