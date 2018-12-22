from django import forms

class AddAcountForm(forms.Form):
	number = forms.CharField(max_length=30)
	nickname = forms.CharField(max_length=30)
	#date = forms.CharField(max_length=30)	#forms.DateField()
	language = forms.ChoiceField(choices=((1, 'russian'), (2, 'english')))
	facebook = forms.BooleanField()
	apple = forms.BooleanField()
	google = forms.BooleanField()
	timeInGame = forms.CharField(max_length=30)
	numberOfSessions = forms.CharField(max_length=30)
	sessionTime = forms.CharField(max_length=30)
