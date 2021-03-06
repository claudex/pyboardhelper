# Generated by Django 3.0.5 on 2020-04-13 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DlfpAuth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oauth_referecne', models.CharField(max_length=256)),
                ('cookie_id', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='OAuth2Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('token_type', models.CharField(max_length=40)),
                ('access_token', models.CharField(max_length=200)),
                ('refresh_token', models.CharField(max_length=200)),
                ('expires_at', models.PositiveIntegerField()),
            ],
        ),
    ]
