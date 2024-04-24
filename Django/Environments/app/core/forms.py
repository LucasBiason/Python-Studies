from core.models import Estoque
from django import forms


class InsereItemForm(forms.ModelForm):

    class Meta:
        model = Estoque

        fields = [
            'codigo',
            'nome',
            'quantidade'
        ]
