# Generated by Django 2.0.5 on 2018-05-27 21:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ej_conversations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='votes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='vote',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='ej_conversations.Comment'),
        ),
        migrations.AddField(
            model_name='taggedconversation',
            name='content_object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ej_conversations.Conversation'),
        ),
        migrations.AddField(
            model_name='taggedconversation',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ej_conversations_taggedconversation_items', to='taggit.Tag'),
        ),
        migrations.AddField(
            model_name='conversation',
            name='author',
            field=models.ForeignKey(help_text='Only the author and administrative staff can edit this conversation.', on_delete=django.db.models.deletion.CASCADE, related_name='conversations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='conversation',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='ej_conversations.TaggedConversation', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='conversation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='ej_conversations.Conversation'),
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together={('author', 'comment')},
        ),
        migrations.AlterUniqueTogether(
            name='comment',
            unique_together={('conversation', 'content')},
        ),
    ]