from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render

from .models import SiteSetting

# Create your views here.

def index(request):

	setting = SiteSetting.objects.get(pk=1)
	return render(request, 'front/index.html', {'setting':setting})

def about(request):
	
	setting = SiteSetting.objects.get(pk=1)
	return render(request, 'front/about.html', {'setting':setting})	

def news_detail(request):
	
	setting = SiteSetting.objects.get(pk=1)
	return render(request, 'front/news_detail.html', {'setting':setting})	
