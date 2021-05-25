# -*- coding: UTF-8 -*-
# orcamento.py
class Orcamento(object):
  def __init__(self, valor):
    self._valor = valor

  @property
  def valor(self):
    return self._valor

'''
Criamos o atributo valor como property , mas com acesso de apenas leitura.
Isso garante que o valor recebido pelo construtor não seja alterado depois do
orçamento criado. Com certeza uma grande vantagem do paradigma da orientação à
objetos, pois estamos encapsulando o valor do orçamento, permitindo acesso
apenas à leitura.

Com isso, podemos criar novos orçamentos, instanciando objetos do respectivo
tipo e caso queiramos calcular um imposto sobre seu valor, basta utilizarmos a
property valor para isso. Assim, podemos estipular que o ICMS valha 10% e
precisamos calculá-lo, baseado no valor do orçamento.
'''
