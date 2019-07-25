from django.shortcuts import render , get_object_or_404

def home_page(request):
	template_name = 'home.html'
	return render(request,template_name)


def about_page(request):
	template_name = 'base.html'
	return render(request,template_name)


def contect_page(request):
	template_name = 'contect.html'
	return render(request,template_name)
