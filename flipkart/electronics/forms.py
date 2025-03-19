from django import forms
from .models import Product


#pascal case ex: ProductForm
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['id','name','price','description']