# Generated by Django 3.2.8 on 2021-11-11 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_remove_userdata_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='compData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=100)),
                ('compName', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=70)),
                ('countryCode', models.CharField(max_length=5)),
                ('contactNumber', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('bio', models.CharField(max_length=300)),
                ('linkGithub', models.TextField(blank=True)),
                ('linkLinkedIn', models.TextField(blank=True)),
                ('linkExtra', models.JSONField(default='{"links" : [] }')),
            ],
        ),
        migrations.CreateModel(
            name='postedJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('jobPos', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=50)),
                ('timing', models.CharField(max_length=50)),
                ('reqSkill', models.CharField(max_length=50)),
                ('expLevel', models.CharField(max_length=50)),
                ('postedBy', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
            ],
        ),
    ]
