# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from .models import Producto

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',) 


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email'] 


class ValoracionForm(forms.Form):
    valoracion = forms.ChoiceField(choices=[(i, f'{i} estrellas') for i in range(1, 6)], label='Valoración')
    comentario = forms.CharField(widget=forms.Textarea, required=False) 


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['titulo', 'imagenes', 'descripcion', 'precio']