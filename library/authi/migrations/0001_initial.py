# Generated by Django 4.0.4 on 2022-05-14 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomModelName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=6)),
                ('pass1', models.CharField(max_length=8)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
