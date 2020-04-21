from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'My description', 'rows': 6}))
    price = forms.DecimalField(),
    image = forms.ImageField(),

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'image',
            'price',
        ]


class RawProductForm(forms.Form):
    email = forms.CharField()
    description = forms.CharField(widget=forms.Textarea(attrs={'cols': 8}))
    price = forms.DecimalField()
