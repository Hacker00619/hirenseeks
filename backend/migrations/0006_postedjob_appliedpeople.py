# Generated by Django 3.2.8 on 2021-11-11 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_alter_postedjob_reqskill'),
    ]

    operations = [
        migrations.AddField(
            model_name='postedjob',
            name='appliedPeople',
            field=models.JSONField(default='{"ID" : [] }'),
        ),
    ]
