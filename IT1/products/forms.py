from django import forms
from .models import Product, Comment


class ProductForm(forms.ModelForm):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'My description', 'rows': 6}))
    price = forms.DecimalField(),
    image = forms.ImageField(),
    store = forms. CharField(),

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


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('rating', 'content', )
