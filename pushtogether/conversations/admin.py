from django.contrib import admin

from .models import Conversation, Comment, Vote

class CommentInline(admin.TabularInline):
    model = Comment


class ConversationAdmin(admin.ModelAdmin):
    fields = ['author', 'title', 'description', 'polis_id']
    list_display = ['id', 'title', 'author', 'created_at', 'updated_at']
    inlines = [CommentInline]


class CommentAdmin(admin.ModelAdmin):
    fields = ['conversation', 'author', 'content', 'polis_id', 'is_approved']
    list_display = ['id', 'content', 'conversation', 'created_at', 'is_approved']
    list_filter = ['is_approved']


admin.site.register(Conversation, ConversationAdmin)
admin.site.register(Comment, CommentAdmin)
