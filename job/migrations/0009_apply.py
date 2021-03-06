# Generated by Django 3.1.4 on 2020-12-26 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_auto_20201226_0427'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('website', models.URLField()),
                ('vc', models.FileField(upload_to='apply/')),
                ('cover_letter', models.TextField(max_length=500)),
            ],
        ),
    ]
