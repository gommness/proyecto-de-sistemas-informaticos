from django import forms

class CartAddProductForm(forms.Form):
	"""
		clase que representa el formulario para meter productos en la cesta
		Author: Javier Gomez
	"""
	update = forms.BooleanField(widget=forms.HiddenInput(), initial=False, required=False)
	units = forms.IntegerField(min_value=1,required=True)