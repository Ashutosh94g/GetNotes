from django import forms
from .models import Notes

class NotesModelForm(forms.ModelForm):
	"""This is a form of django"""
	class Meta:
		model = Notes
		fields = ['department', 'subject', 'slug'] 