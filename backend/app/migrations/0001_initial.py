# Generated by Django 2.0.4 on 2019-03-21 06:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, null=True)),
                ('screen_name', models.TextField(blank=True, null=True)),
                ('location', models.TextField(blank=True, null=True)),
                ('url', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('follows_count', models.IntegerField(blank=True, null=True)),
                ('followers_count', models.IntegerField(blank=True, null=True)),
                ('listed_count', models.IntegerField(blank=True, null=True)),
                ('favourites_count', models.IntegerField(blank=True, null=True)),
                ('tweets_count', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('like_num', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'user_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('twitter_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.UserInfo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]