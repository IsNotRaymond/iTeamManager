from django import forms
from .models import Categoria, Projeto


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']
