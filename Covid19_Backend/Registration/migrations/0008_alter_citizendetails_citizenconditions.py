# Generated by Django 4.0.3 on 2022-03-21 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0007_alter_citizendetails_citizenlandline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citizendetails',
            name='CitizenConditions',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]