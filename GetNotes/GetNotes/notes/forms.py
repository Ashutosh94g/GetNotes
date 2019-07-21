from django import forms
from .models import Notes

class NotesModelForm(forms.ModelForm):
	"""This is a form of django"""
	class Meta:
		model = Notes
		fields = ['department', 'image', 'subject', 'slug']
	
	def clean_data(self, *args, **kwargs):
		department = self.cleaned_data.get('department')
		subject = self.cleaned_data.get('subject')
		qs1 = Notes.objects.filter(department=department)
		qs2= Notes.objects.filter(subject=subject)
		print(qs1)
		print(qs2)
		if qs1.exists() and qs2.exists():
			raise forms.ValidationError('This is not a valid.Its already used')
		return department
