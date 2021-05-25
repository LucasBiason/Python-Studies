# -*- coding: UTF-8 -*-


class Calculador_de_impostos(object):

    def realiza_calculo(self, orcamento, imposto):

        importo_calculado = imposto.calcula(orcamento)

        print importo_calculado


if __name__ == '__main__':
    from orcamento import Orcamento
    from impostos import IKCV, ICPP, ISS, ICMS

    calculador = Calculador_de_impostos()

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('ITEM 1', 50))
    orcamento.adiciona_item(Item('ITEM 2', 200))
    orcamento.adiciona_item(Item('ITEM 3', 250))

    calculador.realiza_calculo(orcamento, ISS())
    calculador.realiza_calculo(orcamento, ICMS())

    calculador.realiza_calculo(orcamento, IKCV())
    calculador.realiza_calculo(orcamento, ICPP())

'''


'''
