'''this is views'''
from django.shortcuts import render

def home_page(request):
	"""this is home page"""
	template_name = 'home.html'
	return render(request, template_name)


def about_page(request):
	"""this is a about page"""
	template_name = 'about.html'
	return render(request, template_name)


def contect_page(request):
	"""this is a contect page"""
	template_name = 'contect.html'
	return render(request, template_name)
	