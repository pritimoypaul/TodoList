# Generated by Django 2.2 on 2019-05-23 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='todos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todoName', models.CharField(max_length=124)),
                ('description', models.TextField()),
                ('is_complete', models.BooleanField(default=False)),
            ],
        ),
    ]
