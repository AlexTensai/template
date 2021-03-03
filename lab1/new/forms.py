from django import forms
from .models import Product, Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product

        fields = [
            "headline",
            "category",
        ]

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category

        fields = [
            "category_name",
            "categoryId",
            "type_name",
        ]