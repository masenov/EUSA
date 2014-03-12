from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.http import HttpResponse
from django.forms import ModelForm
from django import forms
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from polls.models import Opinion, OpinionForm
from django.core.mail import send_mail, mail_admins

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        """Return the last five published polls."""
        return Opinion.objects.filter(moderated='Y')

def create(request):
	if request.POST:
		form = OpinionForm(request.POST)
		if form.is_valid():
			form.save()
			send_mail('test','test email', '',[''], fail_silently=True) #3rd argument is mail sender, 4th is mail receiver; can use mail_admins in the final version
			return HttpResponseRedirect('/polls/thankyou')													
	else:
			form = OpinionForm()
	args = {}
	args.update(csrf(request))
	args['form'] = form
	return render(request, 'polls/write.html', args)

def thankyou(request):
	template_name = 'polls/thankyou.html'
	return render(request, 'polls/thankyou.html')


