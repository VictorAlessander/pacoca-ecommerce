from django import forms
from .models import Order


class FilterForm(forms.ModelForm):

	database = Order.objects.all()

	session_choices = database.values_list('session_id', flat=True).distinct()
	isession_choices = [('', 'None')] + [(id, id) for id in session_choices]
	session_id = forms.ChoiceField(choices=isession_choices, widget=forms.Select(), required=False)

	class Meta:
		model = Order

		fields = ('session_id',)