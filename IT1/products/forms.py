from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'My description', 'rows': 6}))
    price = forms.DecimalField()

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
    
    #Writig for User Registration
    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if not email.endswith("edu"):
            return forms.ValidationError("This is not a valid title")
        return email


class RawProductForm(forms.Form):
    email = forms.CharField()
    description = forms.CharField(widget=forms.Textarea(attrs={'cols': 8}))
    price = forms.DecimalField()
