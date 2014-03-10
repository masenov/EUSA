from django.contrib import admin
from polls.models import Opinion

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'receiver', 'department', 'why_thank', 'anonymous']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        ('Accept feedback',	 {'fields': ['approved']}),
    ]
    list_display = ('name', 'pub_date', 'approved')
    list_filter = ['pub_date']
admin.site.register(Opinion, PollAdmin)

# Register your models here.
