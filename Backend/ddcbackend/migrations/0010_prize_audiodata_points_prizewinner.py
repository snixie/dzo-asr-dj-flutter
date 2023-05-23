# Generated by Django 4.1.7 on 2023-05-08 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ddcbackend', '0009_audiodata_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='prize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_prize', models.IntegerField()),
                ('second_prize', models.IntegerField()),
                ('third_prize', models.IntegerField()),
                ('time_of_result', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='audiodata',
            name='points',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='prizewinner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('first', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='first_prizewinners', to='ddcbackend.userdata')),
                ('second', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='second_prizewinners', to='ddcbackend.userdata')),
                ('third', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='third_prizewinners', to='ddcbackend.userdata')),
            ],
        ),
    ]