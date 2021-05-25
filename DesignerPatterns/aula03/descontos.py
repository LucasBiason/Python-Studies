# -*- coding: UTF-8 -*-
'''
  Cadeia de responsabilidade, passa o proximo desconto e invoca ele caso precise

  Nota pessoal: o código do MAP não utiliza isso, mas deveria...
'''

class Desconto_por_cinco_itens(object):

    def __init__(self, proximo_desconto):
        self.__proximo_desconto = proximo_desconto

    def calcula(self, orcamento):
        if orcamento.total_itens > 5:
            return orcamento.valor * 0.1
        return self.__proximo_desconto.calcula(orcamento)

class Desconto_por_mais_de_quinhentos_reais(object):

    def __init__(self, proximo_desconto):
        self.__proximo_desconto = proximo_desconto

    def calcula(self, orcamento):
        if orcamento.valor >500:
            return orcamento.valor * 0.07
        return self.__proximo_desconto.calcula(orcamento)


class Sem_desconto(object):

    def calcula(self, orcamento):
        return 0
