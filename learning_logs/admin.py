from django.contrib import admin
from django.utils.html import format_html
from .models import Topic, Entry

class EntryInLine(admin.TabularInline):
    """Shows entries connected to the topic."""
    model = Entry

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    search_fields = ['owner']
    list_display = ['id', 'owner', 'date_added', 'text']
    list_filter = ['owner']
    inlines = [EntryInLine]

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ['id', 'topic', 'title', 'date_added']
    list_filter = ['topic']

