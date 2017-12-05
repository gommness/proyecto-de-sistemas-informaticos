from django import forms
from placeorder.models import Order

class OrderCreateForm(forms.ModelForm):
	maxLen = 128
	firstName = forms.CharField(max_length=maxLen, help_text="Please enter your first name")
	familyName = forms.CharField(max_length=maxLen, help_text="Please enter your family name")
	email = forms.EmailField(max_length=maxLen, help_text="Please enter your email")
	address = forms.CharField(max_length=maxLen, help_text="Please enter your address")
	zip = forms.CharField(max_length=maxLen, help_text="Please enter your zip code")
	city = forms.CharField(max_length=maxLen, help_text="Please enter your city")

	class Meta:
		# Provide an association between the ModelForm and a model
		model = Order
		fields = ('firstName','familyName','email','address','zip','city')