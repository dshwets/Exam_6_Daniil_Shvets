from django.contrib import admin
from webapp.models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_filter = ('status',)
    list_display = ('pk', 'name', 'text', 'created_at')
    list_display_links = ('pk', 'name')
    search_fields = ('name',)


admin.site.register(Feedback, FeedbackAdmin)
