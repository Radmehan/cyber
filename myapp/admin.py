from django.contrib import admin
from .models import *
from import_export.admin import ExportActionMixin

class CyberAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('schedule_id', 'name', 'email', 'contact', 'address', 'subject', 'message', 'date')

admin.site.register(Contact)
admin.site.register(Schedule, CyberAdmin)