from django import forms
from job.models import Script


class ScriptForm(forms.ModelForm):

	class Meta:
		model = Script
		fields = ['Script_name']


class ScriptCodeForm(ScriptForm):
	code = forms.textbox()
	
	class Meta(ScriptForm.Meta):
		fields = ProfileForm.Meta.fields + ['code']		