from django.shortcuts import render
from .models import Section

def cv_page(request):
	sections = Section.objects.all()
	return render(request, 'cv.html', {'sections':sections})

def edit_section(request):
	return render(request, 'edit_section.html')
