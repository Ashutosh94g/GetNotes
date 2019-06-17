from django import forms
from .models import Notes

class NotesModelForm(forms.ModelForm):
	class Meta:
		model = Notes
		fields = ['department','subject','slug'] 