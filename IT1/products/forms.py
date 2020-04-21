from django import forms
from store.models import Store

from .models import Product


def store_count():
    context = {
        'stores': Store.objects.all()
    }

    return render(request, 'store/home.html', context)


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
