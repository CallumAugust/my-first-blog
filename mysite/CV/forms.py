from django import forms

from .models import Post

class PostForm(forms.ModelForm):

	class Meta:
		model = Section
		fields = ('text')
