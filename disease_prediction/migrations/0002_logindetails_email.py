# Generated by Django 4.1 on 2022-09-05 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disease_prediction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='logindetails',
            name='email',
            field=models.EmailField(default='abc@xyz.pqr', max_length=50),
            preserve_default=False,
        ),
    ]
