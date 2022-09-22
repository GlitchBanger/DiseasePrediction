# Generated by Django 4.1 on 2022-09-18 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('disease_prediction', '0003_records_userdata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdata',
            name='record',
        ),
        migrations.AddField(
            model_name='records',
            name='user',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, to='disease_prediction.userdata'),
            preserve_default=False,
        ),
    ]
