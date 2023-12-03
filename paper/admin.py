from django.contrib import admin
from . import models

# Register your models here.

class PaperAdmin(admin.ModelAdmin):
    readonly_fields = ['citation']
    # prepopulated_fields = {'slug':['title']}
    list_display=['__str__','citation','field_research','published_in','type','is_active']
    list_filter = ['field_research', 'is_active']
    list_editable=['citation','type','is_active']

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['username', 'Auth_paper']

admin.site.register(models.Paper, PaperAdmin)
admin.site.register(models.Author)
admin.site.register(models.Profile)
admin.site.register(models.Publication)
admin.site.register(models.PaperTag)
admin.site.register(models.FieldResearch)
admin.site.register(models.ConferencePublication)
admin.site.register(models.JournalPublication)

