# Generated by Django 2.1.5 on 2019-05-03 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=500, verbose_name='작성 글')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='작성 날')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정 날짜')),
            ],
            options={
                'verbose_name': '댓글',
                'verbose_name_plural': '댓글 목록',
            },
        ),
        migrations.CreateModel(
            name='HashTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': '해시태그',
                'verbose_name_plural': '해시태그 목록',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=500, verbose_name='작성 글')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성 날짜')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='수정 날짜')),
                ('image', models.ImageField(blank=True, default=True, null=True, upload_to='post', verbose_name='게시글 이미지')),
            ],
            options={
                'verbose_name': '게시글',
                'verbose_name_plural': '게시글 목록',
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='Postlike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '게시글 좋아요',
                'verbose_name_plural': '게시글 좋아요 목록',
            },
        ),
        migrations.CreateModel(
            name='SignatureTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.ManyToManyField(blank=True, null=True, to='members.Player')),
            ],
            options={
                'verbose_name': '유저 지정 팀',
                'verbose_name_plural': '유저 지정 팀 목록',
            },
        ),
    ]