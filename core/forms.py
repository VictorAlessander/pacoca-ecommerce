from django import forms
from .models import Order


class FilterForm(forms.ModelForm):

	def __init__(self, user, *args, **kwargs):
		super(FilterForm, self).__init__(*args, **kwargs)

		database = Order.objects.all().filter(owner=user)
		order_choices = database.values_list('order_id', flat=True).distinct()
		iorder_choices = [('', 'None')] + [(id, id) for id in order_choices]
		self.fields['order_id'] = forms.ChoiceField(choices=iorder_choices, widget=forms.Select(), required=False)


	class Meta:
		model = Order

		fields = ('order_id',)