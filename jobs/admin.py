from django.contrib import admin

from jobs.models import Job


class JobAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'location', 'apply_type', 'remote_type', 'active', 'created_at')
    
    list_display_links = ('id', 'title')
    list_filter = ('id', 'apply_type', 'remote_type', 'active')

    fields = ('title', 'description', 'location', 'apply_type', 'how_to_apply', 'requirements', 'remote_type', 'tags', 'active')

    empty_value_display = '😱'


admin.site.register(Job, JobAdmin)
