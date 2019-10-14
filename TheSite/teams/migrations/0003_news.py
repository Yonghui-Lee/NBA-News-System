# Generated by Django 2.2.5 on 2019-09-05 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_auto_20190905_0933'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=200)),
                ('posttime', models.TextField(max_length=200)),
                ('author', models.TextField(max_length=200)),
                ('content', models.TextField(max_length=200000)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.Team')),
            ],
        ),
    ]
