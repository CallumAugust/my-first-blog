from django.shortcuts import render

def cv_page(request):
	return render(request, 'cv.html')

def edit_section(request):
	return render(request, 'edit_section.html')
