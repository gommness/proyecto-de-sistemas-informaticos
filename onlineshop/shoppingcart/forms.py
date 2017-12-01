from django import forms

class CartAddProductForm(forms.Form):
	update = forms.BooleanField(widget=forms.HiddenInput(), initial=False, required=False)
	units = forms.IntegerField(min_value=1,required=True)