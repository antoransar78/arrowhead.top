# menu/views.py
from django import forms
from django.shortcuts import render
from .models import Customer

class CustomerForm(forms.ModelForm):
    
    class Meta:
        model = Customer
        fields = [
            'service_rating', 'food_rating', 'drinks_rating',
            'ambience_rating', 'cleanliness_rating', 'order', 'comments',
            'compliments', 'visit_reason', 'heard_about_us',
            'first_name', 'email', 'phone',
        ]
        labels = {
            'first_name':'Full Name', 'comments':'Any comment/Suggestion for us:',
            'compliments':'Any compliments for server & food:','visit_reason':'What is the reason for your presence here?',
            'heard_about_us':'Your Visit',
        }
        widgets = {
            'service_rating': forms.RadioSelect,
            'food_rating': forms.RadioSelect,
            'drinks_rating': forms.RadioSelect,
            'ambience_rating': forms.RadioSelect,
            'cleanliness_rating': forms.RadioSelect,
            'order': forms.CheckboxSelectMultiple,
            'visit_reason': forms.CheckboxSelectMultiple,
            'heard_about_us': forms.CheckboxSelectMultiple,
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
        }






