# Generated by Django 4.0.3 on 2022-03-17 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0006_alter_citizendetails_citizenlandline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citizendetails',
            name='CitizenLandLine',
            field=models.CharField(max_length=50),
        ),
    ]
