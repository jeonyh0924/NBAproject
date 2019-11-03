# Generated by Django 2.1.5 on 2019-11-03 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=500, verbose_name='댓글 내용')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='작성 날')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정 날짜')),
                ('_html', models.TextField(blank=True, verbose_name='태그가 html화 된 댓글 내용')),
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
                ('name', models.CharField(max_length=100, unique=True, verbose_name='태그명')),
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
                ('title', models.TextField(max_length=40, verbose_name='제목')),
                ('content', models.TextField(max_length=500, verbose_name='작성 글')),
                ('tag', models.TextField(blank=True, max_length=50, null=True, verbose_name='태그')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성 날짜')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='수정 날짜')),
                ('image', models.ImageField(blank=True, default=True, null=True, upload_to='post', verbose_name='업로드 이미지')),
                ('_html', models.TextField(blank=True, verbose_name='태그가 html화 된 댓글 내용')),
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
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Post')),
            ],
            options={
                'verbose_name': '게시글 좋아요',
                'verbose_name_plural': '게시글 좋아요 목록',
            },
        ),
    ]
