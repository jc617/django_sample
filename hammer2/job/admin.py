from django.contrib import admin


# Register your models here.
from job.models import Script

class ScriptAdmin(admin.ModelAdmin):
	flist_display = ['script_name','created_date', 'modified_date']

admin.site.register(Script, ScriptAdmin)
