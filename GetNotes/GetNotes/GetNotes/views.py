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


def contact_page(request):
	"""this is a contact page"""
	template_name = 'contact.html'
	return render(request, template_name)
	