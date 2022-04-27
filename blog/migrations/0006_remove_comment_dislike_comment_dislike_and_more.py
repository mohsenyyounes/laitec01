# Generated by Django 4.0.4 on 2022-04-27 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_userprofile_comment_remove_userprofile_posts_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='dislike',
        ),
        migrations.AddField(
            model_name='comment',
            name='dislike',
            field=models.ManyToManyField(blank=True, null=True, related_name='comment_dislikes', to='blog.userprofile'),
        ),
        migrations.RemoveField(
            model_name='comment',
            name='like',
        ),
        migrations.AddField(
            model_name='comment',
            name='like',
            field=models.ManyToManyField(blank=True, null=True, related_name='comment_likes', to='blog.userprofile'),
        ),
        migrations.RemoveField(
            model_name='post',
            name='dislike',
        ),
        migrations.AddField(
            model_name='post',
            name='dislike',
            field=models.ManyToManyField(blank=True, null=True, related_name='post_dislikes', to='blog.userprofile'),
        ),
        migrations.RemoveField(
            model_name='post',
            name='like',
        ),
        migrations.AddField(
            model_name='post',
            name='like',
            field=models.ManyToManyField(blank=True, null=True, related_name='post_likes', to='blog.userprofile'),
        ),
    ]
