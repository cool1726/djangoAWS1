# Generated by Django 3.0.8 on 2020-07-27 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='editor',
            field=models.CharField(default='user', max_length=20),
            preserve_default=False,
        ),
    ]
