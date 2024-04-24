from django.test import TestCase
from core.forms import InsereItemForm


class IsereItemFormTest(TestCase):
    def setUp(self):
        self.form = InsereItemForm()

    def test_campos_form(self):
        """Form precisa ter 3 campos"""
        esperado = ['codigo', 'nome', 'quantidade']
        self.assertSequenceEqual(esperado, list(self.form.fields))

    def test_preencher_form_valido(self):
        """Form preenchido precisa ser valido"""
        valid = {'codigo': 100,
                 'nome': 'vassoura',
                 'quantidade': 3}
        form = InsereItemForm(data=valid)
        self.assertTrue(form.is_valid())

    def test_preencher_form_invalido(self):
        """Form preenchido precisa ser invalido"""
        valid = {'codigo': 100,
                 'quantidade': 3}
        form = InsereItemForm(data=valid)
        self.assertFalse(form.is_valid())
