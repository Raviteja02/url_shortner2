# Generated by Django 2.2.4 on 2019-08-03 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortURL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True, verbose_name='Your URL to shorten')),
                ('code', models.CharField(max_length=4, unique=True)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date of registration')),
                ('nb_access', models.IntegerField(default=0, verbose_name='Number of accesses to the URL')),
            ],
            options={
                'verbose_name': 'Short URL',
                'verbose_name_plural': 'Short URLs',
            },
        ),
    ]
