# Generated by Django 3.0.6 on 2020-06-04 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='memobj',
            fields=[
                ('mem_id', models.AutoField(primary_key=True, serialize=False)),
                ('mem_tag', models.CharField(max_length=50)),
                ('mem_img', models.ImageField(upload_to='meme/images')),
            ],
        ),
    ]
