from django.contrib import admin
from polls.models import Opinion

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'receiver', 'department', 'feedback', 'anonymous']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        ('Accept feedback',	 {'fields': ['moderated']}),
    ]
    list_display = ('name', 'pub_date', 'moderated')
    list_filter = ['pub_date', 'moderated']

admin.site.register(Opinion, PollAdmin)

# Register your models here.
