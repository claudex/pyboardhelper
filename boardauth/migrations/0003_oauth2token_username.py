# Generated by Django 3.0.5 on 2020-04-13 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardauth', '0002_oauth2token_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='oauth2token',
            name='username',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
