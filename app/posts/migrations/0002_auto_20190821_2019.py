# Generated by Django 2.1.5 on 2019-08-21 11:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='postlike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='like_users',
            field=models.ManyToManyField(related_name='like_posts', related_query_name='like_post', through='posts.Postlike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='postTags',
            field=models.ManyToManyField(blank=True, to='posts.HashTags'),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_set', related_query_name='comments', to='posts.Post', verbose_name='포스트'),
        ),
        migrations.AddField(
            model_name='comment',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='comment_set', related_query_name='comments', to='posts.HashTags'),
        ),
        migrations.AlterUniqueTogether(
            name='postlike',
            unique_together={('post', 'user')},
        ),
    ]
