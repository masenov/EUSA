from django.db import models
from django.utils import timezone
from django.forms import ModelForm
import datetime

class Opinion(models.Model):
	MODERATED = (
        ('Y', 'accepted'),
        ('N', 'reject'),
        ('-', 'unmoderated'),
    )
	name = models.CharField(max_length=200)
	receiver = models.CharField(max_length=200)
	department = models.CharField(max_length=200)
	feedback = models.CharField(max_length=200)
	anonymous = models.BooleanField(default=False)
	moderated = models.CharField(max_length=1, choices=MODERATED, default='-')
	pub_date = models.DateTimeField('date published', default=timezone.now())
	def __unicode__(self):  # Python 3: def __str__(self):
		return self.feedback
	def was_published_recently(self):
    		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    	was_published_recently.admin_order_field = 'pub_date'
    	was_published_recently.boolean = True
    	was_published_recently.short_description = 'Published recently?'


class OpinionForm(ModelForm):
    class Meta:
        model = Opinion
        fields = ['name', 'receiver', 'department', 'feedback', 'anonymous']

# Create your models here.
