from django.forms import ModelForm
from django import forms
from .models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'customer': forms.TextInput(attrs={'class': 'form-control'}),
            'product': forms.TextInput(attrs={'class': 'from-control'}),
            'date_created': forms.SelectDateWidget(attrs={'class': 'form-control'}),
        }
