# Generated by Django 2.2.5 on 2020-01-23 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sitename', models.CharField(max_length=150)),
                ('fb', models.CharField(max_length=150)),
                ('tw', models.CharField(max_length=150)),
                ('ig', models.CharField(max_length=150)),
                ('yt', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=150)),
                ('website', models.CharField(max_length=150)),
                ('set_name', models.CharField(max_length=150)),
            ],
        ),
    ]
