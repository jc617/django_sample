from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse 
from job.models import Script
# v1

# def index(request):
# 	return HttpResponse("HAMMER II says hey! I am the little bro of HAMMER :) <a href='/job/script/'>Script</a> ")

def index(request):
	context_dict = {'boldmessage': "Comming Soon!"}
	return render(request, 'job/index.html',context = context_dict )

def script(request):
	# return HttpResponse("test page for new view+url <a href='/job/index/'>Index</a>")
	
	script_list = Script.objects.order_by('script_name')
	context_dict = {'scripts': script_list}
	# Render the response and send it back!
	return render(request, 'job/script.html', context_dict)


def post_new(request):
	return HttpResponse("post new script <a href='/job/index/'>Home</a> ")