from django.db import models
from models import Opinion

class OpinionForm(models.Model):
	fieldsets = [
	        (None,               {'fields': ['name', 'receiver', 'department', 'why_thank', 'anonymous']}),
	        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
	        ('Accept feedback',	 {'fields': ['approved']}),
	    ]
	    list_display = ('name', 'pub_date', 'approved')
	
forms.site.register(Opinion,OpinionForm)