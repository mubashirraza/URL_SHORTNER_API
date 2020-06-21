from django.shortcuts import render, redirect
from .models import ShortUrl
from .forms import UrlForm
from .shorten import Shortner

# Create your views here.
def home(request, token):
	long_url= ShortUrl.objects.filter(short_url=token)[0]
	return redirect(long_url.long_url)


def make(request):
	form = UrlForm(request.POST)
	token = "" 
	if request.method == 'POST':
		if form.is_valid():
			new_url = form.save(commit=False)
			token = Shortner().issue_token()
			new_url.short_url = token
			new_url.save()
		else:
			form = UrlForm()
			token = "invalid"


	return render(request, 'home.html',{'form':form, 'token':token})
